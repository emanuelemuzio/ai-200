---
title: "Unit 03 - Build and Run Images with ACR Tasks"
aliases:
  - ACR Tasks
  - Container build
  - Cloud build
  - Run container image
tags:
  - ai-200
  - acr
  - docker
  - build
---

# Unit 03 - Build and run images with ACR Tasks

## Overview

Azure Container Registry Tasks allow you to build, test, and push container images without depending on a local developer machine. This is especially useful in AI projects where image consistency and automation matter.

## Why ACR Tasks matter

Using ACR Tasks gives you:

- centralized image builds
- consistent environment setup
- automation for CI/CD workflows
- reduced local-machine dependency

## Build commands

### Azure CLI build example

```bash
az acr build --registry myregistry --image inference-api:v1.2.0 .
```

This command builds the image in Azure using the source in the current directory and stores it in the registry.

### Local build example

```bash
docker build -t inference-api:latest .
```

Local builds are useful for development, but ACR Tasks are more repeatable in shared environments.

## Running an image locally

After building or pulling an image, you can run it with Docker:

```bash
docker run -d -p 8000:8000 myregistry.azurecr.io/inference-api:v1.2.0
```

This starts a containerized app and exposes the service locally.

## Practical workflow

```bash
# Create or use an ACR registry
az acr create --resource-group my-rg --name myregistry --sku Basic

# Build using ACR Tasks
az acr build --registry myregistry --image inference-api:v1.2.0 .

# Pull the image and run it
az acr login --name myregistry
docker pull myregistry.azurecr.io/inference-api:v1.2.0
docker run -d -p 8000:8000 myregistry.azurecr.io/inference-api:v1.2.0
```

## Best use cases

Use ACR Tasks when you want to:

- standardize application builds
- automate container image creation
- keep build environments consistent across teams
- integrate builds into Azure deployment pipelines

## Summary

ACR Tasks provide a reliable way to build and run container images in a cloud-native workflow. For AI solutions, this makes image lifecycle management more predictable and easier to automate.

## Related notes

- [[../02-registries-repositories-and-artifacts/index]]
- [[../04-tag-and-version-images/index]]
