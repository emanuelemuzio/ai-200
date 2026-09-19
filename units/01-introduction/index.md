---
title: "Unit 01 - Introduction"
aliases:
  - AI 200 introduction
  - ACR overview
  - Why Azure Container Registry
  - Unit 1
tags:
  - ai-200
  - azure
  - acr
  - intro
---

# Unit 01 - Introduction

## Context

AI applications require a secure and scalable place to store container images that serve inference APIs, data pipelines, and backend services. This module introduces Azure Container Registry (ACR) as the platform for storing, building, and managing container images for AI workloads in Azure.

Imagine you are a developer building a real-time AI inference service. Your team maintains several container images: a model-serving API, a preprocessing service, and a monitoring sidecar. Each image requires updates as models improve and dependencies change.

## Problem to solve

Currently, your team builds images locally and pushes them from developer workstations, leading to inconsistent builds and unclear versioning. Your client expects reliable deployments with traceable image versions and the ability to roll back to previous releases.

## Why this matters

You need a centralized registry that supports cloud-based builds, enforces consistent tagging, and integrates with your deployment pipelines.

## Learning objectives

After completing this module, you will be able to:

- Explain how Azure Container Registry organizes images using registries, repositories, and artifacts
- Build and manage container images in the cloud using ACR Tasks
- Implement tagging and versioning strategies for reliable container deployments
- Use the Azure CLI to manage container images and run ACR quick tasks

## Summary

ACR provides a private, managed, Azure-native registry for securely distributing container images and artifacts. For AI workloads, this means better control, stronger traceability, and more predictable deployments.

## Related notes

- [[../02-registries-repositories-and-artifacts/index]]
- [[../03-build-and-run-images-with-acr-tasks/index]]
