## Self-check questions

### 1. 

 You receive reports that an AI inference API on Azure Kubernetes Service occasionally returns HTTP 500 errors and higher latency. You want to inspect recent error messages for a specific pod while reproducing the issue. Which approach is most appropriate?

A. Use `kubectl logs -f <pod-name> -n <namespace>` while you send test requests to the API.
B. Open Azure Monitor and review only node CPU metrics for the last week.
C. Run `kubectl describe node` on all nodes to look for scheduling events.

> [!answer]- Reveal answer
>  A: Streaming logs from the specific pod while you reproduce the issue lets you see real-time error messages and stack traces that explain the HTTP 500 errors and latency.

### 2. 

A pod that runs a model-serving container is stuck in CrashLoopBackOff. You want to understand why the container exits. What should you do first?

A. Run `kubectl describe pod <pod-name> -n <namespace>` and inspect events and container status.
B. Immediately delete the pod so Kubernetes recreates it.
C. Scale the Deployment to zero replicas and then scale it back up.

> [!answer]- Reveal answer
> A: `kubectl describe pod` shows recent events and container status, which usually reveal the exit reason, failed probes, or configuration problems causing CrashLoopBackOff.

### 3. 

A Service that fronts your AI API shows no endpoints, even though the pods appear healthy and ready. Which command helps you confirm whether the Service selectors match pod labels?

A. kubectl describe service <service-name> -n <namespace>
B. kubectl top nodes
C. kubectl logs <pod-name> -n <namespace>

> [!answer]- Reveal answer
> A: `kubectl describe service` shows the selector labels and current endpoints, so you can verify whether the Service matches the pods.

### 4. 

You need to debug a new AI endpoint inside the cluster before exposing it externally. You want to send HTTP requests from your development machine directly to the Service. Which command should you use?

A. kubectl port-forward service/<service-name> 8080:80 -n <namespace>
B. kubectl get endpoints <service-name> -n <namespace>
C. `kubectl describe node` on the node that hosts the pod

> [!answer]- Reveal answer
> A: `kubectl port-forward` from your workstation to the Service lets you send HTTP requests directly to the endpoint inside the cluster.

### 5.  

Metrics for a model-serving pod show sustained CPU usage at its configured limit, and users report increased latency. What is the most appropriate next step?

A. Adjust CPU requests and limits or scale out replicas so the pod has enough capacity.
B. Ignore the metrics because the pod is still running.
C. Delete the Service and recreate it with the same configuration.

> [!answer]- Reveal answer
> A: When a pod consistently hits its CPU limit and latency increases, you typically need to raise CPU resources or add replicas so the workload has more capacity.

## [[Learning Path 3 - Deploy and monitor applications on Azure Kubernetes Service/Module 3 - Monitor and troubleshoot applications on Azure Kubernetes Service/Unit 6 - Summary| Next Unit > Summary]]