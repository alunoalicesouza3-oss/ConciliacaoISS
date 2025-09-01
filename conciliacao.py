import pandas as pd

def conciliar_arquivos(df1, df2, df3):
    """
    Exemplo de conciliação: encontra divergências entre os 3 arquivos.
    Ajuste a lógica conforme seu caso real.
    """

    # Merge básico
    df_merged = df1.merge(df2, how="outer", indicator=True).merge(df3, how="outer", indicator=True)
    
    # Encontrar divergências
    divergencias = df_merged[df_merged['_merge'] != 'both']

    return divergencias
