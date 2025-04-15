from pathlib import Path
import json

# Estrutura básica do notebook com células organizadas pelas etapas do CRISP-DM
notebook_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🧠 CRISP-DM Project Template\n",
            "Structured Data Science project using the CRISP-DM methodology."
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 1. Business Understanding\n",
            "- Describe the business objective\n",
            "- Define the success criteria\n",
            "- Identify stakeholders"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": ["# Business Understanding code or notes (if applicable)"],
        "execution_count": None,
        "outputs": []
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 2. Data Understanding\n",
            "- Load initial dataset\n",
            "- Explore variables and data types\n",
            "- Visualize initial trends"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Import libraries\n",
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns"
        ],
        "execution_count": None,
        "outputs": []
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": ["# Load and preview dataset\n", "# df = pd.read_csv('path_to_dataset.csv')\n", "# df.head()"],
        "execution_count": None,
        "outputs": []
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 3. Data Preparation\n",
            "- Clean missing values\n",
            "- Feature selection & engineering\n",
            "- Encode categorical data"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": ["# Data cleaning and preparation code here"],
        "execution_count": None,
        "outputs": []
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 4. Modeling\n",
            "- Train/test split\n",
            "- Model training and testing\n",
            "- Hyperparameter tuning"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": ["# Modeling code here (e.g., LinearRegression, DecisionTreeClassifier, etc.)"],
        "execution_count": None,
        "outputs": []
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 5. Evaluation\n",
            "- Evaluate model performance\n",
            "- Compare with baseline or other models\n",
            "- Visualize results"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": ["# Evaluation code here (e.g., R², accuracy, confusion matrix, etc.)"],
        "execution_count": None,
        "outputs": []
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 6. Deployment / Insights\n",
            "- Export model or results\n",
            "- Share insights with stakeholders\n",
            "- Suggest business actions"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": ["# Export model or present final conclusions here"],
        "execution_count": None,
        "outputs": []
    }
]

# Criação do notebook com a estrutura básica
notebook_structure = {
    "cells": notebook_cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.x"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

# Salvar como .ipynb
notebook_path = Path("crispdm_template.ipynb")
with notebook_path.open("w", encoding="utf-8") as f:
    json.dump(notebook_structure, f, indent=2)

notebook_path
