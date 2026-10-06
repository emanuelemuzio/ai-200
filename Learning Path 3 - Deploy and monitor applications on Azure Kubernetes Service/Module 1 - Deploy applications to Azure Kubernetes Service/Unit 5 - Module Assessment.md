## Self-check questions

### 1. 

Which Service type should you use when you need to expose an application to the internet with an Azure-managed load balancer?

A. LoadBalancer
B. ClusterIP
C. NodePort

> [!answer]- Reveal answer
>  A.

### 2. 

What happens if a Pod's resource requests exceed the available capacity on all cluster nodes?

A. The Pod stays in Pending status until sufficient resources become available
B. Kubernetes automatically scales the cluster to add more nodes
C. The Pod starts but with reduced resource allocation

> [!answer]- Reveal answer
> A.  

### 3. 

What must match between a Deployment and a Service for traffic to route correctly?

A. The Pod labels in the Deployment template must match the Service selector
B. The container port in the Deployment must match the Service port
C. The Deployment name must match the Service name

> [!answer]- Reveal answer
> A.

### 4. 

Which kubectl command should you use to view logs from a Pod that crashed and restarted?

A. kubectl logs <pod-name> --previous
B. kubectl logs <pod-name>
C. kubectl describe pod <pod-name>

> [!answer]- Reveal answer
> A.

### 5.  

What does the `replicas` field in a Deployment manifest control?

A. The number of Pod copies that should run simultaneously
B. The number of containers in each Pod
C. The number of Services that can connect to the Deployment

> [!answer]- Reveal answer
> A.  

## [[Learning Path 3 - Deploy and monitor applications on Azure Kubernetes Service/Module 1 - Deploy applications to Azure Kubernetes Service/Unit 6 - Summary| Next Unit > Summary]]