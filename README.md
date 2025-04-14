# 🚗 Car Price Prediction Analysis – RCAuto

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange.svg) <a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

> **Objetivo do Projeto:** 
> Desenvolver um modelo preditivo para estimar o preço de automóveis com base em variáveis técnicas e comerciais, auxiliando a empresa  Geely Auto a entender os fatores que influenciam o preço de carros no mercado americano.


🔍 *Este projeto segue a metodologia CRISP-DM e utiliza dados públicos disponibilizados apenas para fins educacionais.*  
📊 Dataset original: [Automobile Dataset - UCI](https://archive.ics.uci.edu/dataset/10/automobile)


## 🧭 Metodologia - CRISP-DM

### 1. 🧠 Business Understanding

RCAuto, uma montadora chinesa, deseja entrar no mercado americano. Para isso, contratou uma consultoria com o objetivo de entender os **fatores que impactam o preço dos carros** nos Estados Unidos, visto que podem diferir substancialmente do mercado chinês.

**Perguntas-chave:**
- Quais variáveis influenciam significativamente o preço de um carro?
- Como essas variáveis se correlacionam com o preço?
- É possível construir um modelo preditivo preciso baseado nessas variáveis?

---

### 2. 📊 Data Understanding

O dataset é composto por mais de **2.000 registros** de veículos de diversas marcas, com variáveis que incluem:

- **Atributos Técnicos:** `engine size`, `horsepower`, `curb weight`, `highway-mpg`
- **Características Comerciais:** `make`, `body-style`, `fuel-type`, `drive-wheels`
- **Variável Alvo:** `price`

**Principais Ações:**
- Análise de tipos de variáveis (numéricas, categóricas)
- Análise de outliers e valores ausentes
- Distribuições e correlações iniciais

---

### 3. 🧹 Data Preparation

**Tarefas:**

- Exclusão de colunas irrelevantes ou com alta cardinalidade
- Remoção de valores nulos ou ausentes
- Remoção de outliers 
- Transformações (encoding de variáveis categóricas)
- Normalização de features para melhorar a performance do modelo
- Criação de novas variáveis (ex: relação `price/horsepower`)

---

### 4. 🧠 Modeling

**Modelos Testados:**

**Métricas de Avaliação:**

---

### 5. ✅ Evaluation


---

### 6. 🚀 Deployment / Application

Este projeto pode ser adaptado para:

- **Estimativa de preços em plataformas de venda de veículos**
- **Análises de precificação por montadoras e concessionárias**
- **Apoio à estratégia de entrada em novos mercados**

---

## 🛠️ Tools and Technologies

| Tool | Description |
|------------|-----------|
| `Python` | Linguagem de programação principal |
| `Pandas` | Manipulação de dados |
| `Seaborn` & `Matplotlib` | Visualização de dados |
| `scikit-learn` | Treinamento e avaliação de modelos |
| `Jupyter Notebook` | Documentação e experimentos interativos |

---

### 📁 Project Structure

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         src and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```
---

## 📌 Lessons Learned


- Entendimento aprofundado de regressão linear e métricas
- Transformações eficientes em variáveis categóricas
- Importância da engenharia de variáveis e preparação de dados
- Como comunicar resultados para fins estratégicos

---

## 📬 Contact

- 🌐 [LinkedIn](https://www.linkedin.com/in/renan-cardoso-8323b151/)
- 📧 renan.cs.sants@gmail.com

---

### ⚠️ Disclaimer
> Os dados são públicos e utilizados apenas para fins educacionais. Nenhuma inferência real deve ser assumida com base neste estudo.


--------

