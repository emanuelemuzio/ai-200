An Azure App Service sidecar  is an auxiliary container that runs in the same environment as the main Linux app container. Sidecars add capabilities such as local AI inference, telemetry collection, or caching without placing those capabilities in the main image. The shared environment creates useful operational coupling, but the pattern isn't a substitute for an independently hosted service. 

## Understand the sidecar execution model

A sidecar-enabled app has one main container and can have up to nine sidecar containers. App Service manages all containers as one application, but each process retains its own image, startup command, and container-specific configuration. The container roles determine external routing rather than process importance.

The main container uses `isMain: true`. App Service sends external HTTP traffic only to that container. Every sidecar uses `isMain: false` and remains reachable from the other containers through the shared network namespace.

Sidecars follow the main app's lifecycle:

- App Service starts and stops the containers as part of the same app.
- When the app scales out, each new instance contains the main container and all configured sidecars.
- When the app scales in, App Service removes the complete set of containers on an instance.
- A configuration deployment can update a sidecar image independently of the main image, but the new configuration still belongs to the same app.

This lifecycle is useful for the conversational AI scenario. Every API instance receives a local model server, so the API doesn't need to discover a remote endpoint or handle a different number of model-server replicas.

## Evaluate coupling and isolation

The sidecar pattern works best when a supporting component has the same availability and scale requirements as the main app. Local communication also avoids a separate network endpoint, which can reduce latency and simplify authentication between the processes. Those benefits need to outweigh the reduced isolation.

Sidecars share the main app's network namespace and environment. A sidecar can reach the ports exposed by other containers on `localhost`. You should run only trusted images because the containers share this trust boundary.

All containers on an app instance also consume capacity from the same App Service plan. The plan doesn't scale the model server independently from the API. A model server that consumes most of the available memory can affect API responsiveness even when the API uses little memory.

For an AI application, a sidecar is a strong fit when:

- Every main-app instance needs exactly one local supporting process.
- The supporting process starts, stops, deploys, and scales with the main app.
- Local communication provides a meaningful latency or data-boundary benefit.
- The combined CPU and memory requirements fit the selected App Service plan.
- The main app and sidecar images come from trusted sources.

A separately deployed service is usually a better fit when:

- Several applications share one model endpoint or cache.
- Model serving needs GPU hardware or a scaling policy that differs from the API.
- The component requires a separate network or security boundary.
- The component must remain available while the main app restarts or scales to zero.
- Failures in the supporting component shouldn't consume resources from the main app.

For example, a compact language model used by one internal API might fit a sidecar. A large model that serves many applications and needs independent capacity is better hosted on a service designed for model inference.

## Compare configuration models

Sidecar-enabled apps use the `sitecontainers` configuration model. Each container is represented by a `Microsoft.Web/sites/sitecontainers` resource, and the app has `LinuxFxVersion=sitecontainers`. This model differs from the classic custom-container configuration.

Classic single-container apps identify an image with a value such as `DOCKER|<image>`. Older multi-container configurations can use Docker Compose. Sidecar-enabled configuration replaces those image definitions with container resources that identify the main role, sidecar roles, target ports, image authentication, and volume mounts.

You can convert an eligible existing Linux custom-container app to sidecar configuration. Conversion changes how App Service stores container settings. Some classic app settings, including `WEBSITES_PORT` and `DOCKER_REGISTRY_SERVER_*`, don't configure sidecar-enabled containers. You should plan the replacement settings before converting a production app.

The following role fragments show the central distinction between the containers:

```JSON
{
  "name": "main-api",
  "properties": {
    "isMain": true
  }
}
```

```JSON
{
  "name": "model-server",
  "properties": {
    "isMain": false
  }
}
```

Exactly one container should have `isMain` set to `true`. The remaining container resources should set the property to `false`.

## Plan capacity and failure boundaries

Capacity planning starts with the combined requirements of the complete app instance. You need to include the main API, model server, and any other sidecars in the estimate. Peak request concurrency and model initialization can raise usage above steady-state measurements.

You can start with the following process:

1. Measure the memory required to load the model before sending traffic.
2. Measure CPU and memory for the main app and sidecar under representative concurrent requests.
3. Include startup overlap because App Service can start the containers during deployment or scale-out.
4. Select an App Service plan that has capacity for the combined peak plus operational headroom.
5. Review App Service metrics after deployment and test scale-out behavior.

App Service plan SKUs, capacity, and pricing change regularly. The correct plan depends on the workload's measured resource use and availability requirements. 

If measurement shows that model serving dominates capacity or requires a different scaling rule, separate the model server from the web app. The additional service boundary introduces network and operational work, but it prevents the model process from competing directly with the API.

## [[Unit 3 - Configure main and sidecar containers | Next Unit > Configure main and sidecar containers]]