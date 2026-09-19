---
title: "ACR CLI e Tutorial"
aliases:
  - Azure CLI
  - ACR Quick Tasks
  - Example commands
tags:
  - azure-cli
  - acr
  - tutorial
  - docker
---

# ACR CLI e tutorial

## Panoramica

Azure Container Registry può essere gestito sia tramite Azure CLI sia tramite Docker. Questa sezione raccoglie i comandi principali e gli esempi pratici di push, pull e build.

## Comandi principali

### Login

```bash
az login
az acr login --name myregistry
```

### Creare un registry

```bash
az acr create --resource-group my-rg --name myregistry --sku Basic
```

### Push di un'immagine

```bash
docker tag my-image:latest myregistry.azurecr.io/inference-api:v1.2.0
docker push myregistry.azurecr.io/inference-api:v1.2.0
```

### Pull di un'immagine

```bash
docker pull myregistry.azurecr.io/inference-api:v1.2.0
```

### Listare le immagini in un repository

```bash
az acr repository list --name myregistry --output table
```

### Elencare i tag di un repository

```bash
az acr repository show-tags --name myregistry --repository inference-api --output table
```

## ACR Tasks

ACR Tasks consente l'esecuzione di build nel cloud in modo integrato con il registry.

```bash
az acr build --registry myregistry --image inference-api:v1.2.0 .
```

Questo comando costruisce l'immagine nel cloud invece che sul workstation locale, aiutando a standardizzare i processi di build e release.

## Esempio completo

```bash
# 1. creare il registry
az acr create --resource-group my-rg --name myregistry --sku Basic

# 2. autenticarsi
az acr login --name myregistry

# 3. build locale
docker build -t inference-api:latest .

# 4. taggare e push
docker tag inference-api:latest myregistry.azurecr.io/inference-api:v1.2.0
docker push myregistry.azurecr.io/inference-api:v1.2.0

# 5. pull a verifica
docker pull myregistry.azurecr.io/inference-api:v1.2.0
```

## Quando usare ACR Tasks

Usa ACR Tasks quando:

- vuoi build nel cloud invece che in locale
- vuoi standardizzare processi CI/CD
- vuoi automatizzare build e scansione delle immagini
- vuoi evitare workstation non omogenee

## Riassunto

ACR combina repository, tag, digest e task di build in un modello coerente per rollout di container affidabili. L'uso di Azure CLI e Docker rende facile integrare ACR in applicazioni AI e pipeline di deployment.

## Note correlate

- [[03-Tags-Layers-Manifests]]
- [[05-Best-Practices]]
