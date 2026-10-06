## Self-check questions

### 1. 

A developer needs to optimize a query that filters documents by documentType and sorts results by uploadDate in descending order. Which index configuration best supports this query pattern?

A. Create a composite index with documentType (ascending) followed by uploadDate (descending)
B. Create separate range indexes on documentType and uploadDate
C. Create a composite index with uploadDate (descending) followed by documentType (ascending)

> [!answer]- Reveal answer
>  A.

### 2. 

An AI application stores 500,000 embeddings per partition and needs to perform fast similarity searches with acceptable accuracy trade-offs. Which vector index type is most appropriate?

A. flat
B. diskANN
C. quantizedFlat

> [!answer]- Reveal answer
> B.  

### 3. 

A team discovers that embedding arrays are consuming significant storage space. The embeddings are used only for vector similarity searches. How should they modify the indexing policy to reduce storage costs?

A. Set indexingMode to none to disable all indexing on the container
B. Change the embedding data type from float32 to float16 in the range index
C. Exclude the embedding path from includedPaths and add a vector index for the embedding property

> [!answer]- Reveal answer
> C.

### 4. 

A document search application queries by category and date range, but users report that recently uploaded documents don't appear in search results. The account uses eventual consistency by default. What change would ensure users see their own uploads immediately?

A. Change the default consistency to strong consistency for all operations
B. Use session consistency and pass session tokens from write operations to subsequent reads
C. Increase the container's provisioned throughput to speed up replication

> [!answer]- Reveal answer
> B.

### 5.  

Query metrics show that a frequently executed query has low index utilization and high retrieved-to-output document ratios. What does this indicate and how should the developer respond?

A. The query is performing scans instead of using indexes efficiently. Analyze the query to identify which properties need indexes and add appropriate range or composite indexes.
B. The container has too many indexes. Remove indexes to reduce query overhead and improve index utilization metrics.
C. The query is returning too many results. Add a TOP clause to limit results and improve the retrieved-to-output ratio.

> [!answer]- Reveal answer
> A.  

## [[Learning Path 4 - Develop AI solutions with Azure Cosmos DB for NoSQL/Module 3 - Optimize query performance for Azure Cosmos DB for NoSQL/Unit 8 - Summary|Next Unit > Summary]]