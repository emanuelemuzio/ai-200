---
title: "Automatically purge images from an Azure container registry"
category: "Additional resource"
tags:
  - acr
  - azure
  - image
---
When you use an Azure container registry as part of a development workflow, the registry can quickly fill up with images or other artifacts that are no longer needed after a short period. You might want to delete all tags that are older than a certain duration or match a specified name filter.

To delete multiple artifacts quickly, use the `acr purge` command. You can run `acr purge` as an on-demand or scheduled ACR task.

> **Important:** `acr purge` is currently in preview. Treat preview features and automation carefully, especially when running destructive cleanup tasks.

The `acr purge` command is distributed as a public container image (`mcr.microsoft.com/acr/acr-cli:0.19`) and is built from the `acr-cli` source code in the GitHub repository for the Azure Container Registry tooling.

Use Azure Cloud Shell or a local installation of the Azure CLI to run the examples in this note. If needed, install or upgrade the CLI before continuing.

> **Warning:** Use the `acr purge` command with caution: deleted image data is unrecoverable. If you have systems that pull images by manifest digest instead of image name, do not purge untagged images. Deleting untagged images prevents those systems from pulling images from your registry. If your workflow depends on manifest-based pulls, use a unique tagging strategy instead.

## Use the purge command

The `acr purge` command deletes images by tag in a repository. It removes all images that match a name filter and are older than a specified duration. By default, the command deletes only tag references, not the underlying manifests and layer data. The command also supports an option to delete manifests as part of the same cleanup pass.

> **Note:** By default, `acr purge` does not delete an image tag or manifest if the `write-enabled` or `delete-enabled` attribute is set to `false`. To also purge these locked artifacts, use the `--include-locked` parameter, which unlocks each matching tag or manifest before removing it.

`acr purge` is designed to run as a container command inside an ACR task. It automatically authenticates with the registry where the task runs and performs actions there. The examples in this note use the `acr purge` command alias instead of a fully qualified container image command.

> **Important:** The standard command to run the `acr purge` command is `az acr run --registry <YOUR_REGISTRY> --cmd 'acr purge --optional parameter' /dev/null`.

We recommend running the full `acr purge` command. For example, run `acr purge --help` as `az acr run --registry <YOUR_REGISTRY> --cmd 'acr purge --help' /dev/null`.

At a minimum, specify the following options when you run `acr purge`:

- `--filter` - A repository name regular expression and a tag name regular expression to filter images in the registry. For example, `--filter "hello-world:.*"` matches all tags in the `hello-world` repository, `--filter "hello-world:^1.*"` matches tags beginning with `1`, and `--filter ".*/cache:.*"` matches all tags in repositories ending in `/cache`. You can also pass multiple `--filter` parameters.
- `--ago` - A Go-style duration string that indicates how old an image must be before it is deleted. Valid units include `d` (days), `h` (hours), and `m` (minutes). For example, `--ago 2d3h6m` selects all filtered images last modified more than two days, three hours, and six minutes ago, and `--ago 1.5h` selects images modified more than 1.5 hours ago.

`acr purge` supports several optional parameters:

- `--untagged` - Deletes manifests that do not have associated tags in addition to the tag deletions already performed. Removing all tags associated with a manifest is a prerequisite for purging the tag-free manifest.
- `--dry-run` - Shows which images would be deleted without removing any data. This is the safest way to validate selection criteria before a real purge.
- `--keep` - Retains the latest number of matching tags or manifests per repository. The keep count applies to manifests only when you specify `--untagged` or `--untagged-only` and is applied independently to tags and manifests.
- `--concurrency` - Specifies how many purge tasks run concurrently.
- `--untagged-only` - Deletes only untagged manifests without deleting any tags first. Unlike the standard `acr purge` flow, this flag makes the `--filter` and `--ago` values optional in some scenarios.
- `--include-locked` - Purges tags and manifests even when they are locked (that is, when their `write-enabled` or `delete-enabled` attributes are set to `false`). For each matching locked artifact, `acr purge` unlocks it by setting both attributes back to `true` before deleting it. Without this flag, locked tags and manifests are skipped.

> **Caution:** `--include-locked` overrides the protection provided by locking and applies to every artifact matching your `--filter` and `--ago` selection. Deleted data is unrecoverable. Run with `--dry-run` first to confirm what will be removed.

