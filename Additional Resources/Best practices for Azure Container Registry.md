---
title: "Best practices for Azure Container Registry"
category: "Additional resource"
tags:
  - acr
  - azure
  - best-practices
  - governance
--- 

By following these best practices, you can help maximize the performance and cost-effective use of your private registry in Azure to store and deploy container images and other artifacts.

A well-designed registry is not just a place to store images: it is part of the delivery pipeline. The right choice of region, image structure, governance model, and cleanup strategy can reduce latency, improve security, and avoid unnecessary cost.

## Network-close deployment

Create your container registry in the same Azure region in which you deploy containers. Placing your registry in a region that is network-close to your container hosts can help lower both latency and cost.

Network-close deployment is one of the primary reasons for using a private container registry. Docker images have an efficient layering model that allows for incremental deployments. However, new nodes need to pull all layers required for a given image. This initial `docker pull` can quickly add up to multiple gigabytes. Having a private registry close to your deployment minimizes network latency, and it also reduces data transfer costs associated with cross-region image pulls.

## Geo-replicate multi-region deployments

Use Azure Container Registry geo-replication if you're deploying containers to multiple regions. Whether you're serving global customers from local data centers or your development team is in different locations, you can simplify registry management and minimize latency by replicating your registry across regions. You can also configure regional webhooks to notify you of events in specific replicas when images are pushed.

Geo-replication is particularly useful for Premium registries that need consistent global deployment patterns and lower latency for users in different regions.

## Maximize pull performance

In addition to placing images close to your deployments, the characteristics of your images themselves can strongly affect pull performance.

- **Image size** - Minimize the sizes of your images by removing unnecessary layers or reducing the size of layers. A common technique is to use a multi-stage build to include only the necessary runtime components.
- **Number of layers** - Balance the number of layers used. If you have too few, you do not benefit from layer reuse and caching on the host. Too many, and your deployment environment spends more time pulling and decompressing. Five to 10 layers is often a good target.

Also choose a service tier of Azure Container Registry that meets your performance needs. The Premium tier provides the greatest bandwidth and highest rate of concurrent read and write operations when you have high-volume deployments.

## Repository namespaces

By using repository namespaces, you can allow sharing a single registry across multiple groups within your organization. Registries can be shared across deployments and teams. Azure Container Registry supports nested namespaces, enabling group isolation. However, the registry manages all repositories independently, not as a hierarchy.

For example, consider the following container image tags. Images that are used corporate-wide, like `aspnetcore`, are placed in the root namespace, while container images owned by different groups use their own namespaces.

- _contoso.azurecr.io/aspnetcore:2.0_
- _contoso.azurecr.io/products/widget/web:1_
- _contoso.azurecr.io/products/bettermousetrap/refundapi:12.3_
- _contoso.azurecr.io/marketing/2023-fall/concertpromotions/campaign:218.42_

## Dedicated resource group

Because container registries are resources that are used across multiple container hosts, a registry should reside in its own resource group.

Although you might experiment with a specific host type, such as Azure Container Instances, you will likely want to delete the container instance when you're done. However, you might also want to keep the collection of images you pushed to Azure Container Registry. By placing your registry in its own resource group, you minimize the risk of accidentally deleting the collection of images in the registry when you delete the container instance resource group.

## Authentication and authorization

When authenticating with an Azure container registry, there are two primary scenarios: individual authentication and service, or "headless", authentication. The following table provides a brief overview of these scenarios and the recommended method for each.

|Type|Example scenario|Recommended method|
|---|---|---|
|Individual identity|A developer pulling images to or pushing images from their development machine.|Azure CLI login with an identity that can access the registry|
|Headless/service identity|Build and deployment pipelines where the user isn't directly involved.|Service principal or managed identity|

Azure Container Registry supports security practices in your organization to distribute duties and privileges to different identities. Use role-based access control to assign appropriate permissions to different users, service principals, or other identities that perform different registry operations. For example, assign push permissions to a service principal used in a build pipeline and assign pull permissions to a different identity used for deployment. Use repository-scoped permissions for fine-grained access to specific repositories when needed.

## Manage registry size

The storage constraints of each container registry service tier are intended to align with a typical scenario: **Basic** for getting started, **Standard** for most production applications, and **Premium** for hyper-scale performance and geo-replication. Throughout the life of your registry, you should manage its size by periodically deleting unused content.

Use the Azure CLI command `az acr show-usage` to display the current consumption of storage and other resources in your registry:

```bash
az acr show-usage --resource-group myResourceGroup --name myregistry --output table
```

Sample output:

```text
NAME                        LIMIT         CURRENT VALUE    UNIT
--------------------------  ------------  ---------------  ------
Size                        536870912000  215629144        Bytes
Webhooks                    500           1                Count
Geo-replications            -1            3                Count
IPRules                     100           1                Count
VNetRules                   100           0                Count
PrivateEndpointConnections  10            0                Count
```

You can also find the current storage usage in the **Overview** of your registry in the Azure portal.

> **Note:** In a geo-replicated registry, storage usage is shown for the home region. Multiply by the number of replications for total registry storage consumed.

### Delete image data

Azure Container Registry supports several methods for deleting image data from your container registry. You can delete images by tag or manifest digest, or delete a whole repository.

For details on deleting image data from your registry, including untagged or orphaned images, you can use a retention policy and routine cleanup procedures to prevent storage bloat.

## Concepts

- **Latency and locality**: placing the registry close to the workloads reduces latency and transfer costs, especially when nodes need to pull large images.
- **Multi-region replication**: geo-replication simplifies global deployment and improves resilience for distributed environments.
- **Image efficiency**: smaller images and a controlled number of layers improve pull time and caching efficiency on execution nodes.
- **Access governance**: namespaces, groups, and repository permissions help teams share the same registry securely.
- **Registry lifecycle management**: monitoring usage, removing unused images, and choosing the right tier prevents waste and performance issues.
