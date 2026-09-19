---
title: "Unit 02 - Registries, Repositories, and Artifacts"
aliases:
  - ACR fundamentals
  - Registry hierarchy
  - Containers and artifacts
tags:
  - ai-200
  - azure
  - acr
  - unit-02
---

# Unit 02 - Registries, Repositories, and Artifacts

## Overview

Understanding how Azure Container Registry (ACR) organizes container images helps you design an effective storage strategy for AI applications. This unit explains the registry hierarchy and shows how manifests, layers, and digests enable efficient storage and retrieval of container artifacts.

## Understand Azure Container Registry

Azure Container Registry is a managed, private Docker registry service that stores and distributes container images and related artifacts. Unlike public registries such as Docker Hub, ACR gives you direct control over access, geo-replication for global distribution, and integration with Azure services such as Azure Kubernetes Service and Azure Container Apps.

For AI workloads, ACR offers several important capabilities:

- **Private storage**: keep model-serving images, preprocessing containers, and inference APIs secure within your Azure environment
- **Geo-replication**: distribute images close to deployment regions for faster pulls and reduced latency
- **Integration**: connect directly to Azure Kubernetes Service, Azure Container Apps, and Azure App Service for seamless deployments
- **Content formats**: store Docker images, Helm charts, and OCI artifacts in a single registry

ACR supports Basic, Standard, and Premium service tiers. Most developer workflows work similarly across tiers, though features like content trust and private endpoints require Premium.

## Registry hierarchy

ACR uses a three-level hierarchy to organize content.

### Registry

The registry is the top-level resource that hosts all container content. Each registry has a unique login server URL in the format `<registry-name>.azurecr.io`.

Example:

```text
contosoinference.azurecr.io
```

A registry contains multiple repositories and provides authentication, access control, and management capabilities.

### Repository

A repository is a collection of container images with the same name but different tags. For example, a repository named `inference-api` contains all versions of your inference API image.

Repositories support namespaces using forward slashes for organization. This lets you group related images logically:

- `production/inference-api` for production-ready images
- `staging/inference-api` for images under validation
- `ml-team/model-server` for team-specific images

### Artifact

An artifact is the actual container image or other content stored in a repository. Each artifact has tags that identify it, layers that make up its content, and a manifest that describes its structure.

## Tags, layers, and manifests

Each component of an artifact serves a specific purpose.

### Tags

Tags identify specific versions of an artifact within a repository. The format `repository:tag` provides a human-readable reference.

Example:

```text
inference-api:v1.2.0
```

A single artifact can have multiple tags pointing to it. This is useful for concepts like `latest`, `stable`, and version-specific references.

### Layers

Container images consist of one or more layers. Each layer maps to a Dockerfile instruction that modifies the filesystem. Layers are content-addressable and can be shared across images.

### Manifests

Every artifact has a manifest that lists its layers and configuration. The manifest is identified by a SHA-256 digest in the format `sha256:abc123...`.

Unlike tags, digests are immutable. Pulling by digest guarantees that you get the exact image you expect.

## Addressing artifacts for push and pull operations

ACR supports two common addressing formats.

### By tag

```bash
docker pull myregistry.azurecr.io/inference-api:v1.2.0
docker push myregistry.azurecr.io/inference-api:v1.2.0
```

### By digest

```bash
docker pull myregistry.azurecr.io/inference-api@sha256:0a2e01852872580b2c2fea9380ff8d7b637d3928783c55beb3f21a6e58d5d108
```

Digest-based addressing is best when you need guaranteed reproducibility.

## Best practices for organizing registries

- Use namespaces to organize repositories by team, environment, or project
- Plan repository structure around deployment patterns and team ownership
- Enable geo-replication for global AI deployments
- Monitor storage and apply retention policies

## Additional resources

- [[resources/about-registries-repositories-and-artifacts]]
- [[resources/azure-container-registry-service-tiers]]
- [[resources/best-practices-for-azure-container-registry]]

## Related notes

- [[../01-introduction/index]]
- [[../03-build-and-run-images-with-acr-tasks/index]]
