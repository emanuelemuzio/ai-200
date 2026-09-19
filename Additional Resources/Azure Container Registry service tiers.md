---
title: "Azure Container Registry service tiers"
category: "Additional resource"
tags:
  - acr
  - azure
  - service-tiers
  - pricing
---
Azure Container Registry is available in multiple SKUs. These SKUs, also known as pricing plans or tiers, support predictable pricing and align to different capacity and usage patterns of your private container registry in Azure.

When you create a registry, you select a **Pricing Plan** that determines the features and limits of your registry. Choose the plan that aligns with your expected usage patterns, such as the number of images, storage needs, and performance requirements.

Azure Container Registry offers three **Pricing Plan** options: Basic, Standard, and Premium. Each SKU offers a different set of features and limits to accommodate various scenarios, from development and testing to production workloads.

|SKU|Description|
|---|---|
|**Basic**|A cost-optimized entry point for developers learning about Azure Container Registry. Basic registries have most of the same capabilities as Standard and Premium registries, such as authentication integration, image deletion, and webhooks. However, the included storage and image throughput are most appropriate for lower usage scenarios, and some features are not available.|
|**Standard**|Standard registries offer the same capabilities as Basic, with increased included storage and image throughput. Standard registries satisfy the needs of many production scenarios.|
|**Premium**|Premium registries provide the highest amount of included storage and concurrent operations, enabling high-volume scenarios. In addition to higher image throughput, Premium adds features such as geo-replication for high availability across regions, private endpoints to restrict access to the registry, and higher API concurrency and bandwidth throughput for large-scale concurrent deployments.|

Each SKU includes a specific amount of free storage, with additional storage available at a per-GB rate. Each SKU also has a different maximum storage limit.

The Basic, Standard, and Premium SKUs all provide the same programmatic capabilities and data plane APIs. They also all benefit from image storage managed entirely by Azure, and all SKUs have zone redundancy enabled by default in supported regions. However, the Premium SKU enables a wider range of features and has higher limits.

## SKU features and limits

The following table details the features and registry limits of the Basic, Standard, and Premium SKUs.

|Resource|Basic|Standard|Premium|
|---|---|---|---|
|Included storage1 (GiB)|10|100|500|
|Storage limit (TiB)|40|40|100|
|Maximum image layer size (GiB)|195|195|195|
|Maximum manifest size (MiB)|4|4|4|
|Webhooks|2|10|500|
|Private link with private endpoints|N/A|N/A|Supported|
|• Private endpoints|N/A|N/A|200|
|Public IP network rules|N/A|N/A|200|
|Service endpoint VNet access|N/A|N/A|Preview|
|• Virtual network rules|N/A|N/A|100|
|Repository-scoped permissions with Microsoft Entra role assignments|Supported|Supported|Supported|
|Repository-scoped permissions with non-Microsoft Entra tokens and scope maps|Supported|Supported|Supported|
|• Non-Microsoft Entra tokens|100|500|50,000|
|• Non-Microsoft Entra token scope maps|100|500|50,000|
|• Actions per non-Microsoft Entra token scope map|500|500|500|
|• Repositories per non-Microsoft Entra token scope map2|500|500|500|
|Anonymous pull access|N/A|Supported|Supported|
|Geo-replication|N/A|N/A|Supported|
|Dedicated data endpoints|N/A|N/A|Supported|
|Availability zones|Supported|Supported|Supported|
|Content trust|N/A|N/A|Supported|
|Customer-managed keys|N/A|N/A|Supported|
|Connected registries|N/A|N/A|Supported|
|Artifact streaming|N/A|N/A|Supported|
|Artifact cache rules|N/A|Supported|Supported|
|IP access rule configuration|N/A|N/A|Supported|
|Retention policy for untagged manifests|N/A|N/A|Supported|
|Artifact transfer|N/A|N/A|Supported|
|Export policy|N/A|N/A|Supported|
|Dedicated agent pools for Tasks|N/A|N/A|Supported|

1 Storage included in the daily rate for each tier. Additional storage may be used, up to the registry storage limit, at an additional daily rate per GiB. If you need storage beyond the registry storage limit, contact Azure Support.

