## Self-check questions

### 1. 

Your AI application needs to store conversation metadata with varying structures. Some conversations include custom fields like model configuration, while others have user preferences. Which PostgreSQL data type best supports this requirement?

A. TEXT
B. JSONB
C. VARCHAR(MAX)

> [!answer]- Reveal answer
>  B.

### 2. 

You insert a new conversation record and need the auto-generated ID immediately to insert related messages. Which PostgreSQL clause retrieves the generated value without a separate query?

A. RETURNING
B. OUTPUT
C. SELECT LAST_INSERT_ID()

> [!answer]- Reveal answer
> A.  

### 3. 

You need to insert a user preference record. If the record already exists, you want to update the value without creating a duplicate. Which PostgreSQL clause handles this scenario?

A. INSERT INTO table ON DUPLICATE KEY UPDATE
B. INSERT INTO table ON CONFLICT DO UPDATE
C. INSERT INTO table IF NOT EXISTS

> [!answer]- Reveal answer
> B.

### 4. 

Your Python application creates many short-lived database connections to store individual messages during AI inference. What approach should you use to improve performance?

A. Open a new connection for each message and close it immediately after
B. Use a ConnectionPool to maintain reusable connections that the application can borrow and return
C. Keep a single global connection open for the entire application lifetime

> [!answer]- Reveal answer
> B.

### 5.  

You're designing a table for AI agent task checkpoints. Tasks have a status that should only be 'pending', 'in_progress', 'completed', or 'failed'. Which constraint enforces this rule at the database level?

A. UNIQUE (status)
B. CHECK (status IN ('pending', 'in_progress', 'completed', 'failed'))
C. NOT NULL DEFAULT 'pending'

> [!answer]- Reveal answer
> B.  

## [[Learning Path 5 - Develop AI solutions with Azure Database for PostgreSQL/Module 1 - Build and query with Azure Database for PostgreSQL/Unit 8 - Summary|Next Unit > Summary]]