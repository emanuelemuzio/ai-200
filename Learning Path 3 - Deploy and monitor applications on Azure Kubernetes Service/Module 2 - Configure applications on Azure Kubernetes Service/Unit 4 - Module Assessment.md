## Self-check questions

### 1. 

You need to store a database connection string for your application running on AKS. The connection string contains a password and shouldn't be visible in your source code repository. Which Kubernetes resource should you use?

A. ConfigMap, because it stores configuration data
B. Secret, because it stores sensitive values and keeps credentials out of source control
C. PersistentVolumeClaim, because it provides storage for application data

> [!answer]- Reveal answer
>  B: Secrets are the correct choice for storing sensitive values like connection strings with passwords. They keep credentials out of source control and can be protected with RBAC policies.

### 2. 

Your AI application reads feature flags and service endpoints from environment variables. You want to update these settings without rebuilding your container image. How should you inject these nonsensitive values into your Pods?

A. Create a ConfigMap with the settings and reference the keys using configMapKeyRef in the Deployment
B. Store the values in a Secret and mount it as a volume
C. Hardcode the values in the Deployment manifest and update the manifest when settings change

> [!answer]- Reveal answer
> A: ConfigMaps are designed for nonsensitive configuration. Using configMapKeyRef lets you inject values as environment variables and update them without rebuilding images.

### 3. 

You create a PersistentVolumeClaim in your AKS cluster. What happens when you apply the PVC manifest?

A. You must manually create an Azure Disk in the Azure portal before the PVC can bind
B. AKS uses the specified StorageClass to automatically provision Azure storage that backs the PVC
C. The PVC remains unbound until you create a matching PersistentVolume manifest

> [!answer]- Reveal answer
> C: AKS includes preconfigured StorageClasses that dynamically provision Azure Disk or Azure Files resources when you create a PVC. No manual storage creation is required.

### 4. 

Your application needs to access API keys stored in a Kubernetes Secret. You want to make the keys available as environment variables in the container. Which field should you use in the Deployment manifest to reference the Secret?

A. valueFrom with secretKeyRef
B. Volumes with secret type
C. configMapKeyRef pointing to the Secret name

> [!answer]- Reveal answer
> A: The valueFrom field with secretKeyRef is the correct way to inject Secret values as environment variables. This resolves the Secret key at Pod start time.

### 5.  

You need to decide between mounting a ConfigMap as environment variables or as files. Your application reads a JSON configuration file at startup. Which approach should you choose?

A. Mount the ConfigMap as environment variables because all applications can read environment variables
B. Mount the ConfigMap as files using a volume so the JSON file appears on disk where the application expects it
C. Store the JSON content in a Secret and use secretKeyRef to inject it as an environment variable

> [!answer]- Reveal answer
> B: When an application expects configuration files on disk, mount the ConfigMap as a volume. Each key becomes a file in the mount directory.

## [[Unit 5 - Summary | Next Unit > Summary]]