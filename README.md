# 🚗 Previsão de Preço de Carros para Entrada no Mercado Americano – RCAuto ReSearch

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange.svg) <a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

🔍 *Este projeto segue a metodologia CRISP-DM e utiliza dados públicos disponibilizados apenas para fins educacionais.*  
📊 Dataset original: [Automobile Dataset - UCI](https://archive.ics.uci.edu/dataset/10/automobile)


## 🧭 Metodologia - CRISP-DM

### 1. 🧠 Business Understanding

A GT Auto é uma montadora chinesa que deseja entrar no mercado americano. Para isso, contratou uma consultoria com o objetivo de entender os **fatores que impactam o preço dos carros** nos Estados Unidos, visto que podem diferir substancialmente do mercado chinês.

**Objetivo principal**:
- Desenvolver um modelo preditivo que explique o preço dos carros com base em características técnicas e de design.

**Problemas de negócio**:
- Quais variáveis mais impactam no preço?
- Como ajustar as especificações dos carros para se posicionar competitivamente?
- Como essas variáveis se correlacionam com o preço?
- É possível construir um modelo preditivo preciso baseado nessas variáveis?

---

### 2. 📊 Data Understanding

O dataset é composto por mais de **2.000 registros** de veículos de diversas marcas, com variáveis que incluem:

- **Atributos Técnicos:** `engine size`, `horsepower`, `curb weight`, `highway-mpg`
- **Características Comerciais:** `make`, `body-style`, `fuel-type`, `drive-wheels`
- **Variável Alvo:** `price`

**Insights esperados**:
- Correlação entre variáveis como [`engine_size`, `curb_weight`, `horsepower`] vs `price`
- Detectar outliers e valores inconsistentes

**Principais Ações:**
- Análise Exploratória do Dataset: estatísticas descritivas; tipos de variáveis (numéricas, categóricas)
- Distribuição dos Dados 
- Identificação de Outliers, inconsistências evalores ausentes

---

### 3. 🧹 Data Preparation

**Tarefas:**

- Exclusão de colunas irrelevantes
- Remoção de valores nulos ou ausentes
- Remoção de outliers 
- Transformações (encoding de variáveis categóricas)
- Normalização de features para melhorar a performance do modelo
- Criação de novas variáveis (ex: relação `price/horsepower`)
- Separação do dataset de treinamento e teste

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

### 📚  Data Catalog

This data dictionary provides a structured description of the variables used in the car price prediction dataset.

| Variable Name       | Role                | Type Variable | Description |
|---------------------|---------------------|----------------|-------------|
| symboling           | Feature             | Categorical    | Risk factor assigned by insurance (ranging from -3 to 3; higher means more risky) |
| normalized-losses   | Feature             | Continuous     | Relative average loss paid by insurance; indicates vehicle damage risk |
| make                | Feature             | Categorical    | Manufacturer brand of the car |
| fuel-type           | Feature             | Categorical    | Type of fuel the car uses (`gas` or `diesel`) |
| aspiration          | Feature             | Categorical    | Engine type: standard or turbocharged |
| num-of-doors        | Feature             | Categorical    | Number of doors in the vehicle |
| body-style          | Feature             | Categorical    | Body type of the car (e.g., sedan, hatchback) |
| drive-wheels        | Feature             | Categorical    | Type of drivetrain (front, rear, or 4-wheel drive) |
| engine-location     | Feature             | Categorical    | Location of the engine (front or rear) |
| wheel-base          | Feature             | Continuous     | Distance between front and rear wheels (affects stability) |
| length              | Feature             | Continuous     | Overall length of the vehicle in inches |
| width               | Feature             | Continuous     | Width of the vehicle in inches |
| height              | Feature             | Continuous     | Height of the vehicle in inches |
| curb-weight         | Feature             | Continuous     | Total weight of the car without passengers or cargo |
| engine-type         | Feature             | Categorical    | Engine configuration (e.g., OHV, OHC, DOHC) |
| num-of-cylinders    | Feature             | Categorical    | Number of cylinders in the engine |
| engine-size         | Feature             | Continuous     | Engine displacement in cubic centimeters |
| fuel-system         | Feature             | Categorical    | Type of fuel injection system |
| bore                | Feature             | Continuous     | Diameter of each cylinder in inches |
| stroke              | Feature             | Continuous     | Distance the piston travels within the cylinder (in inches) |
| compression-ratio   | Feature             | Continuous     | Ratio of engine cylinder volume to combustion chamber volume |
| horsepower          | Feature             | Continuous     | Engine power output measured in horsepower |
| peak-rpm            | Feature             | Continuous     | Engine speed at which maximum horsepower is generated |
| city-mpg            | Feature             | Continuous     | Fuel consumption in city driving (miles per gallon) |
| highway-mpg         | Feature             | Continuous     | Fuel consumption on highways (miles per gallon) |
| price               | Target              | Continuous     | Selling price of the car in USD |

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

