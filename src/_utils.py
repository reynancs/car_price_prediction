from scipy.stats import pearsonr

def classificar_correlacao(x, y):
    """
    Calcula a correlação de Pearson e classifica conforme a tabela fornecida.
    
    Parâmetros:
    x, y : listas ou arrays numéricos de mesma dimensão.
    
    Retorno:
    dicionário com:
        - 'correlacao': valor de Pearson
        - 'p_valor': valor do p-valor
        - 'classificacao': descrição qualitativa da correlação
    """
    if len(x) != len(y):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    corr, p_value = pearsonr(x, y)
    
    abs_corr = abs(corr)
    
    if abs_corr <= 0.19:
        classificacao = "Uma correlação bem fraca"
    elif abs_corr <= 0.39:
        classificacao = "Uma correlação fraca"
    elif abs_corr <= 0.69:
        classificacao = "Uma correlação moderada"
    elif abs_corr <= 0.89:
        classificacao = "Uma correlação forte"
    else:
        classificacao = "Uma correlação muito forte"
    
    return {
        'correlacao': corr,
        'p_valor': p_value,
        'classificacao': classificacao
    }
