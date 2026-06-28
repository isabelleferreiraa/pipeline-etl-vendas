# 🚀 Pipeline ETL com Python

![Python](https://img.shields.io/badge/Python-3.11-blue)
![ETL](https://img.shields.io/badge/ETL-Pipeline-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

```
Pipeline ETL desenvolvido em Python para extração, transformação e carregamento de dados da Fake Store API, utilizando Pandas e PostgreSQL.
```

## 📌 Sobre o projeto

Este projeto implementa um pipeline ETL (Extract, Transform and Load) utilizando Python.

Os dados são extraídos da Fake Store API, transformados com Pandas, validados e armazenados tanto em arquivo CSV quanto em um banco de dados PostgreSQL.

O projeto foi desenvolvido com foco em boas práticas de Engenharia de Dados, incluindo:

- Arquitetura modular em camadas (Extract, Transform, Load)
- Configuração via variáveis de ambiente (.env)
- Logging estruturado
- Validação de dados antes da carga
- Separação entre dados brutos (raw) e tratados (processed)
- Tratamento de exceções

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| **Python 3** | Linguagem principal do projeto |
| **Pandas** | Transformação e tratamento dos dados |
| **Requests** | Consumo da API |
| **PostgreSQL** | Armazenamento dos dados |
| **Psycopg2** | Conexão entre Python e PostgreSQL |
| **Python-dotenv** | Gerenciamento das variáveis de ambiente |
| **Logging** | Registro de logs da execução |
| **Git** | Controle de versão |
| **Docker** | Containerização do ambiente |

## 🏗️ Arquitetura do Pipeline

```mermaid
flowchart TD
    A[Fake Store API] --> B[Extract]
    B --> C[Transform - Pandas]
    C --> D[Validate]
    D --> E[Load]
    E --> F[(PostgreSQL)]
    E --> G[CSV]
```
## 🐳 Docker

```mermaid
flowchart TD
    A[Dockerfile] --> B[Build Image]
    B --> C[Docker Image: pipeline-etl]
    C --> D[Container Running]
    D --> E[Executa Pipeline ETL]
    E --> F[(PostgreSQL)]
    E --> G[CSV Files]
```

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/isabelleferreiraa/pipeline-etl-vendas.git
```

### 2. Entre na pasta do projeto

```bash
cd pipeline-etl-vendas
```

### 3. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
.venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto utilizando o `.env.example` como modelo:

```env
DB_HOST=localhost
DB_NAME=etl_vendas
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_PORT=5432
```

### 7. Execute o pipeline

```bash
python src/main.py
```

## 📂 Estrutura do projeto

```text
pipeline-etl-vendas/
│
├── data/
│   ├── raw/
│   │   └── produtos_raw.json
│   │
│   └── processed/
│       └── produtos_tratados.csv
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   ├── logger.py
│   └── main.py
│
├── tests/
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## 📊 Resultado

Após a execução do pipeline são gerados:

- JSON bruto: `data/raw/produtos_raw.json`
- CSV tratado: `data/processed/produtos_tratados.csv`
- Logs da execução: `logs/pipeline.log`
- Dados inseridos no PostgreSQL

## 🎯 Objetivo do projeto

Aplicar conceitos de Engenharia de Dados, incluindo ingestão de dados via API, processamento com Pandas, validação, persistência em banco de dados e organização em um pipeline ETL modular.

## 💡 Aprendizados

- Construção de pipelines ETL do zero
- Integração Python + PostgreSQL
- Manipulação e limpeza de dados com Pandas
- Estruturação de projeto em camadas
- Boas práticas de engenharia de software aplicadas à dados

## 🔮 Melhorias futuras

- Testes automatizados com Pytest
- GitHub Actions
- Orquestração com Apache Airflow
- Integração com Data Warehouse

## 👨‍💻 Autora

 **Isabelle Ferreira Neri Feitoza**
  
 Estudante de Análise e Desenvolvimento de Sistemas — FIAP  
 RM 573507 | Turma: 1TDSPH

  * [LinkedIn](https://www.linkedin.com/in/isabelle-ferreira-8844593ab/) | [GitHub](https://github.com/isabelleferreiraa)


