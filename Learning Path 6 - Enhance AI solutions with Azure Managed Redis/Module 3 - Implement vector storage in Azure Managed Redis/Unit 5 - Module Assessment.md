## Self-check questions

### 1. 

Which distance metric should you use for text embeddings?

A. COSINE
B. L2 (Euclidean)
C. IP (Inner Product)

> [!answer]- Reveal answer
>  A.

### 2. 

When should you choose HNSW indexing over FLAT indexing for vector search?

A. When you have large datasets (over 10,000 vectors) and need fast queries with acceptable 95-99% accuracy
B. When you need perfect 100% accuracy for all queries
C. When you have fewer than 1,000 vectors to index

> [!answer]- Reveal answer
> A.  

### 3. 

Which data type should you use for vector storage in most AI applications?

A. FLOAT32
B. FLOAT64
C. INT32

> [!answer]- Reveal answer
> A.

### 4. 

When should you use Redis Hash instead of JSON for storing vectors?

A. When you have flat data models and need maximum memory efficiency and query performance
B. When your data has nested structures or multiple vectors per document
C. When you need JSON query capabilities

> [!answer]- Reveal answer
> A. 

### 5.

What does the EF_RUNTIME parameter control in HNSW queries?

A. The tradeoff between query speed and accuracy by controlling how many graph nodes are examined
B. The maximum number of results returned by the query
C. The distance metric used for similarity calculations

> [!answer]- Reveal answer
> A. 