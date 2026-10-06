## Self-check questions

### 1. 

A container image is configured to listen on port 8000. After deploying to App Service, requests to the application return connection errors. What configuration change resolves this issue?

A. Set the `WEBSITES_PORT` app setting to 8000.
B. Modify the Dockerfile to use EXPOSE 80.
C. Enable the HTTP/2 protocol in the platform settings.

> [!answer]- Reveal answer
>  A: For custom containers, App Service can automatically route traffic when the container listens on port 80 or 8080. If the container listens on a different port, WEBSITES_PORT tells App Service which port to forward HTTP requests to inside the container.

### 2. 

A document processing application writes output files during processing. After a container restart, the output files are missing. How do you configure App Service to persist these files?

A. Set `WEBSITES_ENABLE_APP_SERVICE_STORAGE` to true and write files to the `/home` directory.
B. Configure a larger container image with more disk space.
C. Enable always-on to prevent container restarts.

> [!answer]- Reveal answer
> A: This setting enables persistent storage for the /home directory. Files written to /home persist across container restarts and are shared across scaled instances.

### 3. 

A production application requires different API endpoint URLs for staging and production deployment slots. Which configuration approach ensures the staging URL doesn't swap to production during a slot swap?

A. Configure the API_ENDPOINT setting as a slot setting.
B. Store the API endpoint in the container image for each environment.
C. Use connection strings instead of app settings for the API endpoint.

> [!answer]- Reveal answer
> A: Slot settings remain with their slot during swap operations. Marking API_ENDPOINT as a slot setting ensures each slot maintains its own endpoint configuration.

### 4. 

A container starts successfully but health checks are failing, and App Service removes instances from the load balancer. The application has a `/healthz` endpoint that returns HTTP 200. What is the most likely cause?

A. The health check path in App Service is configured differently than the application's health endpoint path.
B. Health checks require HTTPS, but the container only serves HTTP.
C. The container needs more memory to handle health check requests.

> [!answer]- Reveal answer
> A: The health check path configured in App Service must match the exact path where your application responds to health requests. A mismatch like /health versus /healthz causes check failures.

### 5.  

A developer needs to verify that app settings are correctly injected into a running container. Which diagnostic tool provides this information?

A. The Kudu diagnostic console Environment page.
B. The log stream in the Azure portal.
C. The App Service metrics dashboard.

> [!answer]- Reveal answer
> A: The SCM (Kudu) Environment view (or the /Env endpoint) shows the environment variables that App Service applies to the app, including app settings and system-provided variables.

## [[Learning Path 1 - Implement container application hosting on Azure/Module 2 - Deploy containers to Azure App Service/Unit 7 - Summary|Next Unit > Summary]]