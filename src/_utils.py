from scipy.stats import pearsonr

def classificar_correlacao(x, y):
    """
    Calcula a correlação de Pearson e classifica o coeficiente de Pearson conforme a tabela fornecida.
    
    Paramters:
    x, y : listas ou arrays numéricos de mesma dimensão.
    
    Return:
    dicionário com:
        - 'p_value': valor do p-valor
        - 'classif_p_value': descrição qualitativa do p-valor
        - 'pearson_coef': valor de Pearson
        - 'classificacao': descrição qualitativa da Correlação
    """
    if len(x) != len(y):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    signif_alpha = 0.05

    corr, p_value = pearsonr(x, y)
    
    abs_corr = abs(corr)

    if p_value >= signif_alpha:
        classif_p_value = "Não há correlação significativa"
    else:
        classif_p_value = "Existe correlação significativa"

    
    if abs_corr <= 0.19:
        classif_pearson = "Correlação bem fraca"
    elif abs_corr <= 0.39:
        classif_pearson = "Correlação fraca"
    elif abs_corr <= 0.69:
        classif_pearson = "Correlação moderada"
    elif abs_corr <= 0.89:
        classif_pearson = "Correlação forte"
    else:
        classif_pearson = "Correlação muito forte"
    
    return {
        'p-value': float(p_value),
        'classif_p_value': classif_p_value,
        'pearson_coef': float(corr),
        'classificacao': classif_pearson
    }
