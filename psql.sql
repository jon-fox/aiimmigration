CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    user_input TEXT,
    ai_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- If using vectors
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE conversation_vectors (
    conversation_id INTEGER REFERENCES conversations(id),
    vector_data VECTOR(512)  -- Example vector size, adjust based on your actual use case
);