For information about additional parameters, run `acr purge --help`.

`acr purge` also supports other ACR task features such as run variables and task logs, which are streamed and saved for later retrieval.

### Run the purge command in an on-demand task

The following example uses the `az acr run` command to run `acr purge` on demand. This example deletes all image tags and any associated manifests in the `hello-world` repository in `myregistry` that were modified more than one day ago. It also removes untagged manifests, which honor the same `--ago` duration filter as tagged images.

```bash
# Environment variable for container command line
PURGE_CMD="acr purge --filter 'hello-world:.*' \
  --untagged --ago 1d"

az acr run \
  --cmd "$PURGE_CMD" \
  --registry myregistry \
  /dev/null
```

### Run the purge command in a scheduled task

The following example uses `az acr task create` to create a daily scheduled ACR task. The task purges tags modified more than seven days ago in the `hello-world` repository. The container command is passed through an environment variable and the task runs without a source context.

```bash
# Environment variable for container command line
PURGE_CMD="acr purge --filter 'hello-world:.*' \
  --ago 7d"

az acr task create --name purgeTask \
  --cmd "$PURGE_CMD" \
  --schedule "0 0 * * *" \
  --registry myregistry \
  --context /dev/null
```

Run `az acr task show` to confirm that the timer trigger is configured.

### Purge large numbers of tags and manifests

Purging a large number of tags and manifests can take several minutes or longer. If the command times out, the process deletes only a subset of tags and manifests. To ensure a large-scale purge completes, pass the `--timeout` parameter to increase the value.

For example, the following on-demand task sets a timeout value of 3,600 seconds (one hour):

```bash
# Environment variable for container command line
PURGE_CMD="acr purge --filter 'hello-world:.*' \
  --ago 1d --untagged"

az acr run \
  --cmd "$PURGE_CMD" \
  --registry myregistry \
  --timeout 3600 \
  /dev/null
```

## Example: scheduled purge of multiple repositories in a registry

This example shows how to use `acr purge` to periodically clean up multiple repositories in a registry. For example, a development pipeline might push images to the `samples/devimage1` and `samples/devimage2` repositories. After those contents are promoted to a production repository, the development artifacts are no longer needed. On a weekly basis, you can purge those repositories to prepare for the next cycle.

### Preview the purge

Before deleting data, run an on-demand purge task with the `--dry-run` parameter. This option shows which tags and manifests would be purged without removing any data.

In the following example, each repository filter selects all tags. The `--ago 0d` parameter matches images of all ages in the repositories that match the filters. The `--untagged` parameter also deletes manifests in addition to tags. The container command is passed to `az acr run` through an environment variable.

```bash
# Environment variable for container command line
PURGE_CMD="acr purge \
  --filter 'samples/devimage1:.*' --filter 'samples/devimage2:.*' \
  --ago 0d --untagged --dry-run"

az acr run \
  --cmd "$PURGE_CMD" \
  --registry myregistry \
  /dev/null
```

Review the command output to confirm the selected tags and manifests. Because the command uses `--dry-run`, no data is deleted.

Sample output:

```text
[...]
Deleting tags for repository: samples/devimage1
myregistry.azurecr.io/samples/devimage1:232889b
myregistry.azurecr.io/samples/devimage1:a21776a
Deleting manifests for repository: samples/devimage1
myregistry.azurecr.io/samples/devimage1@sha256:81b6f9c92844bbbb5d0a101b22f7c2a7949e40f8ea90c8b3bc396879d95e788b
myregistry.azurecr.io/samples/devimage1@sha256:3ded859790e68bd02791a972ab0bae727231dc8746f233a7949e40f8ea90c8b3
Deleting tags for repository: samples/devimage2
myregistry.azurecr.io/samples/devimage2:5e788ba
myregistry.azurecr.io/samples/devimage2:f336b7c
Deleting manifests for repository: samples/devimage2
myregistry.azurecr.io/samples/devimage2@sha256:8d2527cde610e1715ad095cb12bc7ed169b60c495e5428eefdf336b7cb7c0371
myregistry.azurecr.io/samples/devimage2@sha256:ca86b078f89607bc03ded859790e68bd02791a972ab0bae727231dc8746f233a

Number of deleted tags: 4
Number of deleted manifests: 4
[...]
```

### Schedule the purge

