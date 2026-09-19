---
title: "Tags, Layers e Manifests"
aliases:
  - Docker tagging
  - Image layers
  - Manifest digest
  - Container immutability
tags:
  - docker
  - container
  - acr
  - versioning
---

# Tags, layers e manifests

## Tag

I tag identificano versioni specifiche di un artifact all'interno di un repository. Il formato è:

```text
repository:tag
```

Esempio:

```text
inference-api:v1.2.0
```

### Caratteristiche

- Sono leggibili dall'uomo
- Possono essere multipli per lo stesso artifact
- Sono mutabili: un tag può essere spostato a un nuovo artifact
- `latest` viene usato di default quando non viene specificato un tag

## Layers

Le immagini container sono composte da layer. Ogni layer deriva da un'istruzione del Dockerfile. Installare un package o copiare file crea una nuova layer.

### Vantaggi

- Riutilizzo di layer condivise tra immagini
- Riduzione di spazio di storage
- Pull più veloci

Un esempio comune in AI è la condivisione di un layer base come `python:3.11` o una base con framework ML.

## Manifests

Il manifest descrive la struttura dell'immagine. Include i layer e la configurazione. Il manifest è identificato da un digest immutabile del tipo:

```text
sha256:abc123...
```

### Perché è importante

- Il digest non cambia dopo il push
- Garantisce la riproducibilità
- È fondamentale per deployment di produzione

## By tag vs by digest

### Tag-based addressing

```bash
docker pull myregistry.azurecr.io/inference-api:v1.2.0
```

### Digest-based addressing

```bash
docker pull myregistry.azurecr.io/inference-api@sha256:0a2e01852872580b2c2fea9380ff8d7b637d3928783c55beb3f21a6e58d5d108
```

### Decisione pratica

Usa tag per sviluppo e ambiente dinamici. Usa digest quando hai bisogno di una versione esatta e immutabile in production.

## Esempio di workflow

```bash
# build
az acr build --registry myregistry --image inference-api:v1.2.0 .

# pull by tag
Docker pull myregistry.azurecr.io/inference-api:v1.2.0

# pull by digest
Docker pull myregistry.azurecr.io/inference-api@sha256:0a2e01852872580b2c2fea9380ff8d7b637d3928783c55beb3f21a6e58d5d108
```

## Riassunto

Tag, layer e manifest sono i tre concetti centrali per capire come ACR gestisce immagini container. La combinazione corretta di tag leggibili e digest immutabili rende possibile versioning affidabile e rollback sicuri.

## Note correlate

- [[02-Registries-Repositories-Artifacts]]
- [[04-ACR-CLI-e-Tutorial]]
