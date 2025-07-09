-- Database initialization script for FastAPI Enterprise Template
-- This script runs when the PostgreSQL container starts

-- Create the database if it doesn't exist
-- (PostgreSQL creates the database automatically based on POSTGRES_DB environment variable)

-- Grant necessary permissions
GRANT ALL PRIVILEGES ON DATABASE fastapi_enterprise TO postgres;

-- Create extensions if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Set timezone
SET timezone = 'UTC';

-- Log initialization
DO $$
BEGIN
    RAISE NOTICE 'Database fastapi_enterprise initialized successfully';
END $$;
