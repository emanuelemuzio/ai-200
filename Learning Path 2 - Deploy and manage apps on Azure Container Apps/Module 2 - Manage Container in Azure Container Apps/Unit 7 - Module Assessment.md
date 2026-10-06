## Self-check questions

### 1. 

You deploy a new image to a production container app. Which approach provides the best traceability and reduces the risk of deploying the wrong artifact?

A. Reference the image by digest (for example, `myregistry.azurecr.io/app@sha256:<digest>`) when you update the container app.
B. Reference the image by the `latest` tag to ensure the platform always pulls the most recent build.
C. Rebuild the image locally on each environment to ensure the image matches the environment.

> [!answer]- Reveal answer
>  A.

### 2. 

A new revision starts but shouldn't receive traffic while you investigate. Which action removes the revision from traffic without deleting it?

A. Run `az containerapp revision deactivate` for the revision.
B. Run `az containerapp revision delete` for the revision.
C. Run `az containerapp stop` for the container app.

> [!answer]- Reveal answer
> A.  

### 3. 

A revision fails readiness checks immediately after deployment. Which issue is the most common root cause you should validate first?

A. The readiness probe targets the wrong port or path for the container’s HTTP server.
B. The container image is too small to include all required libraries.
C. The container app environment can't route traffic to the public internet.

> [!answer]- Reveal answer
> A.

### 4. 

You suspect only one revision has a runtime exception after an update. What is the most effective first step to confirm the problem?

A. Stream the container app logs and filter by revision while reproducing the request.
B. Delete older revisions to reduce noise in troubleshooting output.
C. Increase CPU and memory allocations before investigating.

> [!answer]- Reveal answer
> A.

### 5.  

Your AI API experiences high latency and log messages indicate CPU throttling during peak traffic. Which change most directly addresses the throttling?

A. Increase the per-replica CPU allocation, and then reassess scaling rules based on throughput.
B. Deactivate the newest revision to reduce load on the system.
C. Switch the image reference from digest to tag.

> [!answer]- Reveal answer
> A.  

## [[Learning Path 2 - Deploy and manage apps on Azure Container Apps/Module 2 - Manage Container in Azure Container Apps/Unit 8 - Summary| Next Unit > Summary]]