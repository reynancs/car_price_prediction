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

O dataset é composto por 205 registros de veículos de diversas marcas, com variáveis que incluem:

- **Características Técnicas:** `engine size`, `horsepower`, `curb weight`, `highway-mpg`
- **Características Comerciais:** `make`, `body-style`, `fuel-type`, `drive-wheels`
- **Variável Alvo:** `price`

**Insights esperados**:
- Correlação entre variáveis como [`engine_size`, `curb_weight`, `horsepower`] vs `price`
- Detectar outliers e valores inconsistentes

**Principais Ações:**
- Análise Exploratória do Dataset: estatísticas descritivas; tipos de variáveis (numéricas, categóricas)
- Distribuição dos Dados;
- Identificação de Outliers, inconsistências e valores ausentes

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

| Nome da Variável     | Função              | Tipo de Variável  | Descrição                                                                            |
|----------------------|---------------------|-------------------|--------------------------------------------------------------------------------------|
| symboling            | Atributo            | Categorica        | Fator de risco atribuído pelo seguro (varia de -3 a 3; quanto maior, mais arriscado) |
| normalized-losses    | Atributo            | Numerica          | Perda média relativa paga pelo seguro; indica o risco de dano do veículo |
| make                 | Atributo            | Categorica        | Marca do fabricante do carro |
| fuel-type            | Atributo            | Categorica        | Tipo de combustível usado (gasolina ou diesel) |
| aspiration           | Atributo            | Categorica        | Tipo de motor: padrão ou turbo |
| num-of-doors         | Atributo            | Categorica        | Número de portas do veículo |
| body-style           | Atributo            | Categorica        | Tipo de carroceria do carro (ex.: sedã, hatchback) |
| drive-wheels         | Atributo            | Categorica        | Tipo de tração (dianteira, traseira ou 4x4) |
| engine-location      | Atributo            | Categórica        | Localização do motor (frontal ou traseira) |
| wheel-base           | Atributo            | Numerica          | Distância entre os eixos dianteiro e traseiro (afeta a estabilidade) |
| length               | Atributo            | Numerica          | Comprimento total do veículo em polegadas |
| width                | Atributo            | Numerica          | Largura do veículo em polegadas |
| height               | Atributo            | Numerica          | Altura do veículo em polegadas |
| curb-weight          | Atributo            | Numerica          | Peso total do carro sem passageiros ou carga (kg) |
| engine-type          | Atributo            | Categorica        | Configuração do motor (ex.: OHV, OHC, DOHC) |
| num-of-cylinders     | Atributo            | Categorica        | Número de cilindros do motor |
| engine-size          | Atributo            | Numerica          | Deslocamento do motor em centímetros cúbicos |
| fuel-system          | Atributo            | Categorica        | Tipo de sistema de injeção de combustível |
| bore                 | Atributo            | Numerica          | Diâmetro de cada cilindro em polegadas |
| stroke               | Atributo            | Numerica          | Distância que o pistão percorre dentro do cilindro (em polegadas) |
| compression-ratio    | Atributo            | Numerica          | Relação entre o volume do cilindro do motor e a câmara de combustão |
| horsepower           | Atributo            | Numerica          | Potência do motor medida em cavalos de força (hp) |
| peak-rpm             | Atributo            | Numerica          | Rotação do motor na qual a potência máxima é gerada |
| city-mpg             | Atributo            | Numerica          | Consumo de combustível na cidade (milhas por galão - mpg) |
| highway-mpg          | Atributo            | Numerica          | Consumo de combustível na estrada (milhas por galão - mpg) |
| price                | Alvo                | Numerica          | Preço de venda do carro em dólares (USD) |

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

