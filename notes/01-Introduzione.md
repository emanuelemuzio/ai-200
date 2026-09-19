---
title: "Introduzione"
aliases:
  - Overview
  - AI workloads
  - ACR introduction
tags:
  - ai
  - azure
  - container-registry
  - introduction
---

# Introduzione

## Contesto

AI applications require a secure, scalable location to store container images that serve inference APIs, data pipelines, and backend services. This module guides you through using Azure Container Registry (ACR) to store, build, and manage container images for AI solutions on Azure.

Immagina di essere uno sviluppatore che costruisce un servizio di inferenza AI in tempo reale. Il tuo team mantiene diverse immagini container: un'API di serving del modello, un servizio di preprocessing e un sidecar di monitoraggio. Ogni immagine richiede aggiornamenti mentre i modelli migliorano e le dipendenze cambiano.

## Problema da risolvere

Attualmente il team compila le immagini localmente e le carica da workstation degli sviluppatori, causando build incoerenti e versioning poco chiaro. Il cliente richiede deployment affidabili, versioni tracciabili e la possibilità di fare rollback a release precedenti.

## Necessità

Serve un registro centralizzato che supporti build basate sul cloud, mantenga tag coerenti e integri i flussi di deployment.

## Obiettivi di apprendimento

Dopo aver completato questo modulo sarai in grado di:

- Spiegare come Azure Container Registry organizza le immagini tramite registries, repositories e artifact
- Compilare e gestire immagini container nel cloud usando ACR Tasks
- Implementare strategie di tagging e versioning per deployment affidabili
- Usare Azure CLI per gestire immagini e eseguire quick tasks di ACR

## Riassunto

ACR fornisce un archivio privato, gestito e integrato con Azure per distribuzione sicura di container e artifact. Per i carichi di lavoro AI, questo significa più controllo, maggiore tracciabilità e deployment più prevedibili.

## Note correlate

- [[00-Index]]
- [[02-Registries-Repositories-Artifacts]]
- [[03-Tags-Layers-Manifests]]
