<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1B2A4A,100:2563EB&height=200&section=header&text=NexusCloud&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=One%20Platform.%20Every%20Cloud.%20Zero%20Waste.&descAlignY=58&descSize=20&descColor=93C5FD&animation=fadeIn" width="100%"/>

<br/>

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Redis](https://img.shields.io/badge/Redis-7+-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io)
[![GCP](https://img.shields.io/badge/GCP-Cloud%20Run-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://cloud.google.com/run)

<br/>

[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red?style=flat-square)](https://github.com/nexuscloud-dev)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange?style=flat-square)]()

</div>

---

<div align="center">

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   Your AWS + GCP + Azure + R2 + Oracle + B2 — unified.       ║
║   Smart-routed. Zero egress. One API. One dashboard.          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

</div>

---

## 🌩️ What is NexusCloud?

**NexusCloud** is a **Bring-Your-Own-Cloud (BYOC)** multi-cloud storage orchestration platform. Connect your existing cloud accounts — AWS S3, Google Cloud Storage, Azure Blob, Cloudflare R2, Backblaze B2, Oracle Cloud, IBM Cloud — and interact with all of them through a **single unified API and dashboard**.

> You already have **70+ GB of permanently free storage** sitting idle across your cloud accounts. NexusCloud makes it one virtual disk.

---

## ⚡ The Problem We Solve

```
Without NexusCloud                    With NexusCloud
─────────────────────                 ───────────────────────────
aws s3 cp file.txt s3://bucket        POST /api/v1/files/upload
gcloud storage cp file.txt gs://b     → Smart Router picks best cloud
az storage blob upload ...            → File goes directly to your cloud
rclone copy file.txt r2:bucket        → One endpoint. Always.

5 CLIs. 5 credential sets.            One API. Zero friction.
5 consoles. Manual cost tracking.     Auto-routed to cheapest provider.
```

---

## 🧠 How the Smart Router Works

```
                    ┌─────────────────────────────┐
                    │       Upload Request         │
                    │  filename: video.mp4         │
                    │  size: 4.2 GB                │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │        Smart Router          │
                    │                             │
                    │  Score each connected cloud: │
                    │  ┌─────────────────────────┐│
                    │  │ Free Quota Left   40%   ││
                    │  │ Egress Cost       30%   ││
                    │  │ Tier Permanence   20%   ││
                    │  │ File-to-Quota Fit 10%   ││
                    │  └─────────────────────────┘│
                    └──────────────┬──────────────┘
                                   │
          ┌────────────┬───────────┼───────────┬────────────┐
          │            │           │           │            │
       ┌──▼──┐      ┌──▼──┐    ┌──▼──┐    ┌──▼──┐      ┌──▼──┐
       │ R2  │      │ GCP │    │ AWS │    │ B2  │      │ OCI │
       │ ⭐  │      │     │    │     │    │ ⭐  │      │ ⭐  │
       │$0/GB│      │$.12 │    │$.09 │    │$0/GB│      │$0/GB│
       └─────┘      └─────┘    └─────┘    └─────┘      └─────┘
          ▲
          │ Selected — 9.8 GB free, zero egress
```

---

## 🆓 Free Tier Pool Per User

| Provider | Always-Free Storage | Egress Cost | Expires? |
|---|---|---|---|
| ☁️ Cloudflare R2 | **10 GB** | **$0.00/GB** | Never |
| 🟠 Oracle Cloud | **20 GB** | **$0.00/GB** | Never |
| 🔵 Backblaze B2 | **10 GB** | **$0.00/GB** (via CF) | Never |
| 🟢 GCP Cloud Storage | **5 GB** | $0.12/GB | Never |
| 🔵 IBM Cloud | **25 GB** | Partial | Never |
| 🟡 AWS S3 | 5 GB | $0.09/GB | 12 months |
| 🔷 Azure Blob | 5 GB | $0.087/GB | 12 months |
| | **Total: 70+ GB** | **Near zero** | **Permanent** |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   PRESENTATION LAYER                    │
│          React 18 + Vite + TanStack Query               │
│              Hosted on Cloudflare Pages                 │
└───────────────────────┬─────────────────────────────────┘
                        │  HTTPS
┌───────────────────────▼─────────────────────────────────┐
│               ORCHESTRATION CORE (FastAPI)              │
│                   GCP Cloud Run                         │
│                                                         │
│  ┌──────────┐  ┌──────────────┐  ┌───────────────────┐ │
│  │   Auth   │  │ Smart Router │  │   Quota Engine    │ │
│  │  Service │  │  (Core IP)   │  │  (Redis cached)   │ │
│  └──────────┘  └──────────────┘  └───────────────────┘ │
│                                                         │
│  ┌─────────────────────┐  ┌──────────────────────────┐ │
│  │  Presigned URL Svc  │  │    Metadata Service      │ │
│  │  (zero data touch)  │  │    (PostgreSQL)          │ │
│  └─────────────────────┘  └──────────────────────────┘ │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│                  PERSISTENCE LAYER                      │
│  PostgreSQL (metadata) │ Redis (quota cache) │ Vault    │
└─────────────────────────────────────────────────────────┘
                        │
          ┌─────────────┼──────────────┐
          │             │              │
    ┌─────▼────┐  ┌─────▼────┐  ┌────▼─────┐
    │ User's   │  │ User's   │  │ User's   │  ...
    │  AWS S3  │  │   GCP    │  │    R2    │
    └──────────┘  └──────────┘  └──────────┘
         YOUR DATA STAYS IN YOUR CLOUDS
```

> **Key insight:** Files travel directly between the user and their cloud via presigned URLs. NexusCloud never stores, proxies, or touches file content. Our infrastructure cost is nearly fixed regardless of users' storage volume.

---

## 🔐 RLaaS — Rate Limiter as a Service

NexusCloud is protected by our own **custom-built rate limiting microservice** — published as a standalone Maven package.

```
Client Request
      │
      ▼
┌─────────────────────────────────────┐
│           RLaaS Microservice        │
│           (Java 21 + Spring Boot)   │
│                                     │
│  POST /check                        │
│  { key, limit, window, algorithm }  │
│                                     │
│  ┌─────────────┬──────────────────┐ │
│  │ Token       │ Sliding Window   │ │
│  │ Bucket      │ Counter          │ │  ← All 5 algorithms
│  ├─────────────┼──────────────────┤ │
│  │ Fixed       │ Sliding Window   │ │
│  │ Window      │ Log              │ │
│  └─────────────┴──────────────────┘ │
│                                     │
│  → Redis distributed state store    │
└─────────────────────────────────────┘
      │
      ▼
{ allowed: true, remaining: 47, reset_at: 1720000060 }
```

| Endpoint | Algorithm | Limit |
|---|---|---|
| `POST /auth/login` | Sliding Window Counter | 10 req/min per IP |
| `POST /auth/register` | Fixed Window | 5 req/min per IP |
| `POST /files/upload` | Token Bucket | 30 req/min per user |
| `GET /files` | Fixed Window | 60 req/min per user |
| `POST /connections` | Fixed Window | 5 req/min per user |

---

## 🚀 Quick Start

### Prerequisites
```bash
# Required
docker & docker compose
python 3.12+
uv (package manager)
node 18+ (for frontend)
```

### 1. Clone & Setup
```bash
git clone https://github.com/nexuscloud-dev/nexuscloud-backend
cd nexuscloud-backend

# Install dependencies
uv venv && source .venv/bin/activate  # Linux/Mac
uv add -r requirements.txt
```

### 2. Environment Setup
```bash
cp .env.example .env

# Generate required keys
python -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32))"
python -c "from cryptography.fernet import Fernet; print('ENCRYPTION_KEY=' + Fernet.generate_key().decode())"

# Paste both values into .env
nano .env
```

### 3. Start Infrastructure
```bash
docker compose up -d
# Starts PostgreSQL + Redis
```

### 4. Run Migrations
```bash
uv run alembic upgrade head
```

### 5. Start the Server
```bash
uv run uvicorn app.main:app --reload --port 8000
```

### 6. Open API Docs
```
http://localhost:8000/docs
```

---

## 📁 Project Structure

```
nexuscloud/
├── app/
│   ├── api/v1/routes/
│   │   ├── auth.py          # Register, login, refresh, /me
│   │   ├── connections.py   # Connect/disconnect cloud accounts
│   │   ├── files.py         # Upload, download, delete
│   │   └── quota.py         # Unified quota summary
│   ├── core/
│   │   ├── config.py        # Centralised settings (pydantic)
│   │   ├── security.py      # JWT + bcrypt
│   │   ├── deps.py          # FastAPI dependencies
│   │   └── vault.py         # AES-256-GCM credential encryption
│   ├── db/
│   │   ├── base.py          # SQLAlchemy DeclarativeBase
│   │   ├── session.py       # Async engine + session factory
│   │   └── registry.py      # Model registration (no circular imports)
│   ├── models/              # PostgreSQL table definitions
│   │   ├── user.py
│   │   ├── connection.py
│   │   ├── file_record.py
│   │   ├── quota.py
│   │   └── audit.py
│   ├── services/
│   │   ├── router.py        # Smart Router (core IP)
│   │   ├── vault.py         # Credential encrypt/decrypt
│   │   ├── quota_engine.py  # Quota polling + Redis cache
│   │   └── providers/
│   │       ├── base.py      # Abstract provider interface
│   │       ├── gcp.py       # Google Cloud Storage SDK
│   │       ├── r2.py        # Cloudflare R2 (boto3)
│   │       ├── aws.py       # AWS S3 (boto3)
│   │       ├── azure.py     # Azure Blob Storage
│   │       ├── oracle.py    # Oracle OCI
│   │       └── b2.py        # Backblaze B2
│   ├── workers/
│   │   ├── tasks.py         # Celery tasks (quota polling)
│   │   └── scheduler.py     # Celery beat schedule
│   └── main.py              # FastAPI app entry point
├── alembic/                 # Database migrations
├── tests/                   # Pytest test suite
├── docs/                    # Provider setup guides
├── .env.example
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Reason |
|---|---|---|
| **Backend API** | FastAPI 0.115+ | Async-first, auto OpenAPI docs, 2-3x faster than Django |
| **Language** | Python 3.12 | Best multi-cloud SDK coverage (boto3, GCS, Azure) |
| **Database** | PostgreSQL 16 | ACID compliance, UUID, JSONB for metadata |
| **Cache** | Redis 7 | Sub-ms quota reads, Celery broker, rate limit state |
| **Secrets** | HashiCorp Vault | AES-256-GCM, audit log on every credential access |
| **Frontend** | React 18 + Vite | Fast HMR, TanStack Query, Tailwind CSS |
| **Hosting** | GCP Cloud Run | Scale to zero, $0 idle cost, author-proven stack |
| **Frontend CDN** | Cloudflare Pages | Free, global, instant deploys |
| **CI/CD** | GitHub Actions | Auto test + deploy on push to main |
| **Rate Limiting** | RLaaS (Java 21) | Custom-built, 5 algorithms, Maven published |
| **Task Queue** | Celery + Redis | Nightly quota polling, background sync |

</div>

---

## 📡 API Reference

```
AUTH
  POST   /api/v1/auth/register     Create account
  POST   /api/v1/auth/login        Get JWT tokens
  POST   /api/v1/auth/refresh      Rotate access token
  GET    /api/v1/auth/me           Current user info

CLOUD CONNECTIONS
  POST   /api/v1/connections       Connect a cloud account
  GET    /api/v1/connections       List connected accounts + quota
  DELETE /api/v1/connections/{id}  Disconnect + wipe credentials

FILES
  POST   /api/v1/files/upload          Get smart-routed presigned upload URL
  POST   /api/v1/files/{id}/confirm    Confirm upload success
  GET    /api/v1/files                 List files (paginated)
  GET    /api/v1/files/{id}            Get presigned download URL
  DELETE /api/v1/files/{id}            Delete from cloud + metadata

QUOTA
  GET    /api/v1/quota/summary     Unified free pool across all providers
```

---

## 💰 Pricing

| Tier | Price | Clouds | Storage Managed |
|---|---|---|---|
| **Free** | ₹0/mo | 2 connections | 5 GB |
| **Starter** | ₹249/mo | All 7 providers | 50 GB |
| **Pro** | ₹749/mo | Unlimited | Unlimited + file splitting |
| **Team** | ₹2,499/mo | Unlimited | Unlimited + 10 seats |

> Infrastructure cost: ~₹1,000/month fixed. At 200 paying users: **97% gross margin**.

---

## ⚖️ Legal & Compliance

NexusCloud operates as a **software orchestration layer** — not a cloud reseller.

- ✅ Users connect **their own** cloud accounts
- ✅ Data stays in **user-owned** infrastructure
- ✅ NexusCloud never touches file content (presigned URL architecture)
- ✅ Legally identical to rclone, MultCloud, odrive — all ToS-compliant
- ✅ Credentials encrypted AES-256-GCM in HashiCorp Vault
- ✅ Scoped IAM only — no admin keys ever accepted
- ✅ One account per provider enforced — no free-tier multiplication

---

## 👥 Team

<div align="center">

| | Member | Role |
|---|---|---|
| 🔴 | **Prabhusiddarth AV** | Project Lead · Backend Core · Smart Router · RLaaS · DevOps |
| 🔴 | **Mahibala** | Cloud SDKs · File Operations · Connections UI |
| 🟡 | **Lenin** | Quota Engine · Background Workers · Files UI |
| 🟡 | **Kavii** | API Polish · Oracle & B2 Providers · Auth UI |

*Sri Shakthi Institute of Engineering and Technology, Coimbatore — B.Tech IT, Batch 2028*

</div>

---

## 🤝 Contributing

```bash
# Fork the repo
# Create your feature branch
git checkout -b feat/your-feature

# Commit your changes
git commit -m "feat: add your feature"

# Push and open a PR to dev branch
git push origin feat/your-feature
```

> All PRs must target the `dev` branch. GitHub Actions will run tests automatically.

---

## 📄 License

```
Copyright 2026 NexusCloud Dev Team

Licensed under the Apache License, Version 2.0.
You may not use this file except in compliance with the License.
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2563EB,100:1B2A4A&height=120&section=footer&animation=fadeIn" width="100%"/>

**Built with 🔥 by the NexusCloud team — SIET Coimbatore**

[![GitHub](https://img.shields.io/badge/GitHub-nexuscloud--dev-181717?style=for-the-badge&logo=github)](https://github.com/nexuscloud-dev)

*If this project helped you, drop a ⭐ — it means everything to a student team.*

</div>
