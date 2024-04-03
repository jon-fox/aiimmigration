import psycopg2 as psy
from psycopg2.extras import execute_values
import os


def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        if end > len(text):
            end = len(text)
        chunks.append(text[start:end])
        start = end - overlap  # Overlap chunks

    return chunks

# Example usage
def generate_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        response = openai.Embedding.create(
            input=chunk,
            model="text-embedding-ada-002"
        )
        embeddings.append(response['data'][0]['embedding'])
    return embeddings

# TODO FIX THIS
# https://blog.gopenai.com/rag-with-pg-vector-with-sql-alchemy-d08d96bfa293
def insert_embeddings(embeddings):
    for embedding in embeddings:
        new_embedding = TextEmbedding(embedding=embedding)
        session.add(new_embedding)
    session.commit()

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
    cursor.execute("INSERT INTO conversations (user_input, ai_response) VALUES (%s, %s) RETURNING id;",
                   (user_input, ai_response))
    conversation_id = cursor.fetchone()[0]
    conn.commit()
    
    # Example: Generating and storing a vector (optional and hypothetical)
    # Let's assume you have a function to convert texts to vectors: text_to_vector(text)
    # vector_data = text_to_vector(ai_response)
    # cursor.execute("INSERT INTO conversation_vectors (conversation_id, vector_data) VALUES (%s, %s);",
    #                (conversation_id, vector_data))
    # conn.commit()

    return conversation_id