After you verify that the dry run behaves as expected, create a scheduled task to automate the purge. The following example schedules a weekly task on Sunday at 1:00 UTC:

```bash
# Environment variable for container command line
PURGE_CMD="acr purge \
  --filter 'samples/devimage1:.*' --filter 'samples/devimage2:.*' \
  --ago 0d --untagged"

az acr task create --name weeklyPurgeTask \
  --cmd "$PURGE_CMD" \
  --schedule "0 1 * * Sun" \
  --registry myregistry \
  --context /dev/null
```

Run `az acr task show` to confirm that the timer trigger is configured.

### Example: purge only untagged manifests

Sometimes you may want to remove only untagged manifests without touching any tagged images. You can achieve this by using a repository filter that matches no tag names, such as `^$`. This causes `acr purge` to skip all tags and evaluate only untagged manifests.

```bash
# Environment variable for container command line
PURGE_CMD="acr purge \
  --filter 'samples/devimage1:^$' --filter 'samples/devimage2:^$' \
  --ago 0d --untagged"

az acr task create --name weeklyPurgeTask \
  --cmd "$PURGE_CMD" \
  --schedule "0 1 * * Sun" \
  --registry myregistry \
  --context /dev/null
```

### Example: purge only untagged manifests with `--untagged-only`

The `--untagged-only` flag provides a simpler way to clean up dangling manifests without deleting any tags. Unlike `--untagged`, which removes untagged manifests in addition to tag deletions, `--untagged-only` skips tag deletion entirely.

To purge all untagged manifests across every repository in the registry:

```bash
PURGE_CMD="acr purge --untagged-only"

az acr run \
  --cmd "$PURGE_CMD" \
  --registry myregistry \
  /dev/null
```

## Purge in ABAC-enabled registries

Registries with Attribute-Based Access Control (ABAC) enabled use repository-scoped permissions instead of registry-wide roles. The `acr purge` command automatically detects ABAC-enabled registries and adjusts its authentication without requiring additional flags.

Because ABAC registries do not support wildcard token scopes, `acr purge` processes repositories in batches (default: 10). For each batch, it requests a new access token scoped to only those repositories.

### Required permissions

| Permission | Role | Scope |
| --- | --- | --- |
| List repositories | `Container Registry Repository Catalog Lister` | Registry |
| Read, delete, and manage tags and manifests | `Container Registry Repository Contributor` | Per-repository |

> **Note:** You can use ABAC conditions to scope the `Container Registry Repository Contributor` role to specific repositories, for example granting delete access only to `samples/*`.

### Purging without list permissions

If your identity does not have `Container Registry Repository Catalog Lister` permissions, you can still purge tags and manifests within a single repository by specifying it directly in the `--filter` option. Because the repository name is explicit, `acr purge` does not need to list repositories first.

```bash
PURGE_CMD="acr purge --filter 'hello-world:.+' \
  --ago 1d"

az acr run \
  --cmd "$PURGE_CMD" \
  --registry myregistry \
  /dev/null
```

In this case, only the `Container Registry Repository Contributor` role (or equivalent read and delete permissions) on the target repository is required.

### Partial access behavior

If `--filter` matches repositories your identity cannot purge, the command stops at the first unauthorized repository and reports which repositories were completed, which failed, and which were not yet processed.

> **Tip:** Use a specific `--filter` that targets only repositories your identity has access to. For example, use `--filter 'samples/.*:.*'` instead of `--filter '.*:.*'`.

## Concepts

- Registry hygiene: purging stale tags and manifests keeps the registry compact and reduces operational drift, especially in continuous integration and testing environments. See [Lock a Container Image in Azure Registry.md](./Lock%20a%20Container%20Image%20in%20Azure%20Registry.md).
- Lifecycle management: cleanup is part of the broader image lifecycle, from build and push to release, rollback, and eventual retirement of outdated artifacts. See [Tag and version images.md](../Unit%204%20-%20Tag%20and%20version%20images/Tag%20and%20version%20images.md).
- Safety controls: dry-run validation and explicit filtering help prevent accidental deletions, while lock states and retention rules protect the artifacts you still need. See [ACR Tasks Overview.md](ACR%20Tasks%20overview.md).
- Operational scaling: scheduled and batched purge jobs reduce manual effort and help keep large registries manageable as image volume grows.
