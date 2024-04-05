import psycopg2 as psy
from psycopg2.extras import execute_values
import os
from openai import OpenAI
from langchain.text_splitter import NLTKTextSplitter


def split_text(text):
    print("Splitting the text with langchain")
    text_splitter = NLTKTextSplitter()
    chunks = text_splitter.split_text(text)
    return chunks

# Example usage
def generate_embeddings(text_chunks):
    client = OpenAI()
    embeddings = []
    print(text_chunks)
    for chunk in text_chunks:
        response = client.embeddings.create(
            input=chunk,
            # model="text-embedding-ada-002"
            model="text-embedding-3-small"
        ).data[0].embedding
        embeddings.append(response)
        # print(response)
    return embeddings

# TODO FIX THIS
# https://blog.gopenai.com/rag-with-pg-vector-with-sql-alchemy-d08d96bfa293
def insert_embeddings(embeddings):
    conn = psy.connect(database="postgres", user="postgres", password=os.getenv('DB_PSWD'), host="localhost", port=5432)
    cur = conn.cursor()
    for embedding in embeddings:
        sql = f"INSERT INTO conversations.conversation_vectors (vector_data) VALUES ('{embedding}')"
        cur.execute(sql)
    conn.commit()
    conn.close()

# N_DIM = 1536

# class TextEmbedding(Base):
#     __tablename__ = 'text_embeddings'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     content = Column(String)
#     embedding = Vector(N_DIM)


def store_conversation(user_input, ai_response):
    conn = psy.connect(database="postgres", user="postgres", password=os.getenv('DB_PSWD'), host="localhost", port=5432)
    cursor = conn.cursor()
    # Insert into the conversations table
    cursor.execute("INSERT INTO conversations.conversations (user_input, ai_response) VALUES (%s, %s) RETURNING id;",
                   (user_input, ai_response))
    conversation_id = cursor.fetchone()[0]
    conn.commit()

    print("Conversation stored in postgres db conversations table")
    print("Storing conversations into vector table")
    chunks = split_text(text=ai_response)
    print("Finished Splitting into chunks for embeddings")
    embeddings = generate_embeddings(text_chunks=chunks)
    print("Embeddings creation completed")
    print("Inserting embeddings into vector db")
    insert_embeddings(embeddings=embeddings)
    print("Embeddings insertion completed")
    
    # Example: Generating and storing a vector (optional and hypothetical)
    # Let's assume you have a function to convert texts to vectors: text_to_vector(text)
    # vector_data = text_to_vector(ai_response)
    # cursor.execute("INSERT INTO conversation_vectors (conversation_id, vector_data) VALUES (%s, %s);",
    #                (conversation_id, vector_data))
    # conn.commit()

    return conversation_id

# def find_similar_embeddings(query_embedding, limit=5):
#     k = 5
#     similarity_threshold = 0.7
#     query = session.query(TextEmbedding, TextEmbedding.embedding.cosine_distance(query_embedding)
#             .label("distance"))
#             .filter(TextEmbedding.embedding.cosine_distance(query_embedding) < similarity_threshold)
#             .order_by("distance")
#             .limit(k)
#             .all()