## Self-check questions

### 1. 

Your AI inference function experiences cold start latency of several seconds because it loads large ML libraries and initializes connections to Azure AI services. You need to reduce latency for the first request while keeping costs low during idle periods. Which approach should you use?

A. Use the Flex Consumption plan with always-ready instances configured for the function
B. Use the Consumption plan with increased function timeout settings
C. Use the Premium plan with pre-warmed workers disabled

> [!answer]- Reveal answer
>  A.

### 2. 

You're setting up a local development environment for Azure Functions. Your function app uses a Service Bus queue trigger, but you notice the trigger doesn't fire when you run the function locally. What is the most likely cause?

A. The AzureWebJobsStorage setting in local.settings.json isn't configured with a valid storage connection
B. The function app needs to be deployed to Azure before Service Bus triggers can be tested
C. Visual Studio Code doesn't support debugging Service Bus-triggered functions

> [!answer]- Reveal answer
> A.  

### 3. 

Your function processes documents asynchronously. An HTTP endpoint accepts requests, writes messages to a Service Bus queue, and a separate queue-triggered function performs the processing. You want to configure the queue trigger to process one message at a time per instance to maximize CPU and memory available for each document. Which configuration should you use?

A. Set maxConcurrentCalls to 1 in the serviceBus section of host.json
B. Set batchSize to 1 in the serviceBus section of host.json
C. Set maxDequeueCount to 1 on the Service Bus queue resource

> [!answer]- Reveal answer
> A.

### 4. 

You need to store an API key for an Azure AI service in your function app's configuration. The security team requires that the key be stored in Azure Key Vault and rotated regularly without requiring application redeployment. Which approach meets these requirements?

A. Create a Key Vault reference in the application setting using a versionless secret URI
B. Create a Key Vault reference in the application setting using a versioned secret URI
C. Store the API key directly in the application setting with encryption enabled

> [!answer]- Reveal answer
> A. 

### 5.

You're configuring identity-based connections for a Service Bus trigger in your function app. You've enabled a system-assigned managed identity and set ServiceBusConnection__fullyQualifiedNamespace to your namespace. The function fails to receive messages. What role assignment is missing?

A. Azure Service Bus Data Receiver on the Service Bus namespace
B. Azure Service Bus Data Owner on the Service Bus namespace
C. Key Vault Secrets User on the Service Bus namespace

> [!answer]- Reveal answer
> A. 