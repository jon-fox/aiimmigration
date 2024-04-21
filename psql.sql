CREATE TABLE conversations.conversations (
    id SERIAL PRIMARY KEY,
    user_input TEXT,
    ai_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE conversations.conversation_vectors (
    id SERIAL PRIMARY KEY,
    -- content TEXT,
    vector_data VECTOR(1536)  -- Example vector size, adjust based on your actual use case
);

-- If using vectors
-- CREATE EXTENSION IF NOT EXISTS vector;
-- CREATE OR REPLACE TABLE conversation_vectors (
--     id INTEGER PRIMARY KEY AUTO INCREMENT,
--     -- content TEXT,
--     vector_data VECTOR(1536)  -- Example vector size, adjust based on your actual use case
-- );

-- text-embedding-ada-002 embedding model