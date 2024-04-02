from openai import OpenAI
from openai import AssistantEventHandler
from typing_extensions import override


client = OpenAI()

def _assistant_call(question):
  assistant = client.beta.assistants.create(
    name="Immigration Paralegal",
    instructions="You are a united states paralegal assistant, help this non-citizen with immigration questions",
    tools=[{"type": "code_interpreter"}],
  #   model="gpt-4-turbo-preview",
    model="gpt-3.5-turbo-0125",
    # model="US Immigration Law AI",
    # https://chat.openai.com/g/g-2g79Fgyn6-us-immigration-law-ai
  )

  thread = client.beta.threads.create()

  message = client.beta.threads.messages.create(
      thread_id=thread.id,
      role="user",
      content=question
  )

  return thread.id, assistant.id

# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.
 
class EventHandler(AssistantEventHandler):
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)
 

# Then, we use the `create_and_stream` SDK helper 
# with the `EventHandler` class to create the Run 
# and stream the response.

def gpt_call(name, question):
  thread_id, assistant_id = _assistant_call(question=question)

  with client.beta.threads.runs.create_and_stream(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions=f"Please address the user as {name}. The user has a premium account.",
    event_handler=EventHandler(),
  ) as stream:
    stream.until_done() 
