---
markdown
# 🤖 DevHelper Sischef – Projeto Final de IA para Engenharia de Software

Este repositório contém o **MVP** de um agente baseado em LLM (**Gemini**) para auxiliar desenvolvedores em tarefas como:

* Geração de **docstrings** e **explicações** de código  
* Sugestão de **melhorias** e **refatorações**  
* **Diagnóstico** de erros comuns em Python  
* (Opcional) **Geração de testes unitários** a partir de trechos de código  

A interface é feita em **Streamlit**.  
Na 2ª etapa foram adicionados scripts de **IaC** (Terraform – simulado), **Dockerfile**, **Docker Compose**, **pipeline CI/CD** (GitHub Actions) e **testes automatizados**.

---

## 🎯 Problema e MVP

* **Problema**: Código mal documentado e qualidade inconsistente dificultam manutenção e colaboração.  
* **MVP**: O usuário cola um trecho de código (e opcionalmente um erro/traceback) → o **DevHelper Sischef** gera docstrings, explicações, correções e sugestões de testes/refatorações.

---

## 🚀 Como rodar o projeto

### 1. Pré-requisitos
* Python 3.10+  
* Conta no **Google AI Studio** e uma **API Key do Gemini**  
* (Opcional) Docker + Docker Compose  
* (Opcional) Terraform 1.6+  

### 2. Configuração
Crie um arquivo `.env` na raiz (baseado no `.env.example`):

env
GEMINI_API_KEY=sua_chave_aqui
MODEL_NAME=gemini-1.5-pro


### 3. Instalar dependências

bash
pip install -r requirements.txt


### 4. Rodar localmente (Streamlit)

bash
streamlit run main.py


Acesse em [http://localhost:8501](http://localhost:8501)

---

## 🐳 Rodando com Docker

### Dockerfile

bash
docker build -t devhelper-sischef:latest .
docker run --env-file .env -p 8501:8501 devhelper-sischef:latest


### Docker Compose

bash
docker compose up --build


Acesse em [http://localhost:8501](http://localhost:8501)

---

## ☁️ Infraestrutura como Código (Terraform – simulado)

No diretório `terraform/`:

bash
cd terraform
terraform init
terraform plan -out=tfplan
terraform apply -auto-approve tfplan


> O `main.tf` é apenas um **placeholder/skeleton**.
> Arquivos incluídos:
>
> * `main.tf`: configuração inicial de Terraform
> * `variables.tf`: variáveis básicas (nome do projeto, região)
> * `readme.md`: explicação do objetivo e possibilidades futuras

---

## 🔄 CI/CD (GitHub Actions)

Pipeline em `.github/workflows/pipeline.yml`:

* Instala dependências
* Roda os testes (`pytest`)
* Executa *deploy simulado* (echo)

---

## 🧪 Testes

Testes implementados em `tests/test_main.py`:
bash
pytest -q


---

## 📂 Estrutura do projeto

```
projeto-final-ia/
├── .env.example            # modelo de variáveis
├── .env                    # sua API KEY (não versionar)
├── main.py                 # app Streamlit
├── requirements.txt
├── readme.md               # este documento
├── BRIEFING.md             # briefing preenchido
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── .devcontainer/
│   └── devcontainer.json
├── tests/
│   └── test_main.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── readme.md
└── .github/
    └── workflows/
        └── pipeline.yml
```

---

## ℹ️ Observações

* **Nunca** comite sua chave de API real.
* Os prompts foram escritos para serem **seguros e auditáveis**.
* O agente pode ser expandido para suportar **outras linguagens** e fluxos de DevOps.

---

## 📄 Licença

MIT

