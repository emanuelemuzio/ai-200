## Self-check questions

### 1. 

 You receive reports that an AI inference API on Azure Kubernetes Service occasionally returns HTTP 500 errors and higher latency. You want to inspect recent error messages for a specific pod while reproducing the issue. Which approach is most appropriate?

A. Use `kubectl logs -f <pod-name> -n <namespace>` while you send test requests to the API.
B. Open Azure Monitor and review only node CPU metrics for the last week.
C. Run `kubectl describe node` on all nodes to look for scheduling events.

> [!answer]- Reveal answer
>  C.

### 2. 

A pod that runs a model-serving container is stuck in CrashLoopBackOff. You want to understand why the container exits. What should you do first?

A. Run `kubectl describe pod <pod-name> -n <namespace>` and inspect events and container status.
B. Immediately delete the pod so Kubernetes recreates it.
C. Scale the Deployment to zero replicas and then scale it back up.

> [!answer]- Reveal answer
> A.  

### 3. 

A Service that fronts your AI API shows no endpoints, even though the pods appear healthy and ready. Which command helps you confirm whether the Service selectors match pod labels?

A. kubectl describe service <service-name> -n <namespace>
B. kubectl top nodes
C. kubectl logs <pod-name> -n <namespace>

> [!answer]- Reveal answer
> A.

### 4. 

You need to debug a new AI endpoint inside the cluster before exposing it externally. You want to send HTTP requests from your development machine directly to the Service. Which command should you use?

A. kubectl port-forward service/<service-name> 8080:80 -n <namespace>
B. kubectl get endpoints <service-name> -n <namespace>
C. `kubectl describe node` on the node that hosts the pod

> [!answer]- Reveal answer
> A.

### 5.  

Metrics for a model-serving pod show sustained CPU usage at its configured limit, and users report increased latency. What is the most appropriate next step?

A. Adjust CPU requests and limits or scale out replicas so the pod has enough capacity.
B. Ignore the metrics because the pod is still running.
C. Delete the Service and recreate it with the same configuration.

> [!answer]- Reveal answer
> A.  

## [[Learning Path 3 - Deploy and monitor applications on Azure Kubernetes Service/Module 3 - Monitor and troubleshoot applications on Azure Kubernetes Service/Unit 6 - Summary| Next Unit > Summary]]