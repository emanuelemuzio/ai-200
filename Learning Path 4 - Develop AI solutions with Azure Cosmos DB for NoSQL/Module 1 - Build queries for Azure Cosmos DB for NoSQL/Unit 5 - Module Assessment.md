## Self-check questions

### 1. 

A developer is designing a container for an AI application that stores user interaction logs. Each document includes a userId property. The application frequently retrieves all logs for a specific user. Which partition key selection provides the best performance for this access pattern?

A. Use userId as the partition key
B. Use a timestamp property as the partition key
C. Use a boolean isProcessed property as the partition key

> [!answer]- Reveal answer
>  A: Using `userId` as the partition key colocates each user’s logs in the same logical partition, making queries for a specific user efficient.

### 2. 

An AI application caches model inference results in Azure Cosmos DB. The application periodically recomputes results and needs to store them regardless of whether a cached entry already exists. Which SDK method handles this requirement most effectively?

A. Use create_item() to insert the item
B. Use replace_item() to update the item
C. Use upsert_item() to insert or replace the item

> [!answer]- Reveal answer
> C: `upsert_item()` inserts the item if it does not exist and replaces it if it already exists.

### 3. 

An AI application stores product recommendations with document IDs in the format product-{id}. The application needs to retrieve a specific recommendation by its known ID and category. Which method provides the most efficient retrieval?

A. Use query_items() with a WHERE clause filtering by ID
B. Use read_item() with the item ID and partition key
C. Use query_items() with enable_cross_partition_query=True

> [!answer]- Reveal answer
> B: `read_item()` with the known item ID and partition key is the most efficient way to retrieve a specific item directly.

### 4. 

A developer is building a search feature that accepts user-provided filter values. The feature filters products by category and maximum price. What is the primary reason to use parameterized queries instead of string concatenation?

A. Parameterized queries prevent injection attacks and enable query plan caching
B. Parameterized queries automatically convert data types
C. Parameterized queries run faster than queries with literal values

> [!answer]- Reveal answer
> A: Parameterized queries prevent injection attacks and allow Cosmos DB to reuse query plans efficiently.

### 5.  

A data analyst notices that queries filtering products by price range consume more RUs than expected. The container uses categoryId as the partition key. Which optimization would most effectively reduce RU consumption?

A. Remove the ORDER BY clause from the query
B. Increase the container's provisioned throughput
C. Add the partition key (categoryId) to the WHERE clause to enable single-partition routing

> [!answer]- Reveal answer
> C: Including `categoryId` in the `WHERE` clause allows Cosmos DB to route the query to a single partition, significantly reducing RU consumption. 

## [[Learning Path 4 - Develop AI solutions with Azure Cosmos DB for NoSQL/Module 1 - Build queries for Azure Cosmos DB for NoSQL/Unit 6 - Summary|Next Unit > Summary]]