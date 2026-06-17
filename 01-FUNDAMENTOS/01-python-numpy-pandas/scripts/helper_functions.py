# ==========================================
# ARQUIVO: helper_functions.py
# ==========================================
import numpy as np  # Passo 1A: Importar o NumPy dentro do script também!

def filtrar_valores_altos(vendas):
    """
    Esta é uma Docstring (comentário profissional).
    Objetivo: Receber um array de vendas e filtrar o que passou de 5000.
    Input (Entrada): vendas -> um array NumPy.
    Output (Saída): Um novo array filtrado.
    """
    
    # Passo 1B: Criamos a máscara booleana (Aula 2)
    mascara = vendas > 5000
    
    # Passo 1C: Aplicamos a máscara para extrair os valores reais
    vendas_filtradas = vendas[mascara]
    
    # Passo 1D: O 'return' joga o resultado para fora da função
    return vendas_filtradas