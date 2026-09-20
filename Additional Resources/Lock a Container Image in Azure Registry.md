---
title: "Lock a container image in an Azure container registry"
category: "Additional resource"
tags:
  - acr
  - azure
  - container
  - image
  - versioning
---
In an Azure container registry, you can lock an image version or a repository so that it cannot be deleted or updated. To lock an image or a repository, update its attributes using the Azure CLI command `az acr repository update`.

This article requires that you run the Azure CLI in Azure Cloud Shell or locally. Run `az --version` to find the version. If you need to install or upgrade, follow the Azure CLI installation guidance for your platform.

> **Important:** This article does not apply to locking an entire registry resource with Azure management locks. Locking a registry resource does not prevent data changes inside repositories; it only affects management operations such as registry deletion or replication changes.

## Scenarios

By default, a tagged image in Azure Container Registry is *mutable*, so with appropriate permissions you can repeatedly update and push an image with the same tag to a registry. Container images can also be deleted as needed. This behavior is useful when you develop images and need to maintain a manageable registry size.

However, when you deploy a container image to production, you might need an *immutable* container image. An immutable image is one that you cannot accidentally delete or overwrite.

Use the `az acr repository update` command to set repository attributes so you can:

- Lock an image version or an entire repository
- Protect an image version or repository from deletion while allowing updates
- Prevent read operations on an image version or repository

See the following sections for examples.

## Lock an image or repository

### Show the current repository attributes

To see the current attributes of a repository, run the following command:

```bash
az acr repository show \
    --name myregistry --repository myrepo \
    --output jsonc
```

### Show the current image attributes

To see the current attributes of a tag, run the following command:

```bash
az acr repository show \
    --name myregistry --image myrepo:tag \
    --output jsonc
```

### Lock an image by tag

To lock the `myrepo:tag` image in `myregistry`, run the following command:

```bash
az acr repository update \
    --name myregistry --image myrepo:tag \
    --write-enabled false
```

### Lock an image by manifest digest

To lock a `myrepo` image identified by manifest digest (`sha256:...`), run the following command. To find the manifest digest associated with one or more image tags, run the corresponding manifest metadata command.

```bash
az acr repository update \
    --name myregistry --image myrepo@sha256:123456abcdefg \
    --write-enabled false
```

### Lock a repository

To lock the `myrepo` repository and all images in it, run the following command:

```bash
az acr repository update \
    --name myregistry --repository myrepo \
    --write-enabled false
```

### List the current repository attributes

To update the repository attributes to indicate image lock listing, run the following command:

```bash
az acr repository update \
    --name myregistry --repository myrepo \
    --list-enabled false
```

### Show the image attributes on image lock

To query the tags on an image lock with `--list-enabled false`, run the following command:

```bash
az acr repository show-manifests \
    --name myregistry --repository myrepo \
    --query "[?listEnabled==null].tags" \
    --output table
```

## Check image attributes for tag and its corresponding manifest

The changeable attributes of tags and manifests are managed separately. That is, setting `deleteEnabled=false` for the tag does not set the same flag for the corresponding manifest.

Query the attributes using the script below:

```bash
registry="myregistry"
repo="myrepo"
tag="mytag"

az login
az acr repository show -n $registry --repository $repo
az acr manifest show-metadata -r $registry -n "$repo:$tag"
digest=$(az acr manifest show-metadata -r $registry -n "$repo:$tag" --query digest -o tsv)
az acr manifest show-metadata -r $registry -n "$repo@$digest"
```

> **Note:** If the image attributes are set with `writeEnabled=false` or `deleteEnabled=false`, image deletion is blocked.

## Protect an image or repository from deletion

### Protect an image from deletion

To allow the `myrepo:tag` image to be updated but not deleted, run the following command:

```bash
az acr repository update \
    --name myregistry --image myrepo:tag \
    --delete-enabled false --write-enabled true
```

### Protect a repository from deletion

The following command sets the `myrepo` repository so it cannot be deleted. Individual images can still be updated or deleted.

```bash
az acr repository update \
    --name myregistry --repository myrepo \
    --delete-enabled false --write-enabled true
```

## Prevent read operations on an image or repository

To prevent read operations on the `myrepo:tag` image, run the following command:

```bash
az acr repository update \
    --name myregistry --image myrepo:tag \
    --read-enabled false
```

To prevent read operations on all images in the `myrepo` repository, run the following command:

```bash
az acr repository update \
    --name myregistry --repository myrepo \
    --read-enabled false
```

## Unlock an image or repository

To restore the default behavior of the `myrepo:tag` image so that it can be deleted and updated, run the following command:

```bash
az acr repository update \
    --name myregistry --image myrepo:tag \
    --delete-enabled true --write-enabled true
```

To restore the default behavior of the `myrepo` repository, enabling individual images to be deleted and updated, run the following command:

```bash
az acr repository update \
    --name myregistry --repository myrepo \
    --delete-enabled true --write-enabled true
```

However, if there is a lock on the manifest, you need to run an additional command to unlock the manifest.

```bash
az acr repository update \
   --name myregistry --image $repo@$digest \
   --delete-enabled true --write-enabled true
```

> **Note:** If it has sufficient permissions, the `acr purge` command can unlock locked artifacts automatically. When run with the `--include-locked` parameter, it resets `delete-enabled` and `write-enabled` to `true` on each matching locked tag or manifest before deleting it.

## Concepts

- Immutability of production images: locking image tags or repositories prevents accidental overwrite or deletion, which is essential once a version is promoted to production. See [Unit 4 - Tag and version images/Tag and version images.md](../Unit%204%20-%20Tag%20and%20version%20images/Tag%20and%20version%20images.md).
- Deployment safety: immutable artifacts support stable rollouts and safer rollback because each running version stays available until you explicitly retire it.
- Registry hygiene: lock and purge patterns help maintain a trustworthy registry without losing the ability to clean up obsolete artifacts in a controlled way.
- Policy and governance: access rules and repository attributes are part of operational safety, ensuring artifacts are not modified by accident in shared environments.
