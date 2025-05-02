# 🚗 Previsão de Preço de Carros para Entrada no Mercado Americano – RCAuto ReSearch

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange.svg) <a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

🔍 *Este projeto segue a metodologia CRISP-DM e utiliza dados públicos disponibilizados apenas para fins educacionais.*  
📊 Dataset original: [Automobile Dataset - UCI](https://archive.ics.uci.edu/dataset/10/automobile)


## 🧭 CRISP-DM METODOLOGY

### 1. 🧠 Business Understanding

No dinâmico e altamente competitivo mercado automotivo, a definição estratégica de preços para novos veículos é uma alavanca crítica para o sucesso de montadoras e suas redes de concessionárias. Uma precificação otimizada não só garante a rentabilidade e a competitividade no lançamento de novos modelos, mas também informa a estratégia de posicionamento de mercado e o desenvolvimento de produtos futuros. O desafio reside em quantificar o impacto de inúmeras características do veículo no seu valor percebido e real, além de entender como fatores relacionados a risco e potenciais custos de manutenção/reparo podem influenciar essa equação.

Com isto uma rede de consecionárias vem perdendo ***market share*** no seu último ano e a nova gerência contratou a **RC Research** para extrair insights fundamentos afim de criar um modelo de precificação do veículo.Os aprendizados servirão como base para refinar os modelos de precificação atuais da concessionária, otimizar a seleção de features para novos modelos e entender a percepção de risco associada a diferentes configurações de veículos.


**Objetivo principal**:
- Desenvolver um modelo de regressão capaz de prever o preço (`price`) de carros com base em suas características técnicas, de design, risco de seguro (`symboling`) e perdas normalizadas (`normalized-losses`).


**Problemas de negócio**:
- a) Quais características intrínsecas do veículo (ex: tamanho do motor, potência, tipo de carroceria, marca) têm o maior impacto na definição do preço inicial (price)?
- b) Como o risco atribuído (`symboling`) e as perdas normalizadas (`normalized-losses`) se relacionam com as características do veículo e, consequentemente, com o preço (`price`)? (Entender se carros com características associadas a maior risco/perdas tendiam a ser precificados de forma diferente na época).
- c) É possível construir um modelo preditivo que estime o preço ideal com 85% de acurácia?

**Hipóteses para serem testadas**:
- a) Características relacionadas à performance do veículo (ex: horsepower, engine-size) terão uma correlação positiva significativa com o price?
- b) Veículos com maior tamanho (length, width, wheel-base) tenderão a ter um price mais alto?
- c) Certas marcas (make) terão um impacto significativo no price, refletindo percepção de valor e posicionamento de mercado.
- d) Tipos de carroceria (body-style) associados a segmentos premium ou esportivos (ex: convertible, hardtop) terão preços médios (price) mais altos do que tipos de carroceria mais utilitários (ex: sedan, hatchback).
- e) O risco atribuído pelo seguro (symboling) terá alguma correlação (possivelmente negativa, indicando que carros percebidos como mais arriscados podem ser menos atraentes ou terem preços ajustados) com o price.
- f)  As perdas normalizadas (normalized-losses) terão uma correlação (possivelmente positiva, indicando que características associadas a maiores perdas podem estar presentes em carros de maior valor ou complexidade, ou talvez uma correlação negativa se indicarem problemas que depreciem o valor) com o price.
- g) Há uma relação entre características específicas do veículo (ex: tipo de tração drive-wheels, engine-location) e o symboling ou normalized-losses.
-  Um modelo de regressão linear ou baseado em árvores será capaz de predizer o price com um grau razoável de acurácia utilizando as características do veículo.
Quais características intrínsecas do veículo (ex: tamanho do motor, potência, tipo de carroceria, marca) têm o maior impacto na definição do preço inicial (price)?
- Como o risco atribuído (symboling) e as perdas normalizadas (normalized-losses) se relacionam com as características do veículo e, consequentemente, com o preço (price)? (Entender se carros com características associadas a maior risco/perdas tendiam a ser precificados de forma diferente na época).

---

### 2. 📊 Data Understanding

**Objetivo**: entender o conteúdo, a estrutura e a qualidade dos dados.


O dataset é composto por 205 registros de veículos de diversas marcas, com variáveis que incluem diversas características, sendo classificadas da seguinte forma com alguns exemplos:

**Caracteristicas:**
- **Técnicas:** `engine-size`, `horsepower`, `curb-weight`...
- **Design:** `body-style`, `num-of-doors`, `drive-wheels`.
- **Mercado:**`make`, `fuel-type`, `aspiration`
- **Alvo:** `price`


**Atividades:**
- Analisa a qualidade inicial dos dados
- Verifica valores ausentes, tipos de dados, distribuições
- Identifica valores extremos, inconsistências, duplicatas
- Verifica a estrutura dos dados
- Realiza estatísticas descritivas iniciais (describe, value_counts)
- Responder algumas questões de negócios com análise exploratória dos dados

---

### 3. 🧹 Data Preparation
**Objetivo:** Transformar os dados brutos em um formato para uso em análise exploratória e modelagem.

**Atividades:**
- Tratamento de valores ausentes;
- Substituição de valores inconsistentes
- Conversão de tipos
- Remoção de colunas irrelevantes ou redundantes
- Trata dados faltantes, padroniza formatos, remove duplicatas
- Tratamento de outliers extremos
- Combinação de múltiplas fontes
- Salvamento do dataset limpo (`data/processed/`)

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

| Tool                     | Description                        |
|------------------------ -|---------------------  -------------|
| `Python`                 | Linguagem de programação principal |
| `Pandas`                 | Manipulação de dados |
| `Seaborn` `Matplotlib`   | Visualização de dados |
| `scikit-learn`           | Treinamento e avaliação de modelos |
| `Jupyter Notebook`       | Documentação e experimentos interativos |

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

