## Self-check questions

### 1. 

You're deploying an AI document-processing API that must access a private endpoint and share logs and networking settings across multiple container apps. Which Azure Container Apps resource provides that shared boundary?

A. A Container Apps environment
B. A Container Apps revision
C. A replica

> [!answer]- Reveal answer
>  A: A Container Apps environment is the shared boundary that groups container apps for networking and observability integration, which helps you manage shared settings for a solution.

### 2. 

You want a consistent, source-controlled deployment for a container app so that configuration is reviewed like code. Which approach best supports that goal?

A. Use `az containerapp create --yaml` and `az containerapp update --yaml` with a YAML file stored in source control 
B. Use `az containerapp update --set-env-vars` for all changes without maintaining a configuration file
C. Rely on image tags and redeploy with `az containerapp update --image` to apply environment-specific configuration

> [!answer]- Reveal answer
> A: Using YAML definitions lets you store configuration in source control and apply it consistently across environments using CLI commands.  

### 3. 

Your container app needs an API key for an embeddings provider. You don't want to store the value in a YAML file. Which pattern should you use?

A. Store the secret in Container Apps secrets and reference it from an environment variable
B. Add the API key as plain text in the YAML file under `env:`
C. Bake the API key into the container image

> [!answer]- Reveal answer
> A: This pattern keeps secret values out of source control while still making them available to the running container through a referenced environment variable.

### 4. 

You updated a container app and want to confirm the new configuration is running in production. Which command helps you see the versioned change that Container Apps created?

A. Run `az containerapp revision list`
B. Run `az containerapp registry list`
C. Run `az containerapp secret list`

> [!answer]- Reveal answer
> A: Container Apps uses revisions to version configuration changes. Listing revisions helps you verify which revision is active after an update.

### 5.  

A container app fails to start after you update the image. You need fast feedback to diagnose the issue. Which command is the best first step?

A. Run `az containerapp logs show`
B. Run `az containerapp revision list`
C. Run `az containerapp replica list`

> [!answer]- Reveal answer
> A: Container logs provide immediate signals such as startup errors, missing environment variables, or authentication failures.


## [[Unit 8 - Summary|Next Unit > Summary]]