2 Individual _actions_ of `content/delete`, `content/read`, `content/write`, `metadata/read`, `metadata/write` correspond to the limit of repositories per non-Microsoft Entra token scope map.

ACR also has the following image pull and push performance limits.

### API request rate limits

In addition to the storage and feature limits in the preceding table, Azure Container Registry enforces request rate limits on registry APIs. Rate limits are measured in requests per minute (r/m) and are determined by your registry's SKU. When your request rate exceeds a limit, the registry returns an HTTP `429 Too Many Requests` error. The response includes a `Retry-After` header that indicates how long to wait before retrying.

Requests are throttled in the following operation categories. Each category is defined by the HTTP methods used by the registry's data plane APIs:

|Operation category|HTTP methods|Examples|
|---|---|---|
|**DataplaneRead**|GET, HEAD, OPTIONS|Getting image manifests and layers, layer metadata, repository listings, and other read operations.|
|**DataplaneWrite**|PUT, PATCH, POST|Pushing image manifests and layers, tagging images, and other write operations.|
|**DataplaneDelete**|DELETE|Deleting images, manifests, and tags.|
|**OAuth**|Authentication and authorization|Authentication and authorization requests made while obtaining registry access tokens.|
|**ListReferrers**|GET|Listing referrer artifacts of a manifest, such as signatures and SBOMs.|

The following request rate limits are enforced for each SKU:

|Operation|Scope|Basic and Standard|Premium|
|---|---|---|---|
|DataplaneRead|Per registry|10,000 r/m|20,000 r/m|
|DataplaneRead|Per identity per registry|5,000 r/m|10,000 r/m|
|DataplaneWrite|Per registry|2,000 r/m|4,000 r/m|
|DataplaneWrite|Per identity per registry|1,000 r/m|2,000 r/m|
|DataplaneDelete|Per registry|1,000 r/m|4,000 r/m|
|DataplaneDelete|Per identity per registry|500 r/m|2,000 r/m|
|ListReferrers|Per registry|500 r/m|2,000 r/m|
|ListReferrers|Per identity per registry|250 r/m|1,000 r/m|
|OAuth|Per registry|10,000 r/m|20,000 r/m|

> **Note:** The rate limits listed in the preceding table are best-effort approximate maximums and are not backed by an SLA. Actual throughput may vary across registries and over time depending on infrastructure conditions, traffic patterns, and other factors.

#### Per-registry and per-identity limits

- **Per registry** limits apply to the combined request rate from all clients and identities to a single registry.
- **Per identity per registry** limits apply to the request rate from a single identity to a single registry. Per identity limits prevent a single client, such as a vulnerability scanner or a misconfigured deployment, from consuming a registry's entire request capacity.
- For a registry with anonymous pull access enabled, all anonymous requests are throttled together as a single identity for that single registry.
- For a registry with the admin user account enabled, all requests that authenticate with admin credentials are throttled together as a single identity for that registry.
- **OAuth** authentication and authorization requests are throttled per registry only, without separate per identity per registry limits.

#### Requests that count against multiple limits

Some requests count against more than one operation category, and a request is throttled if any applicable limit is exceeded. For example, a request to list the referrers of a manifest is both a read request and a referrers request. If the registry has already exhausted its read limit, referrers requests are also throttled, even if the referrers limit has not been reached.

#### How rate limits are enforced

Rate limits are enforced by using a token bucket algorithm. Each operation category has a bucket of request capacity that refills continuously at the rate shown in the preceding table. This approach is designed to tolerate bursty workloads:

- **Short bursts above the steady rate are allowed.** A spike of requests, such as a large-scale deployment pulling images across many nodes at the same time, succeeds as long as capacity remains in the bucket.
- **Sustained traffic must stay at or below the limit.** If a burst empties the bucket, subsequent requests are rejected with `429 Too Many Requests` until capacity refills.

The `Retry-After` value in a `429` response indicates the number of seconds remaining until the current throttling period ends. Because the value is calculated dynamically for each request, do not rely on a fixed `Retry-After` value.

Occasionally, during a sudden ramp-up from a low baseline, you might temporarily observe lower throughput than the published limits while the registry's infrastructure scales out to meet demand.

> **Note:** Some limits in this table can be increased by contacting Azure Support. Other limits are fixed and cannot be increased through a support request.

## Registry image pull and push performance limits

