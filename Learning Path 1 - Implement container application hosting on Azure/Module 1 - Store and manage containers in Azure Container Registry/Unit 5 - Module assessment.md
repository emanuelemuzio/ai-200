## Self-check questions

### 1. 

Your team builds container images on developer workstations, leading to inconsistent results. You need to ensure all images are built in a controlled environment. Which Azure Container Registry feature addresses this requirement?

A. ACR Tasks quick build  
B. Geo-replication  
C. Repository namespaces

> [!answer]- Reveal answer
> A: ACR Tasks quick build offloads image building to Azure, providing a consistent cloud environment that eliminates 'works on my machine' problems. Quick tasks use the az acr build command to build images in a controlled Azure environment.

### 2.  

You need to deploy a container image to production and ensure every node in your Kubernetes cluster runs the exact same image version, even if someone pushes a new image with the same tag. How should you reference the image?

A. By manifest digest  
B. By the latest tag  
C. By semantic version tag

> [!answer]- Reveal answer
> A: Manifest digests are immutable SHA-256 hashes that uniquely identify an image regardless of tags. Pulling by digest guarantees you get the exact image, even if someone pushes a new image with the same tag.

### 3. 

Your AI application depends on a base image containing PyTorch. When the PyTorch team releases security patches to the base image, you want your application image to rebuild automatically. Which ACR Tasks trigger type provides this capability?

A. Base image update trigger  
B. Source code commit trigger  
C. Scheduled trigger

> [!answer]- Reveal answer
> A: Base image update triggers detect changes to parent images and automatically rebuild dependent images. This capability keeps your application images current with security patches in base images.

### 4.  

You are implementing a tagging strategy for production deployments. Your requirements include traceability to the source code commit and the ability to roll back to any previous version. Which tagging pattern best meets these requirements?

A. Unique tags with Git commit SHA  
B. Stable tags like v1 and v2  
C. Using only the latest tag

> [!answer]- Reveal answer
> A: Unique tags with Git commit SHA provide direct traceability to source code and guarantee each build is distinct for rollback. The immutable nature of unique tags ensures you can reference any specific build.

### 5.  

You deployed a critical AI inference API to production and need to prevent the container image from being accidentally deleted. Which ACR feature should you use?

A. Image locking with write-enabled false  
B. Repository namespaces  
C. Geo-replication

> [!answer]- Reveal answer
> A: Setting write-enabled to false locks the image to prevent deletion or modification. Locked images remain available even when retention policies run, ensuring production deployments are protected.

## [[Learning Path 1 - Implement container application hosting on Azure/Module 1 - Store and manage containers in Azure Container Registry/Unit 6 - Summary| Unit 6 - Next Unit >Summary]]