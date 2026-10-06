## Self-check questions

### 1. 

You're tuning PostgreSQL for a vector search workload with 2 million 1536-dimensional embeddings. Queries are slow and you observe a cache hit ratio of 85%. Which configuration change should you prioritize?

A. Increase `shared_buffers` to keep more data in the PostgreSQL cache
B. Decrease `random_page_cost` to encourage more index scans
C. Increase `ivfflat.probes` to search more index partitions

> [!answer]- Reveal answer
>  A.

### 2. 

You need to create a vector index for a dataset of 5 million product embeddings that receives frequent batch updates (daily full refresh). Build time must be under 30 minutes. Which index configuration should you choose?

A. IVFFlat with lists set to sqrt(rows)
B. HNSW with m=16 and ef_construction=64
C. HNSW with m=8 and ef_construction=32

> [!answer]- Reveal answer
> A.  

### 3. 

Your filtered vector search query filters by `category_id` and then orders by vector similarity. The query plan shows a sequential scan on the products table. What should you check first?

A. Verify that a B-tree index exists on the `category_id` column
B. Verify that the vector index uses the same operator class as the query
C. Increase `hnsw.ef_search` to expand the search space

> [!answer]- Reveal answer
> A.

### 4. 

You're implementing connection management for an AI application that makes 500 vector queries per second during peak traffic. Your Azure Database for PostgreSQL instance supports 1,719 max connections. Which approach should you use?

A. Enable PgBouncer in transaction mode with a pool size appropriate for your application instances
B. Create a new database connection for each query request
C. Enable PgBouncer in session mode to maintain persistent connections

> [!answer]- Reveal answer
> A.

### 5.  

You're scaling a recommendation engine that currently runs on a General Purpose 8 vCore instance. CPU utilization averages 75% and P95 query latency is 150 ms, but you need to achieve sub-50ms latency. What scaling approach should you try first?

A. Upgrade to a Memory Optimized tier with more vCores
B. Add read replicas to distribute query load
C. Implement application-level caching with Azure Cache for Redis

> [!answer]- Reveal answer
> A.   