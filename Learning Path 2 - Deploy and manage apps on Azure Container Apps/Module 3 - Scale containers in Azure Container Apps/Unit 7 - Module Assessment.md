## Self-check questions

### 1. 

A developer wants to configure a container app that processes messages from an Azure Service Bus queue and scales to zero replicas when no messages are present. Which scaling configuration meets this requirement?

A. Set `--min-replicas 0` with an HTTP scale rule
B. Set `--min-replicas 0` with a CPU scale rule
C. Set `--min-replicas 0` with an azure-servicebus scale rule

> [!answer]- Reveal answer
>  C.

### 2. 

A development team wants to ensure their container app has five replicas ready before the morning traffic spike at 8 AM, while still allowing scale-to-zero overnight. Which scaling approach meets this requirement?

A. Configure a cron scale rule combined with an HTTP scale rule
B. Set minimum replicas to five with an HTTP scale rule
C. Configure a CPU scale rule with a low utilization threshold

> [!answer]- Reveal answer
> A.  

### 3. 

A team is deploying a new version of their container app and wants to send 10% of traffic to the new version for validation before full rollout. What must they configure?

A. The readiness probe targets the wrong port or path for the container’s HTTP server.
B. The container image is too small to include all required libraries.
C. The container app environment can't route traffic to the public internet.

> [!answer]- Reveal answer
> A.

### 4. 

You suspect only one revision has a runtime exception after an update. What is the most effective first step to confirm the problem?

A. Enable multiple revision mode and configure traffic splitting with revision weights
B. Use single revision mode with zero-downtime deployment
C. Configure a cron scale rule to schedule traffic shifts

> [!answer]- Reveal answer
> A.

### 5.  

When configuring KEDA scale rules for Azure services, which authentication method is recommended for production workloads?

A. Connection strings stored as container app secrets
B. Managed identity with `--scale-rule-identity`
C. Anonymous access without authentication

> [!answer]- Reveal answer
> B.  

## [[Learning Path 2 - Deploy and manage apps on Azure Container Apps/Module 3 - Scale containers in Azure Container Apps/Unit 8 - Summary|Next Unit > Summary]]