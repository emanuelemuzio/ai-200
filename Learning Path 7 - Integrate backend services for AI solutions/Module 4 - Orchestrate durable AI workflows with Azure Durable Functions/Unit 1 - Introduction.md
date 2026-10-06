AI applications require reliable coordination when they combine model calls, data processing, and human decisions. This module guides you through using Azure Durable Functions to preserve workflow progress, run independent tasks in parallel, and resume long-running AI workflows after delays or failures.

Imagine you're a developer building an AI document-processing application for an insurance company. The application receives batches of claim documents in Azure Blob Storage. Each document requires text extraction, classification, and an AI-generated summary. Independent documents should run in parallel so one large claim doesn't block the rest of the batch. Model calls and storage operations can fail because of throttling, transient service errors, or malformed input. Claims with low confidence scores require an adjuster to approve or reject the generated summary. An adjuster might respond hours later, so the application can't keep a function invocation active while it waits. The client expects the workflow to resume after failures without repeating completed work or creating duplicate records. The client also expects rejected or failed claims to follow a defined compensation path. Durable Functions provides persistent orchestration, parallel activity execution, durable waits, and explicit failure-handling policies for this workflow.

After completing this module, you'll be able to:

- Explain how Durable Functions coordinates reliable, long-running AI workflows.
- Separate deterministic orchestration logic from activity functions that call AI models and external services.
- Implement fan-out/fan-in processing for independent documents or media items.
- Build human approval flows with external events and durable timers.
- Apply retries, timeouts, idempotency, and compensation to failed workflow steps.