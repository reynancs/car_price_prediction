import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def load_data(filepath='data/raw/car_data.csv'):
    """
    Carrega os dados de carros do arquivo CSV.
    """
    return pd.read_csv(filepath)

def preprocess_data(df):
    """
    Realiza o pré-processamento dos dados:
    - Remove valores nulos
    - Converte tipos de dados
    - Cria novas features
    """
    # Remover valores nulos ou substituí-los
    df = df.dropna()
    
    # Exemplo de conversão de características categóricas
    # df = pd.get_dummies(df, columns=['marca', 'modelo', 'combustivel'])
    
    return df

def exploratory_analysis(df):
    """
    Realiza análise exploratória dos dados.
    """
    # Estatísticas básicas
    print(df.describe())
    
    # Matriz de correlação
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlação')
    plt.savefig('reports/figures/correlation_matrix.png')
    
    # Distribuição de preços
    plt.figure(figsize=(10, 6))
    sns.histplot(df['preco'], kde=True)
    plt.title('Distribuição de Preços')
    plt.savefig('reports/figures/price_distribution.png')
    
    # Relação entre preço e quilometragem
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='quilometragem', y='preco', data=df)
    plt.title('Preço vs Quilometragem')
    plt.savefig('reports/figures/price_vs_mileage.png')

def train_models(df, target_col='preco'):
    """
    Treina modelos de predição de preços.
    """
    # Separar features e target
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    
    # Dividir em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Treinar modelo de regressão linear
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    
    # Treinar modelo de Random Forest
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Avaliar modelos
    models = {
        'Linear Regression': lr_model,
        'Random Forest': rf_model
    }
    
    results = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results[name] = {
            'MSE': mse,
            'R2': r2
        }
        
        print(f"Modelo: {name}")
        print(f"MSE: {mse:.2f}")
        print(f"R²: {r2:.2f}")
        print("-------------------")
    
    # Salvar o melhor modelo
    best_model = rf_model  # Normalmente Random Forest tem melhor desempenho
    os.makedirs('models', exist_ok=True)
    joblib.dump(best_model, 'models/car_price_model.pkl')
    
    return models, results

def predict_price(model, car_features):
    """
    Realiza a predição de preço para um novo carro.
    """
    return model.predict([car_features])[0]

if __name__ == "__main__":
    # Exemplo de uso
    print("Iniciando análise de preços de carros...")
    
    # Carregar dados
    df = load_data()
    print(f"Dados carregados: {df.shape[0]} registros com {df.shape[1]} características")
    
    # Pré-processamento
    df_processed = preprocess_data(df)
    print(f"Dados pré-processados: {df_processed.shape[0]} registros restantes")
    
    # Análise exploratória
    exploratory_analysis(df_processed)
    print("Análise exploratória concluída. Gráficos salvos na pasta reports/figures/")
    
    # Treinamento de modelos
    models, results = train_models(df_processed)
    print("Treinamento de modelos concluído")
    
    # Exemplo de predição
    # Supondo que temos um modelo treinado:
    # modelo_carregado = joblib.load('models/car_price_model.pkl')
    # features_novo_carro = [2018, 50000, 2.0, 'gasolina']  # Ano, km, motor, combustível
    # preco_estimado = predict_price(modelo_carregado, features_novo_carro)
    # print(f"Preço estimado: R$ {preco_estimado:.2f}") 