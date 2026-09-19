---
title: "Exercise - Build and Manage a Container Image with ACR Tasks"
aliases:
  - Lab
  - Practice exercise
  - ACR lab
tags:
  - exercise
  - acr
  - docker
  - azure
---

# Exercise - Build and manage a container image with ACR Tasks

## Goal

In this exercise, you will create a simple container image, push it to Azure Container Registry, and verify that it is available for reuse in a deployment workflow.

## Prerequisites

- Azure subscription
- Azure CLI installed
- Docker installed
- A resource group available in Azure

## Step 1: Create a registry

```bash
az group create --name my-rg --location eastus
az acr create --resource-group my-rg --name myregistry --sku Basic
```

## Step 2: Build the image with ACR Tasks

```bash
az acr build --registry myregistry --image inference-api:v1.0.0 .
```

This builds the image directly in Azure and pushes it into the registry.

## Step 3: Verify the image is available

```bash
az acr repository list --name myregistry --output table
az acr repository show-tags --name myregistry --repository inference-api --output table
```

## Step 4: Pull and run the image locally

```bash
az acr login --name myregistry
docker pull myregistry.azurecr.io/inference-api:v1.0.0
docker run -d -p 8000:8000 myregistry.azurecr.io/inference-api:v1.0.0
```

## Reflection

This exercise demonstrates the main ACR workflow: build, tag, push, and reuse. In real AI workloads, you would repeat this pattern for model-serving APIs, preprocessors, and monitoring sidecars.

## Related notes

- [[03-Build-and-Run-Images-with-ACR-Tasks]]
- [[04-Tag-and-Version-Images]]
- [[06-Module-Assessment]]
