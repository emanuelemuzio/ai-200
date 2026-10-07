## Self-check questions

### 1. 

You're building an AI content moderation application. You need to emit events when your inference service completes a classification. What type of Event Grid topic should you use to publish these events?

A. A custom topic
B. A system topic
C. An Event Hubs topic

> [!answer]- Reveal answer
>  A: A custom topic is used to publish application-defined events from your AI inference service.

### 2. 

You're designing custom events for an AI pipeline and want to enable subscribers to filter events based on which pipeline stage produced them. Which CloudEvents attribute is best suited for path-based filtering with prefix and suffix matches?

A. The `subject` attribute
B. The `type` attribute
C. The `source` attribute

> [!answer]- Reveal answer
> A: The `subject` attribute supports subject-based filtering, including prefix and suffix matching.  

### 3. 

Your AI handler endpoint occasionally experiences cold-start latency that exceeds 30 seconds. You want to ensure events are still delivered successfully after the handler warms up. What should you do?

A. Rely on Event Grid's automatic retry mechanism with exponential backoff
B. Configure a dead-letter destination to capture timed-out events
C. Set the event time-to-live to 30 seconds to match the timeout

> [!answer]- Reveal answer
> A: Event Grid's automatic retry mechanism with exponential backoff allows delivery attempts to continue while the handler warms up.

### 4. 

You need to route AI moderation events to different handlers based on whether the content was flagged for review. The flagged status is stored in the `data.status` field of the event payload. Which filtering approach should you use?

A. Advanced filtering with the `StringIn` operator on `data.status`
B. Event type filtering with `--included-event-types`
C. Subject filtering with `--subject-begins-with`

> [!answer]- Reveal answer
> A: Advanced filtering with the `StringIn` operator on `data.status` lets you route events based on the payload value.

### 5.

You're deploying an AI inference service to Azure Functions and need to publish events to an Event Grid custom topic. What authentication approach should you use for production workloads?

A. Microsoft Entra ID with a managed identity assigned to the function app
B. Access key authentication using the `aeg-sas-key` header
C. Store the access key in the function app's application settings

> [!answer]- Reveal answer
> A: Microsoft Entra ID with a managed identity assigned to the Function App is the recommended production approach because it avoids managing static access keys.

## [[Unit 7 - Summary|Next Unit > Summary]]
