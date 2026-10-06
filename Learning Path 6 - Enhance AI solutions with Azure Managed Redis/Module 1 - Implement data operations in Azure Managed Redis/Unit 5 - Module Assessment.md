## Self-check questions

### 1. 

What is the default TLS connection port for Azure Managed Redis?

A. 10000
B. 6379
C. 6380

> [!answer]- Reveal answer
>  A: Azure Managed Redis uses port 10000 as the default connection port for TLS connections.

### 2. 

Which Redis command should you avoid using in production environments for iterating over keys?

A. KEYS
B. SCAN
C. EXISTS

> [!answer]- Reveal answer
> A: The KEYS command should be avoided in production because it blocks the server while scanning all keys. Use SCAN instead for non-blocking iteration.

### 3. 

Which redis-py method sets a key with an expiration time in a single atomic operation?

A. setex()
B. expire()
C. set()

> [!answer]- Reveal answer
> A: The `setex()` method sets a value and expiration time in a single atomic operation, making it efficient and reliable.

### 4. 

What does a TTL value of -1 indicate when checking key expiration in Redis?

A. Key exists but has no expiration set
B. Key doesn't exist
C. Key expired 1 second ago

> [!answer]- Reveal answer
> A: A TTL value of -1 means the key exists in Redis but has no expiration time set, so it persists indefinitely.