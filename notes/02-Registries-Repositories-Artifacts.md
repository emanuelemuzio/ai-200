---
title: "Registries, Repositories e Artifacts"
aliases:
  - Registry hierarchy
  - Repository
  - Artifact
  - ACR hierarchy
tags:
  - azure
  - container-registry
  - acr
  - architecture
---

# Registries, repositories e artifacts

## Introduzione

Comprendere la struttura di Azure Container Registry aiuta a progettare una strategia di archiviazione efficace per applicazioni AI. Questo modulo spiega la gerarchia del registro e mostra come manifest, layers e digest consentano uno storage e un recupero efficienti dei container artifact.

## Understand Azure Container Registry

Azure Container Registry è un servizio di registry Docker privato e gestito che archivia e distribuisce immagini container e artifact correlati. A differenza dei registri pubblici come Docker Hub, ACR offre un controllo diretto sugli accessi, la geo-replication per distribuzione globale e l'integrazione con servizi Azure come Azure Kubernetes Service e Azure Container Apps.

### Funzionalità principali

- **Storage privato**: manteneri immagini di serving, servizi di preprocessing e API di inferenza in un ambiente Azure sicuro
- **Geo-replication**: distribuire immagini vicino alle regioni di deployment per ridurre latenza
- **Integrazione**: collegarsi direttamente ad Azure Kubernetes Service, Azure Container Apps e Azure App Service
- **Formati supportati**: immagini Docker, chart Helm e artifact OCI in un unico registro

### Livelli di servizio

ACR supporta i livelli Basic, Standard e Premium. La maggior parte dei flussi di lavoro di sviluppo funziona in modo simile in tutti i livelli. Funzionalità come content trust e private endpoint richiedono il tier Premium.

## Gerarchia del registro

ACR utilizza una struttura a tre livelli per organizzare i contenuti.

### 1. Registry

Il registry è la risorsa principale che ospita tutti i contenuti container. Ogni registro ha un URL univoco del login server nel formato `registry-name.azurecr.io`.

Esempio:

```text
contosoinference.azurecr.io
```

Il registry contiene più repository e fornisce autenticazione, access control e gestione delle policy.

### 2. Repository

Un repository è una collezione di immagini container con lo stesso nome ma tag diversi. Ad esempio:

```text
inference-api
```

Contiene tutte le versioni della stessa immagine. Ogni volta che fai push di una nuova versione con un tag diverso, questa viene aggiunta al repository.

### 3. Artifact

Un artifact è l'immagine container effettiva o altro contenuto archiviato in un repository. Ogni artifact ha tag, layer e un manifest che descrive la sua struttura.

## Tag, layers e manifests

### Tag

I tag identificano versioni specifiche di un artifact all'interno di un repository. Il formato è:

```text
repository:tag
```

Esempio:

```text
inference-api:v1.2.0
```

Un'immagine può avere più tag che puntano allo stesso artifact. Tag come `latest`, `stable` e una versione specifica sono molto comuni.

### Layers

Le immagini container sono composte da uno o più layer. Ogni layer corrisponde a una istruzione del Dockerfile. Layer condivisi tra immagini consentono deduplica e riduzione di spazio di storage.

### Manifests

Ogni artifact ha un manifest che elenca i layer e la configurazione. Il manifest è identificato da un digest SHA-256 immutabile.

## Indirizzamento degli artifact

ACR supporta due modalità di indirizzamento: per tag e per digest.

### Per tag

Formato:

```text
registry/repository:tag
```

Esempio:

```bash
docker pull myregistry.azurecr.io/inference-api:v1.2.0
docker push myregistry.azurecr.io/inference-api:v1.2.0
```

### Per digest

Formato:

```text
registry/repository@sha256:hash
```

Esempio:

```bash
docker pull myregistry.azurecr.io/inference-api@sha256:0a2e01852872580b2c2fea9380ff8d7b637d3928783c55beb3f21a6e58d5d108
```

I digest garantiscono immutabilità e riproducibilità.

## Best practice di organizzazione

- Usa namespace per team, ambiente o progetto
- Piana repository per environment o funzionalità
- Abilita geo-replication per distribuzione globale
- Monitora lo storage e applica policy di retention

## Note correlate

- [[00-Index]]
- [[01-Introduzione]]
- [[03-Tags-Layers-Manifests]]
