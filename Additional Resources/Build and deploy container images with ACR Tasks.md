---
title: "Build and deploy container images with ACR Tasks"
category: "Additional resource"
tags:
  - acr
  - azure
  - tasks
  - container
  - deployment
---
ACR Tasks is a suite of features within Azure Container Registry that provides streamlined and efficient Docker container image builds in Azure. In this article, you learn how to use the *quick task* feature of ACR Tasks.

The "inner-loop" development cycle is the iterative process of writing code, building, and testing your application before committing to source control. A quick task extends your inner-loop to the cloud, providing build success validation and automatic pushing of successfully built images to your container registry. Your images are built natively in the cloud, close to your registry, enabling faster deployment.

All your Dockerfile expertise is directly transferable to ACR Tasks. You do not have to change your Dockerfiles to build in the cloud, only the command you run.

In this tutorial, part one of a series:

- Get the sample application source code
- Build a container image in Azure
- Deploy a container to Azure Container Instances

In subsequent tutorials, you learn to use ACR Tasks for automated container image builds on code commit and base image update. ACR Tasks can also run multi-step tasks, using a YAML file to define steps to build, push, and optionally test multiple containers.

## Prerequisites

### GitHub account

Create an account on [Github](https://github.com) if you do not already have one. This tutorial series uses a GitHub repository to demonstrate automated image builds in ACR Tasks.

### Fork sample repository

Next, use the GitHub UI to fork the sample repository into your GitHub account. In this tutorial, you build a container image from the source in the repo, and in the next tutorial, you push a commit to your fork of the repo to kick off an automated task.

Fork this [repository](https://github.com/Azure-Samples/acr-build-helloworld-node) 

### Clone your fork

Once you've forked the repo, clone your fork and enter the directory containing your local clone.

Clone the repo with `git`, replace **<your-github-username>** with your GitHub username:

```bash
git clone https://github.com/<your-github-username>/acr-build-helloworld-node
```

Enter the directory containing the source code:

```bash
cd acr-build-helloworld-node
```

### Bash shell

The commands in this tutorial series are formatted for the Bash shell. If you prefer to use PowerShell, Command Prompt, or another shell, you may need to adjust the line continuation and environment variable format accordingly.

### Prepare your environment for the Azure CLI

- Use the Bash environment in Azure Cloud Shell.
- If you prefer to run CLI reference commands locally, install the Azure CLI. If you're running on Windows or macOS, consider running Azure CLI in a Docker container.
  - If you're using a local installation, sign in to the Azure CLI by using the `az login` command. To finish the authentication process, follow the steps displayed in your terminal.
  - When you're prompted, install the Azure CLI extension on first use.
  - Run `az version` to find the version and dependent libraries that are installed. To upgrade to the latest version, run `az upgrade`.

## Build in Azure with ACR Tasks

Now that you've pulled the source code down to your machine, follow these steps to create a container registry and build the container image with ACR Tasks.

To make executing the sample commands easier, the tutorials in this series use shell environment variables. Execute the following command to set the `ACR_NAME` variable. Replace **<registry-name>** with a unique name for your new container registry. The registry name must be unique within Azure, contain only lower case letters, and contain 5-50 alphanumeric characters. The other resources you create in the tutorial are based on this name, so you should need to modify only this first variable.

```bash
ACR_NAME=<registry-name>
```

With the container registry environment variable populated, you should now be able to copy and paste the remainder of the commands in the tutorial without editing any values. Execute the following commands to create a resource group and container registry.

```bash
RES_GROUP=$ACR_NAME # Resource Group name

az group create --resource-group $RES_GROUP --location eastus
az acr create --resource-group $RES_GROUP --name $ACR_NAME --sku Standard --location eastus
```

Now that you have a registry, use ACR Tasks to build a container image from the sample code. Execute the `az acr build` command to perform a *quick task*.

> **Note:** The Dockerfile used in the following example depends on a public base container image from Docker Hub. To improve reliability when using public content, import and manage the image in a private Azure container registry and update your Dockerfile to use your privately managed base image.

```bash
az acr build --registry $ACR_NAME --image helloacrtasks:v1 --file /path/to/Dockerfile /path/to/build/context.
```

Output from the `az acr build` command is similar to the following. You can see the upload of the source code (the "context") to Azure, and the details of the `docker build` operation that the ACR task runs in the cloud. Because ACR tasks use `docker build` to build your images, no changes to your Dockerfiles are required to start using ACR Tasks immediately.

```text
Packing source code into tar file to upload...
Sending build context (4.813 KiB) to ACR...
Queued a build with build ID: da1
Waiting for build agent...
2023/11/18 18:31:42 Using acb_vol_01185991-be5f-42f0-9403-a36bb997ff35 as the home volume
2023/11/18 18:31:42 Setting up Docker configuration...
2023/11/18 18:31:43 Successfully set up Docker configuration
2023/11/18 18:31:43 Logging in to registry: myregistry.azurecr.io
2023/11/18 18:31:55 Successfully logged in
Sending build context to Docker daemon   21.5kB
Step 1/5 : FROM node:15-alpine
15-alpine: Pulling from library/node
Digest: sha256:8dafc0968fb4d62834d9b826d85a8feecc69bd72cd51723c62c7db67c6dec6fa
Status: Image is up to date for node:15-alpine
 ---> a56170f59699
Step 2/5 : COPY . /src
 ---> 88087d7e709a
Step 3/5 : RUN cd /src && npm install
 ---> Running in e80e1263ce9a
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN helloworld@1.0.0 No repository field.

up to date in 0.1s
Removing intermediate container e80e1263ce9a
 ---> 26aac291c02e
Step 4/5 : EXPOSE 80
 ---> Running in 318fb4c124ac
Removing intermediate container 318fb4c124ac
 ---> 113e157d0d5a
Step 5/5 : CMD ["node", "/src/server.js"]
 ---> Running in fe7027a11787
Removing intermediate container fe7027a11787
 ---> 20a27b90eb29
Successfully built 20a27b90eb29
Successfully tagged myregistry.azurecr.io/helloacrtasks:v1
2023/11/18 18:32:11 Pushing image: myregistry.azurecr.io/helloacrtasks:v1, attempt 1
The push refers to repository [myregistry.azurecr.io/helloacrtasks]
6428a18b7034: Preparing
c44b9827df52: Preparing
172ed8ca5e43: Preparing
8c9992f4e5dd: Preparing
8dfad2055603: Preparing
c44b9827df52: Pushed
172ed8ca5e43: Pushed
8dfad2055603: Pushed
6428a18b7034: Pushed
8c9992f4e5dd: Pushed
v1: digest: sha256:b038dcaa72b2889f56deaff7fa675f58c7c666041584f706c783a3958c4ac8d1 size: 1366
2023/11/18 18:32:43 Successfully pushed image: myregistry.azurecr.io/helloacrtasks:v1
2023/11/18 18:32:43 Step ID acb_step_0 marked as successful (elapsed time in seconds: 15.648945)
The following dependencies were found:
- image:
    registry: myregistry.azurecr.io
    repository: helloacrtasks
    tag: v1
    digest: sha256:b038dcaa72b2889f56deaff7fa675f58c7c666041584f706c783a3958c4ac8d1
  runtime-dependency:
    registry: registry.hub.docker.com
    repository: library/node
    tag: 15-alpine
    digest: sha256:8dafc0968fb4d62834d9b826d85a8feecc69bd72cd51723c62c7db67c6dec6fa
  git: {}

Run ID: da1 was successful after 1m9.970148252s
```

Near the end of the output, ACR Tasks displays the dependencies it has discovered for your image. This enables ACR Tasks to automate image builds on base image updates, such as when a base image is updated with OS or framework patches.

## Deploy to Azure Container Instances

ACR Tasks automatically push successfully built images to your registry by default, allowing you to deploy them from your registry immediately.

In this section, you create an Azure Key Vault and service principal, then deploy the container to Azure Container Instances (ACI) using the service principal's credentials.

### Configure registry authentication

All production scenarios should use service principals to access an Azure container registry. Service principals allow you to provide role-based access control to your container images. For example, you can configure a service principal with pull-only access to a registry.

#### Create a key vault

If you do not already have a vault in Azure Key Vault, create one with the Azure CLI using the following commands.

```bash
AKV_NAME=$ACR_NAME-vault

az keyvault create --resource-group $RES_GROUP --name $AKV_NAME
```

#### Create a service principal and store credentials

You now need to create a service principal and store its credentials in your key vault.

Use the `az ad sp create-for-rbac` command to create the service principal, and `az keyvault secret set` to store the service principal's **password** in the vault. Use Azure CLI version **2.25.0** or later for these commands.

The correct role to use in the role assignment depends on whether the registry is ABAC-enabled or not.

```bash
# Create service principal, store its password in AKV (the registry *password*)
ROLE="Container Registry Repository Reader" # For ABAC-enabled registries. For non-ABAC registries, use AcrPull.
az keyvault secret set \
  --vault-name $AKV_NAME \
  --name $ACR_NAME-pull-pwd \
  --value $(az ad sp create-for-rbac \
                --name $ACR_NAME-pull \
                --scopes $(az acr show --name $ACR_NAME --query id --output tsv) \
                --role "$ROLE" \
                --query password \
                --output tsv)
```

The `--role` argument in the preceding command configures the service principal with a built-in role to grant it pull-only access to the registry. The correct role to use in the role assignment depends on whether the registry is ABAC-enabled or not, with ABAC-enabled registries needing the `Container Registry Repository Reader` role and non-ABAC registries needing the `AcrPull` role.

To grant both push and pull access, change the `--role` argument to either the `Container Registry Repository Writer` role for ABAC-enabled registries, or the `AcrPush` role for non-ABAC-enabled registries.

For more information about Microsoft Entra ABAC, see the Microsoft Entra-based repository permissions guidance for Azure Container Registry.

Next, store the service principal's _appId_ in the vault, which is the **username** you pass to Azure Container Registry for authentication:

```bash
# Store service principal ID in AKV (the registry *username*)
az keyvault secret set \
    --vault-name $AKV_NAME \
    --name $ACR_NAME-pull-usr \
    --value $(az ad sp list --display-name $ACR_NAME-pull --query [].appId --output tsv)
```

You've created an Azure Key Vault and stored two secrets in it:

- `$ACR_NAME-pull-usr`: The service principal ID, for use as the container registry **username**.
- `$ACR_NAME-pull-pwd`: The service principal password, for use as the container registry **password**.

You can now reference these secrets by name when you or your applications and services pull images from the registry.

### Deploy a container with Azure CLI

Now that the service principal credentials are stored as Azure Key Vault secrets, your applications and services can use them to access your private registry.

Execute the following `az container create` command to deploy a container instance. The command uses the service principal's credentials stored in Azure Key Vault to authenticate to your container registry.

```bash
az container create \
    --resource-group $RES_GROUP \
    --name acr-tasks \
    --image $ACR_NAME.azurecr.io/helloacrtasks:v1 \
    --registry-login-server $ACR_NAME.azurecr.io \
    --registry-username $(az keyvault secret show --vault-name $AKV_NAME --name $ACR_NAME-pull-usr --query value -o tsv) \
    --registry-password $(az keyvault secret show --vault-name $AKV_NAME --name $ACR_NAME-pull-pwd --query value -o tsv) \
    --dns-name-label acr-tasks-$ACR_NAME \
    --query "{FQDN:ipAddress.fqdn}" \
    --output table
```

The `--dns-name-label` value must be unique within Azure, so the preceding command appends your container registry's name to the container's DNS name label. The output from the command displays the container's fully qualified domain name (FQDN), for example:

```text
FQDN
----------------------------------------------
acr-tasks-myregistry.eastus.azurecontainer.io
```

Take note of the container's FQDN; you will use it in the next section.

### Verify the deployment

To watch the startup process of the container, use the `az container attach` command:

```bash
az container attach --resource-group $RES_GROUP --name acr-tasks
```

The `az container attach` output first displays the container's status as it pulls the image and starts, then binds your local console's STDOUT and STDERR to that of the container.

```text
Container 'acr-tasks' is in state 'Running'...
(count: 1) (last timestamp: 2023-11-18 18:39:10+00:00) pulling image "myregistry.azurecr.io/helloacrtasks:v1"
(count: 1) (last timestamp: 2023-11-18 18:39:15+00:00) Successfully pulled image "myregistry.azurecr.io/helloacrtasks:v1"
(count: 1) (last timestamp: 2023-11-18 18:39:17+00:00) Created container
(count: 1) (last timestamp: 2023-11-18 18:39:17+00:00) Started container

Start streaming logs:
Server running at http://localhost:80
```

When `Server running at http://localhost:80` appears, navigate to the container's FQDN in your browser to see the running application. The FQDN should have been displayed in the output of the `az container create` command you executed in the previous section.

To detach your console from the container, hit `Control+C`.

## Clean up resources

Stop the container instance with the `az container delete` command: 

```bash
az container delete --resource-group $RES_GROUP --name acr-tasks
```

To remove all resources you've created in this tutorial, including the container registry, key vault, and service principal, issue the following commands. These resources are used in the next tutorial in the series, however, so you might want to keep them if you move on directly to the next tutorial. 

```bash
az group delete --resource-group $RES_GROUP
az ad sp delete --id http://$ACR_NAME-pull
```

## Concepts

- Inner-loop automation: quick tasks move the build-and-test cycle into the cloud so developers can validate container images before they commit changes.
- Registry-first delivery: ACR builds and stores images in a central registry, making deployment and reuse easier across environments.
- Dependency awareness: the registry can detect image dependencies and help teams react to base-image updates before drift becomes a production issue. See [Additional Resources/ACR Tasks Overview.md](ACR%20Tasks%20overview.md).
- Secure deployment: Key Vault and service principals reduce secret exposure while allowing a container to pull from a private registry. See [Additional Resources/About registries, repositories, and artifacts.md](About%20registries,%20repositories,%20and%20artifacts.md).
