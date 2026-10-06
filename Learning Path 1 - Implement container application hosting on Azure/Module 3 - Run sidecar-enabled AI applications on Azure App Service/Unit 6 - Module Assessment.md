## Self-check questions

### 1. 

A team runs one compact language model for each instance of an internal API. The model must start, stop, and scale with the API. Low-latency local calls are also important. Which hosting approach best fits these requirements?

A. Deploy the model as a separate shared service with its own scaling policy.
B. Run the model in an App Service sidecar beside the main API container.
C. Add the model process to the main API container image.

> [!answer]- Reveal answer
>  B.

### 2. 

A sidecar-enabled app contains an API and a model server. External requests must reach only the API, while the API calls the model server locally. How should the container roles be configured?

A. Set `isMain: true` on the API and `isMain: false` on the model server.
B. Set `isMain: true` on both containers and assign different target ports.
C. Set `isMain: false` on both containers and configure `WEBSITES_PORT` for the API.

> [!answer]- Reveal answer
> A.  

### 3. 

A production web app must pull private main and sidecar images from an Azure Container Registry that uses RBAC Registry Permissions. The app can't store registry passwords. Which configuration meets the requirement?

A. Enable the registry admin account and store its credentials in `DOCKER_REGISTRY_SERVER_*` app settings.
B. Make the repositories public and omit authentication from each site container definition.
C. Assign a managed identity to the app, grant it `AcrPull`, and reference the identity in each private site container definition.

> [!answer]- Reveal answer
> C.  

### 4. 

A model sidecar produces artifacts that must remain durable independently of the web app lifecycle and serve as a system of record for other applications. Where should the application store the artifacts?

A. Store the artifacts under the web app's shared `/home` directory.
B. Use Azure Blob Storage or Azure Files as the durable storage boundary.
C. Write the artifacts to each container's writable image layer.

> [!answer]- Reveal answer
> B.  

### 5.  

The main API receives a connection-refused error when it calls `http://localhost:11434`. Which diagnostic step most directly tests the failing boundary?

A. Compare the API endpoint port with the sidecar target port, then inspect whether the sidecar process listens on that port.
B. Scale the App Service plan before inspecting the container configuration.
C. Change the API endpoint from `localhost` to the sidecar container name.

> [!answer]- Reveal answer
> A.  

## [[Learning Path 1 - Implement container application hosting on Azure/Module 3 - Run sidecar-enabled AI applications on Azure App Service/Unit 7 - Summary|Unit 7 - Summary | Next Unit > Summary]]
 