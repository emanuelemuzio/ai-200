---
title: "Unit 04 - Tag and Version Images"
aliases:
  - Tagging strategy
  - Image versioning
  - Tags and digests
tags:
  - ai-200
  - acr
  - docker
  - versioning
---

# Unit 04 - Tag and version images

## Why tagging matters

Tags give a human-readable name to a specific image version. In production, consistent versioning helps teams identify exactly what is running and makes rollout and rollback easier.

## Tag format

```text
registry/repository:tag
```

Examples:

```text
myregistry.azurecr.io/inference-api:v1.2.0
myregistry.azurecr.io/inference-api:stable
```

## Tagging best practices

- Use semantic versioning when possible: `v1.2.0`
- Keep `latest` only for development or quick testing
- Use environment-specific tags such as `prod`, `staging`, or `dev`
- Prefer immutable versions for production deployments

## Mutable vs immutable references

Tags are mutable because the same tag can be reassigned to a different image later. Digests are immutable and are safer for production rollout guarantees.

## Example workflow

```bash
# Build a local image
docker build -t inference-api:latest .

# Tag it for ACR
docker tag inference-api:latest myregistry.azurecr.io/inference-api:v1.2.0

# Push to ACR
docker push myregistry.azurecr.io/inference-api:v1.2.0

# Pull by tag
docker pull myregistry.azurecr.io/inference-api:v1.2.0
```

## Digests and reproducibility

A digest looks like this:

```text
sha256:0a2e01852872580b2c2fea9380ff8d7b637d3928783c55beb3f21a6e58d5d108
```

Using the digest ensures:

- the exact image is reused
- no accidental tag rewrite occurs
- production deployments remain consistent

## Recommendation

Use tags for readability and digest references for final deployment certainty.

## Related notes

- [[../03-build-and-run-images-with-acr-tasks/index]]
- [[../05-exercise-build-and-manage-a-container-image-with-acr-tasks/index]]
