from openai import OpenAI
from openai import AssistantEventHandler
from typing_extensions import override
from model.conversation_storage import store_conversation


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
  def __init__(self):
    super().__init__()
    self.accumulated_output = ""

  @override
  def on_text_created(self, text) -> None:
      # Accumulate instead of printing
      self.accumulated_output += "\nassistant > "

  @override
  def on_text_delta(self, delta, snapshot):
      # Accumulate text changes
      self.accumulated_output += delta.value

  def on_tool_call_created(self, tool_call):
      # Accumulate tool call notifications
      self.accumulated_output += f"\nassistant > {tool_call.type}\n"

  def on_tool_call_delta(self, delta, snapshot):
      if delta.type == 'code_interpreter':
          if delta.code_interpreter.input:
              self.accumulated_output += delta.code_interpreter.input
          if delta.code_interpreter.outputs:
              self.accumulated_output += "\n\noutput >"
              for output in delta.code_interpreter.outputs:
                  if output.type == "logs":
                      self.accumulated_output += f"\n{output.logs}"

  def get_accumulated_output(self):
      # Method to get the accumulated output
      return self.accumulated_output
 

# Then, we use the `create_and_stream` SDK helper 
# with the `EventHandler` class to create the Run 
# and stream the response.

def gpt_call(name, question):
  thread_id, assistant_id = _assistant_call(question=question)

  handle_event = EventHandler()

  with client.beta.threads.runs.create_and_stream(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions=f"Please address the user as {name}. The user has a premium account.",
    event_handler=handle_event,
  ) as stream:
    stream.until_done()
  
  # After streaming is done, retrieve the accumulated output
  full_output = handle_event.get_accumulated_output()
  store_conversation(question, full_output)
  print(full_output)  # or return full_output for further processing
