## Self-check questions

### 1. 

Which pgvector distance operator should you use when your embeddings are normalized to unit length and you want to measure semantic similarity?

A. `<=>` (cosine distance)
B. `<->` (L2 distance)
C. `<#>` (negative inner product)

> [!answer]- Reveal answer
>  A: `<=>` is the cosine distance operator, which is appropriate for normalized unit-length embeddings when measuring semantic similarity.

### 2. 

You're building a RAG pipeline that needs to retrieve relevant document chunks quickly from a collection of 5 million embeddings. The collection receives occasional batch updates but no real-time inserts. Which index type should you choose?

A. IVFFlat with an appropriate number of lists
B. HNSW with high ef_construction value
C. No index, relying on exact sequential scan

> [!answer]- Reveal answer
> A: IVFFlat is well suited for large datasets with occasional batch updates, providing fast approximate searches with a configurable accuracy/performance trade-off.

### 3. 

When creating an HNSW index, what does the `m` parameter control?

A. The maximum number of connections per node in the graph
B. The number of candidate neighbors considered during index construction
C. The number of lists to partition vectors into

> [!answer]- Reveal answer
> A: The `m` parameter controls the maximum number of connections each node can have in the HNSW graph.

### 4. 

You need to update embeddings for 50,000 product descriptions after switching to a new embedding model. What approach minimizes the impact on concurrent searches?

A. Batch the updates into transactions of 1,000-5,000 rows each
B. Update all 50,000 rows in a single transaction
C. Drop the existing vector index before updating

> [!answer]- Reveal answer
> A: Batching updates into smaller transactions reduces lock duration and resource contention, minimizing the impact on concurrent searches.

### 5.  

In a hybrid search combining vector similarity with full-text search, what technique helps balance the relevance scores from both search methods?

A. Using Reciprocal Rank Fusion (RRF) to combine rankings
B. Multiplying the vector distance by the text relevance score
C. Always returning vector search results first

> [!answer]- Reveal answer
> A: Reciprocal Rank Fusion (RRF) combines the rankings from vector and full-text search, balancing their contributions without requiring directly comparable score scales.

## [[Unit 8 - Summary|Next Unit > Summary]]
