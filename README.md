# 🔒 Secreton

Secreton is a **secure, CLI-based note vault** written in Python.  
It lets you create, encrypt, and manage notes directly from your terminal — with plans to support **FastAPI backend, PostgreSQL, Docker, and DevOps workflows** for full remote access.

---

## ✨ Features

- 📝 Take notes directly from the CLI  
- 🔐 End-to-end encryption (client-side encryption, server stores only ciphertext)  
- 🔑 Secure authentication (Argon2 password hashing + JWT)  
- 🌍 Access from anywhere via SSH tunneling  
- 🗄️ PostgreSQL backend with FastAPI API  
- 🐳 Dockerized for easy deployment (Azure / any cloud)  
- 🛡️ Security-first design (no plaintext leaves your machine)

---

## 🏗️ Tech Stack

- **Python 3.12**  
- **CLI**: [Typer](https://typer.tiangolo.com/) + [Rich](https://rich.readthedocs.io/)  
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn]  
- **Database**: PostgreSQL + SQLAlchemy + Alembic  
- **Crypto**: `argon2-cffi`, `cryptography` (Fernet)  
- **Auth**: JWT (via python-jose) + optional TOTP (pyotp)  
- **DevOps**: Docker, docker-compose, GitHub Actions CI/CD  
- **Deployment**: Azure VM + Caddy (TLS)  

---

## 📂 Project Structure

```bash
secreton/
│── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # FastAPI entry
│   │   ├── models.py       # SQLAlchemy models
│   │   ├── schemas.py      # Pydantic schemas
│   │   ├── db.py           # DB session setup
│   │   ├── auth.py         # JWT, password hashing
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── notes.py
│   │   └── security.py     # crypto utils
│   ├── alembic/            # migrations
│   ├── Dockerfile
│   └── requirements.txt
│
│── cli/
│   ├── __init__.py
│   ├── main.py             # Typer CLI entry
│   ├── api.py              # talk to FastAPI
│   ├── crypto.py           # local encryption/decryption
│   └── config.py           # API URL, config
│
│── docker-compose.yml
│── README.md

