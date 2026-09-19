---
title: "Best Practices"
aliases:
  - Governance
  - ACR best practices
  - Recommendations
tags:
  - azure
  - acr
  - best-practices
  - operations
---

# Best practices

## Principi guida

Seguire queste pratiche aiuta a mantenere un registry ordinato ed efficiente.

### 1. Usa namespace

Organizza i repository per team, ambiente o progetto. Esempio:

```text
production/inference-api
staging/inference-api
ml-team/model-server
```

Questo semplifica il controllo degli accessi e la governance.

### 2. Pianifica la struttura dei repository

Raggruppa le immagini in base a:

- ownership del team
- ambiente di deployment
- ciclo di vita dell'applicazione
- dipendenze tecniche

### 3. Abilita geo-replication

Per distribuzione globale, ripeti le immagini nelle regioni dove vengono eseguite le applicazioni. Riduce latenza e aumenta affidabilità.

### 4. Monitora lo storage

Le immagini container accumulano spazio rapidamente. Applica policy di retention e rimuovi artifact non etichettati o obsoleti.

### 5. Preferisci digest per produzione

Quando serve un deployment deterministico e riproducibile, usa digest invece di tag mutable.

## Checklist operativa

- [ ] Repository ben organizzati per ambiente
- [ ] Tag coerenti e documentati
- [ ] Policy di accesso definite
- [ ] Geo-replication abilitata se necessario
- [ ] Policy di retention attive
- [ ] Deployment production basati su digest

## Riassunto

Una registrazione ben strutturata riduce rischio, aumenta tracciabilità e rende i rollout più facili da gestire. Per AI workloads, la governance di immagini è parte integrante della sicurezza e della qualità del deployment.

## Note correlate

- [[04-ACR-CLI-e-Tutorial]]
- [[06-Resources]]
