# Pipeline ETL com Python (Requests + Pandas)

## 📌 Descrição
Projeto de pipeline ETL simples que consome dados de uma API pública, trata os dados com Pandas e gera um arquivo CSV com os dados estruturados.

## 🚀 Tecnologias usadas
- Python
- Requests
- Pandas

## Arquitetura do Pipeline
O fluxo do projeto segue o modelo ETL:

- **Extract:** Coleta de dados da API Fake Store
- **Transform:** Tratamento e estruturação dos dados com Pandas
- **Load:** Exportação dos dados tratados para CSV

## Etapas do projeto

### 1. Extract
Consumo de dados da API Fake Store:
https://fakestoreapi.com/products

### 2. Transform
- Conversão de JSON para DataFrame
- Normalização do campo `rating`
- Tratamento e organização dos dados

### 3. Load
- Salvamento dos dados tratados em arquivo CSV
- Estrutura organizada na pasta `data/processed/`

## 📊 Resultado final
Arquivo CSV gerado na pasta `data/`

## 📂 Estrutura do projeto

```
pipeline-etl-vendas/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   └── main.py
│
├── data/
│   └── processed/
│
├── requirements.txt
└── README.md
```
## 👨‍💻 Autor
  Isabelle Ferreira Neri Feitoza — Aluna da FIAP: Graduação em Ánalise e Desenvolvimento de sistemas 
  RM 573507 - Turma: 1TDSPH
  * [LinkedIn](https://www.linkedin.com/in/isabelle-ferreira-8844593ab/) | [GitHub](https://github.com/isabelleferreiraa)

## Projeto desenvolvido para prática de Engenharia de Dados com Python.