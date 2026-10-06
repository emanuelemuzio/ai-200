## Self-check questions

### 1. 

An orchestrator directly calls a model endpoint and branches on the response. The orchestration later fails during replay because the model returns a different result. How should you redesign the workflow?

A. Move the model call to an activity function and branch on the recorded activity result in the orchestrator
B. Keep the model call in the orchestrator and replace the endpoint with a synchronous deployment
C. Keep the model call in the orchestrator and use context.current_utc_datetime before each request
> [!answer]- Reveal answer
>  A.

### 2. 

A workflow processes thousands of independent documents, but the model deployment has limited request capacity. Which fan-out/fan-in design best protects the dependency while preserving parallel processing?

A. Yield each activity immediately so the orchestrator processes every document sequentially
B. Divide the documents into bounded batches and use context.task_all() for each batch before scheduling the next one
C. Schedule every activity at once and rely on the orchestration history to enforce the model rate limit

> [!answer]- Reveal answer
> B.  

### 3. 

A document workflow must wait up to 24 hours for an adjuster's decision without holding compute resources. Which orchestration pattern should you use?

A. Call time.sleep() in the orchestrator and check the approval database after the delay
B. Call an approval activity with a 24-hour client request timeout
C. Race wait_for_external_event() against a durable timer with context.task_any() and cancel the pending timer when the event wins

> [!answer]- Reveal answer
> C.

### 4. 

An activity writes a result blob, but the host restarts before Durable Functions records the activity completion. The activity runs again. Which design prevents a duplicate result?

A. Use a stable operation ID as the blob name, create the blob without overwrite, and return the existing result when the blob already exists
B. Generate a new UUID inside the activity for each write so every retry has a unique blob name
C. Enable orchestrator replay logging so Durable Functions suppresses the second blob write

> [!answer]- Reveal answer
> A. 

### 5.

A document activity exhausts its bounded retries after a transient dependency failure, and an earlier step already created provisional external state. How should the orchestration handle the failure?

A. Return a Completed status after logging the error so the batch can continue
B. Schedule an idempotent compensation activity for completed side effects, then rethrow the original failure
C. Retry the entire orchestration instance without recording which forward operations completed

> [!answer]- Reveal answer
> B. 