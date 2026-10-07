## Self-check questions

### 1. 

Your AI platform completes a document analysis, and three independent services need to react to the result: a notification service alerts the user, an audit service logs the result for compliance, and a dashboard service updates metrics. Which Service Bus entity type supports this requirement?

A. A topic with three subscriptions
B. A queue with three competing consumers
C. Three separate queues with the sender publishing to each one

> [!answer]- Reveal answer
>  A: A topic with three subscriptions allows each independent service to receive its own copy of every message.

### 2. 

You're building an AI inference pipeline where losing a customer's request is unacceptable. If a worker crashes while processing a message, the message must become available to another worker. Which receive mode should you configure?

A. Peek-lock mode
B. Receive-and-delete mode
C. Deferred receive mode

> [!answer]- Reveal answer
> A: Peek-lock keeps the message locked while processing; if the worker fails without completing it, the message becomes available for another worker. 

### 3. 

A message in your inference queue consistently causes a processing error every time a worker attempts it. After 10 delivery attempts, what does Service Bus do with the message?

A. Moves the message to the dead-letter queue with the reason MaxDeliveryCountExceeded
B. Deletes the message permanently from the queue
C. Returns the message to the back of the queue for continued retry attempts

> [!answer]- Reveal answer
> A: After exceeding `MaxDeliveryCount`, Service Bus moves the message to the dead-letter queue with the reason `MaxDeliveryCountExceeded`.

### 4. 

Your AI pipeline needs to process 500-MB document files, but Azure Service Bus Premium tier supports messages up to 100 MB via AMQP. Which pattern addresses this constraint?

A. The claim-check pattern, uploading files to Azure Blob Storage and sending only the blob URI in the message
B. Splitting the document into five 100-MB messages and reassembling them at the consumer
C. Encoding the document as base64 and sending it as the message body on the Premium tier

> [!answer]- Reveal answer
> A: The claim-check pattern stores the large document in Azure Blob Storage and sends only its URI through Service Bus.

### 5.

You set the correlation_id property on every Service Bus message in your AI pipeline. What is the primary purpose of this property?

A. Tracking a request end-to-end across all pipeline stages, from the API through processing to result delivery
B. Enabling duplicate detection so Service Bus discards repeated submissions of the same request
C. Routing messages to specific subscriptions based on filter rules

> [!answer]- Reveal answer
> A: `correlation_id` is primarily used to trace a request end-to-end across different stages and services in the pipeline.

## [[Unit 7 - Summary|Next Unit > Summary]]
