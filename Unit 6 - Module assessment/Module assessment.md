---
title: "Unit 06 - Module Assessment"
aliases:
  - Quiz
  - Knowledge check
  - Assessment
tags:
  - ai-200
  - assessment
  - acr
  - azure
---

# Unit 06 - Module assessment

## Self-check questions

### 1. What is Azure Container Registry primarily used for?

A. Hosting a SQL database  
B. Storing and managing container images  
C. Running Python scripts  
D. Managing virtual machines

### 2. Which ACR element groups multiple image versions under the same logical name?

A. Tag  
B. Manifest  
C. Repository  
D. Layer

### 3. What is the main advantage of using digests in production?

A. Tags are easier to read  
B. Digests are immutable and reproducible  
C. Digests reduce network latency  
D. Digests require less storage

### 4. Which command builds an image in Azure using ACR Tasks?

```bash
az acr build --registry myregistry --image inference-api:v1.0.0 .
```

### 5. Why is tagging important?

Because it helps teams identify and manage image versions consistently across builds, deployments, and rollbacks.

## Answer key

1. B  
2. C  
3. B  
4. Correct command shown above  
5. Open-ended answer: tagging supports traceability and deployment management

## Reflection

If you can describe the relationship between registry, repository, tag, and digest, you have a strong foundation for working with ACR in Azure-based AI solutions.

## Related notes

- [Course overview](../../course.md)
- [[Build and run images with ACR Tasks]]
- [[Tag and version images]]
- [[Summary]]