API concurrency, bandwidth throughput, and throttling during high-volume operations primarily affect image pull and push performance. Your registry SKU, network configuration, and client configuration determine these factors.

### API concurrency and bandwidth throughput limits

Your SKU determines API concurrency and bandwidth throughput. Higher SKUs support more concurrent operations and greater bandwidth for data-plane operations like listing, deleting, pushing, and pulling images.

The following factors affect API concurrency and bandwidth throughput during image pulls and pushes:

- Number and size of image layers
- Reuse of layers across images in the registry
- Additional API calls required for each operation
- Scale of concurrent deployments, such as Kubernetes deployments pulling images across many nodes simultaneously

The following client environment factors affect performance:

- Docker daemon or Podman configuration for concurrent operations
- Container runtime configuration, such as `containerd` or CRI-O concurrency settings
- Cluster configuration or cluster data plane settings

The following network factors affect performance:

- Network bandwidth and latency for the network hops from clients to the registry
- Client-side network configuration, such as firewall rules and proxy settings
- Geographic distance to the registry or nearest replica if the registry is geo-replicated

### Throttling and bandwidth constraints

During periods of high request volume, you might encounter throttling with an HTTP 429 `Too many requests` error or slow bandwidth throughput. To mitigate these problems:

- Implement retry logic with exponential backoff and jitter.
- Reduce the rate of concurrent requests.
- Space out large-scale deployments to reduce simultaneous image pulls across multiple nodes.
- If you're experiencing throttling after a sudden increase in traffic from a previously low baseline, you might temporarily see lower throughput while the registry's infrastructure scales out to meet demand.

> **Note:** If you experience persistent API throttling or slow bandwidth throughput, consider upgrading your registry SKU to a higher one. You can also contact Azure support to request a limit increase.

## Show registry usage

Usage information helps you make decisions about changing the SKU when your registry nears a limit, and helps you manage consumption. To get a snapshot of your registry's current consumption of storage and other resources, check the **Overview** page of your registry in the Azure portal. You can also use Azure CLI or PowerShell commands to inspect usage.

> **Note:** The registry's storage usage might not reflect all recent registry operations. Monitor the registry's usage metrics for up-to-date information.

Depending on your registry's SKU, usage information includes some or all of the following, along with the limit in that SKU:

- Storage consumed in bytes
- Number of webhooks
- Number of geo-replications (includes the home replica)
- Number of private endpoints
- Number of IP access rules
- Number of virtual network rules

In a geo-replicated registry, storage usage is shown for the home region. Multiply by the number of replicas for the total amount of storage.

## Change registry SKU

You can change a registry's SKU in the Azure portal or by using Azure CLI or Azure PowerShell. You can move freely between SKUs as long as the SKU you're switching to has the required maximum storage capacity.

When you change a registry's SKU, there is no downtime or impact on registry operations. However, if you move from Premium to a lower SKU, features specific to Premium are disabled. In some cases, you need to remove resources related to these features before you can switch SKUs. For example, you must delete any geo-replications or connected registries before you can switch from Premium to Standard or Basic.

To change SKUs in the Azure portal, go to your container registry. In the service menu, under **Settings**, select **Properties**. Change the option for **Pricing plan**, and then select **Save**.

To change SKUs by using the Azure CLI, use the `az acr update` command. For example, to switch to Premium:

```bash
az acr update --name myContainerRegistry --sku Premium
```

To change SKUs by using Azure PowerShell, use the `Update-AzContainerRegistry` cmdlet. For example, to switch to Premium:

```powershell
Update-AzContainerRegistry -ResourceGroupName myResourceGroup -Name myContainerRegistry -Sku Premium
```

## Concepts

- **Tier selection**: the Basic, Standard, and Premium plans balance cost, storage, and advanced capabilities to match different workload requirements.
- **Scalability and performance**: higher tiers support more throughput, concurrency, and larger operational scale for busy registry workloads.
- **Regional resilience**: geo-replication and private networking improve latency, availability, and control over access.
- **Operational governance**: monitoring usage, managing limits, and choosing a tier deliberately helps avoid throttling and unnecessary cost.
- **Lifecycle planning**: registry health depends on matching the SKU to real usage patterns, then adjusting it as demand changes.