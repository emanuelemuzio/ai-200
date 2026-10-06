## Self-check questions

### 1. 

What is the key difference between Redis pub/sub and Redis Streams for event messaging?

A. Pub/sub delivers messages to active subscribers only, while Streams persist messages for consumer groups to process at their own pace
B. Pub/sub can handle more messages per second than Streams
C. Streams are only for string data while pub/sub works with any data type

> [!answer]- Reveal answer
>  A.

### 2. 

When building a processing pipeline with multiple services that need automatic retry on failure, which pattern should you use?

A. Redis Streams with consumer groups for reliable task coordination and built-in retry handling
B. Redis pub/sub for real-time distribution of work items
C. A simple Redis List with LPUSH and RPOP

> [!answer]- Reveal answer
> A.  

### 3. 

Which Redis command is used to add a new message to a Stream?

A. XADD
B. LPUSH
C. PUBLISH

> [!answer]- Reveal answer
> A.

### 4. 

Which scenario is best suited for Redis pub/sub messaging?

A. Broadcasting real-time status updates to multiple connected clients or services that are currently listening
B. Storing messages that arrive when subscribers are offline and delivering them when subscribers reconnect
C. Implementing a reliable work queue where tasks must be processed exactly once

> [!answer]- Reveal answer
> A. 

### 5.

How would you coordinate multiple AI workers processing documents from a Stream to ensure no document is processed by more than one worker simultaneously?

A. Use XREADGROUP to pull tasks from a consumer group, which automatically assigns unacknowledged tasks to different workers
B. Use XREAD to have each worker independently read from the Stream without coordination
C. Use pub/sub channels with one channel per worker

> [!answer]- Reveal answer
> A. 