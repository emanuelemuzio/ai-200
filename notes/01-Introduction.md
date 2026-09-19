---
title: "Introduction"
aliases:
  - Overview
  - AI workloads
  - ACR introduction
tags:
  - ai
  - azure
  - container-registry
  - introduction
---

# Introduction

## Context

AI applications require a secure, scalable location to store container images that serve inference APIs, data pipelines, and backend services. This module guides you through using Azure Container Registry (ACR) to store, build, and manage container images for AI solutions on Azure.

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

- [[00-Index]]
- [[02-Registries-Repositories-and-Artifacts]]
- [[03-Build-and-Run-Images-with-ACR-Tasks]]
