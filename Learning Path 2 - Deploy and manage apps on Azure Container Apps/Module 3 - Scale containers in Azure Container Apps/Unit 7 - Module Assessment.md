## Self-check questions

### 1. 

A developer wants to configure a container app that processes messages from an Azure Service Bus queue and scales to zero replicas when no messages are present. Which scaling configuration meets this requirement?

A. Set `--min-replicas 0` with an HTTP scale rule
B. Set `--min-replicas 0` with a CPU scale rule
C. Set `--min-replicas 0` with an azure-servicebus scale rule

> [!answer]- Reveal answer
>  C: The azure-servicebus scale rule monitors queue depth and supports scale-to-zero. When no messages are in the queue, the application can scale to zero replicas. New messages trigger automatic scale-up.

### 2. 

A development team wants to ensure their container app has five replicas ready before the morning traffic spike at 8 AM, while still allowing scale-to-zero overnight. Which scaling approach meets this requirement?

A. Configure a cron scale rule combined with an HTTP scale rule
B. Set minimum replicas to five with an HTTP scale rule
C. Configure a CPU scale rule with a low utilization threshold

> [!answer]- Reveal answer
> A: Cron scaling activates during specified time windows and requests a fixed number of replicas. Combined with HTTP scaling, the cron rule establishes baseline capacity before expected peak hours while HTTP scaling handles variations. Outside the cron window, the app can scale to zero when no traffic arrives.

### 3. 

A team is deploying a new version of their container app and wants to send 10% of traffic to the new version for validation before full rollout. What must they configure?

A. Enable multiple revision mode and configure traffic splitting with revision weights
B. Use single revision mode with zero-downtime deployment
C. Configure a cron scale rule to schedule traffic shifts

> [!answer]- Reveal answer
> A: Multiple revision mode allows multiple revisions to be active simultaneously. Traffic splitting with revision weights distributes traffic by percentage, enabling canary deployments where a small percentage of traffic goes to the new version for validation.

### 4.  

When configuring KEDA scale rules for Azure services, which authentication method is recommended for production workloads?

A. Connection strings stored as container app secrets
B. Managed identity with `--scale-rule-identity`
C. Anonymous access without authentication

> [!answer]- Reveal answer
> B: Managed identity authentication eliminates the need to store connection strings as secrets. The scaler authenticates directly using the identity, reducing security risks, and simplifying credential management for production deployments.

## [[Learning Path 2 - Deploy and manage apps on Azure Container Apps/Module 3 - Scale containers in Azure Container Apps/Unit 8 - Summary|Next Unit > Summary]]