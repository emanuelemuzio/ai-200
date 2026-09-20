---
title: "Module assessment"
aliases:
  - ACR module assessment
  - Azure Container Registry assessment
tags:
  - ai-200
  - assessment
  - acr
  - docker
---

## Self-check questions

### 1. Controlled image builds

Your team builds container images on developer workstations, leading to inconsistent results. You need to ensure all images are built in a controlled environment. Which Azure Container Registry feature addresses this requirement?

A. ACR Tasks quick build  
B. Geo-replication  
C. Repository namespaces

> [!answer]- Reveal answer
> A. ACR Tasks quick build

### 2. Exact image version in production

You need to deploy a container image to production and ensure every node in your Kubernetes cluster runs the exact same image version, even if someone pushes a new image with the same tag. How should you reference the image?

A. By manifest digest  
B. By the latest tag  
C. By semantic version tag

> [!answer]- Reveal answer
> A. By manifest digest

### 3. Automatic rebuild when base image updates

Your AI application depends on a base image containing PyTorch. When the PyTorch team releases security patches to the base image, you want your application image to rebuild automatically. Which ACR Tasks trigger type provides this capability?

A. Base image update trigger  
B. Source code commit trigger  
C. Scheduled trigger

> [!answer]- Reveal answer
> A. Base image update trigger

### 4. Traceable and rollback-friendly production tags

You are implementing a tagging strategy for production deployments. Your requirements include traceability to the source code commit and the ability to roll back to any previous version. Which tagging pattern best meets these requirements?

A. Unique tags with Git commit SHA  
B. Stable tags like v1 and v2  
C. Using only the latest tag

> [!answer]- Reveal answer
> A. Unique tags with Git commit SHA

### 5. Prevent accidental deletion of a critical image

You deployed a critical AI inference API to production and need to prevent the container image from being accidentally deleted. Which ACR feature should you use?

A. Image locking with write-enabled false  
B. Repository namespaces  
C. Geo-replication

> [!answer]- Reveal answer
> A. Image locking with write-enabled false

## [Next >](../Unit%207%20-%20Summary/Summary.md)