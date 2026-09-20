---
title: "Run multi-step build, test, and patch tasks"
category: "Additional resource"
tags:
  - acr
  - azure
  - tasks
  - yaml
  - automation
---
Multi-step tasks extend the single image build-and-push capability of ACR Tasks with multi-step, multi-container-based workflows. Use multi-step tasks to build and push several images, in series or in parallel. Then run those images as commands within a single task run. Each step defines a container image build or push operation, and can also define the execution of a container. Each step in a multi-step task uses a container as its execution environment.

Important

If you previously created tasks during the preview with the `az acr build-task` command, those tasks need to be re-created using the `az acr task` command.

For example, you can run a task with steps that automate the following logic:

1. Build a web application image
2. Run the web application container
3. Build a web application test image
4. Run the web application test container which performs tests against the running application container
5. If the tests pass, build a Helm chart archive package
6. Perform a `helm upgrade` using the new Helm chart archive package

All steps are performed within Azure, offloading the work to Azure's compute resources and freeing you from infrastructure management. Besides your Azure container registry, you pay only for the resources you use. For information on pricing, see the Container Build section of Azure Container Registry pricing.

## Common task scenarios

Multi-step tasks enable scenarios like the following logic:

- Build, tag, and push one or more container images, in series or in parallel.
- Run and capture unit test and code coverage results.
- Run and capture functional tests. ACR Tasks supports running more than one container, executing a series of requests between them.
- Perform task-based execution, including pre/post steps of a container image build.
- Deploy one or more containers with your favorite deployment engine to your target environment.

## Multi-step task definition

A multi-step task in ACR Tasks is defined as a series of steps within a YAML file. Each step can specify dependencies on the successful completion of one or more previous steps. The following task step types are available:

- `build`: Build one or more container images using familiar `docker build` syntax, in series or in parallel.
- `push`: Push built images to a container registry. Private registries like Azure Container Registry are supported, as is the public Docker Hub.
- `cmd`: Run a container, such that it can operate as a function within the context of the running task. You can pass parameters to the container's `[ENTRYPOINT]`, and specify properties like env, detach, and other familiar `docker run` parameters. The `cmd` step type enables unit and functional testing, with concurrent container execution.

The following snippets show how to combine these task step types. Multi-step tasks can be as simple as building a single image from a Dockerfile and pushing to your registry, with a YAML file similar to:

```yaml
version: v1.1.0
steps:
  - build: -t $Registry/hello-world:$ID .
  - push: ["$Registry/hello-world:$ID"]
```

Or more complex, such as this fictitious multi-step definition which includes steps for build, test, helm package, and helm deploy (container registry and Helm repository configuration not shown):

```yaml
version: v1.1.0
steps:
  - id: build-web
    build: -t $Registry/hello-world:$ID .
    when: ["-"]
  - id: build-tests
    build: -t $Registry/hello-world-tests ./funcTests
    when: ["-"]
  - id: push
    push: ["$Registry/helloworld:$ID"]
    when: ["build-web", "build-tests"]
  - id: hello-world-web
    cmd: $Registry/helloworld:$ID
  - id: funcTests
    cmd: $Registry/helloworld:$ID
    env: ["host=helloworld:80"]
  - cmd: $Registry/functions/helm package --app-version $ID -d ./helm ./helm/helloworld/
  - cmd: $Registry/functions/helm upgrade helloworld ./helm/helloworld/ --reuse-values --set helloworld.image=$Registry/helloworld:$ID
```

See task examples and Dockerfiles for several scenarios.

## Run a sample task

Tasks support both manual execution, called a "quick run," and automated execution on Git commit or base image update.

To run a task, you first define the task's steps in a YAML file, then execute the Azure CLI command `az acr run`.

Here's an example command that runs a task using a sample task YAML file. Its steps build and then push an image. Update `\<acrName\>` with the name of your own Azure container registry before running the command.

```bash
az acr run --registry <acrName> -f build-push-hello-world.yaml https://github.com/Azure-Samples/acr-tasks.git
```

When you run the task, the output should show the progress of each step defined in the YAML file. In the following output, the steps appear as `acb_step_0` and `acb_step_1`.

```bash
az acr run --registry myregistry -f build-push-hello-world.yaml https://github.com/Azure-Samples/acr-tasks.git
```

```text
Sending context to registry: myregistry...
Queued a run with ID: yd14
Waiting for an agent...
2023/09/12 20:08:44 Using acb_vol_0467fe58-f6ab-4dbd-a022-1bb487366941 as the home volume
2023/09/12 20:08:44 Creating Docker network: acb_default_network
2023/09/12 20:08:44 Successfully set up Docker network: acb_default_network
2023/09/12 20:08:44 Setting up Docker configuration...
2023/09/12 20:08:45 Successfully set up Docker configuration
2023/09/12 20:08:45 Logging in to registry: myregistry.azurecr-test.io
2023/09/12 20:08:46 Successfully logged in
2023/09/12 20:08:46 Executing step: acb_step_0
2023/09/12 20:08:46 Obtaining source code and scanning for dependencies...
2023/09/12 20:08:47 Successfully obtained source code and scanned for dependencies
Sending build context to Docker daemon  109.6kB
Step 1/1 : FROM hello-world
 ---> 4ab4c602aa5e
Successfully built 4ab4c602aa5e
Successfully tagged myregistry.azurecr-test.io/hello-world:yd14
2023/09/12 20:08:48 Executing step: acb_step_1
2023/09/12 20:08:48 Pushing image: myregistry.azurecr-test.io/hello-world:yd14, attempt 1
The push refers to repository [myregistry.azurecr-test.io/hello-world]
428c97da766c: Preparing
428c97da766c: Layer already exists
yd14: digest: sha256:1a6fd470b9ce10849be79e99529a88371dff60c60aab424c077007f6979b4812 size: 524
2023/09/12 20:08:55 Successfully pushed image: myregistry.azurecr-test.io/hello-world:yd14
2023/09/12 20:08:55 Step id: acb_step_0 marked as successful (elapsed time in seconds: 2.035049)
2023/09/12 20:08:55 Populating digests for step id: acb_step_0...
2023/09/12 20:08:57 Successfully populated digests for step id: acb_step_0
2023/09/12 20:08:57 Step id: acb_step_1 marked as successful (elapsed time in seconds: 6.832391)
The following dependencies were found:
- image:
    registry: myregistry.azurecr-test.io
    repository: hello-world
    tag: yd14
    digest: sha256:1a6fd470b9ce10849be79e99529a88371dff60c60aab424c077007f6979b4812
  runtime-dependency:
    registry: registry.hub.docker.com
    repository: library/hello-world
    tag: latest
    digest: sha256:0add3ace90ecb4adbf7777e9aacf18357296e799f81cabc9fde470971e499788
  git: {}


Run ID: yd14 was successful after 19s
```

For more information about automated builds on Git commit or base image update, see the build-task and base-image-update tutorial guides.

## Concepts

- Pipeline orchestration: multi-step tasks sequence build, validation, packaging, and deployment steps in a single workflow so the release process stays explicit and repeatable.
- Dependency tracking: when a base image or upstream artifact changes, the task model can react by rebuilding downstream images and preserving consistency. See [Additional Resources/ACR Tasks Overview.md](ACR%20Tasks%20overview.md).
- Image lifecycle: build, test, push, and deploy are part of one continuous delivery loop that keeps registry content consistent over time.
- Governance and traceability: tags, logs, and task history make it easier to audit what changed and identify which image version should be promoted or rolled back. See [Additional Resources/About registries, repositories, and artifacts.md](About%20registries,%20repositories,%20and%20artifacts.md).
