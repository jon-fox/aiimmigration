CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    user_input TEXT,
    ai_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- If using vectors
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE conversation_vectors (
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    content TEXT,
    vector_data VECTOR(1536)  -- Example vector size, adjust based on your actual use case
);

-- text-embedding-ada-002 embedding model