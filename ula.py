"""
===============================================================================
MÓDULO DA UNIDADE LÓGICA E ARITMÉTICA (ULA)
===============================================================================
Disciplina: Arquitetura e Organização de Computadores (AOC)
Descrição: Responsável por realizar operações aritméticas e lógicas básicas
           sobre operandos de 8 bits.
===============================================================================
"""

def limitar_8bits(valor):
    return valor & 0xFF


def ula(operacao, a, b=0):
"""
    Executa a operação especificada na ULA utilizando dois operandos de 8 bits.
    
    Parâmetros:
      - operacao (str): Nome do comando ('ADD', 'SUB', 'AND', 'OR', 'XOR').
      - a (int): Operando de entrada A (normalmente valor do registrador de destino).
      - b (int): Operando de entrada B (normalmente valor do registrador de origem).
      
    Retorna:
      - int: Resultado da operação ajustado para 8 bits (0 a 255).
    """

# Trunca os operandos de entrada para garantir que cheguem à ULA com 8 bits
    a = limitar_8bits(a)
    b = limitar_8bits(b)

# -------------------------------------------------------------------------
# OPERAÇÕES ARITMÉTICAS
# -------------------------------------------------------------------------


    if operacao == "ADD":          
# Soma aritmética dos dois operandos
        resultado = a+b

    elif operacao == "SUB":
# Subtração aritmética (A - B)
        resultado = a-b

# -------------------------------------------------------------------------
# OPERAÇÕES LÓGICAS BIT A BIT (BITWISE)
# -------------------------------------------------------------------------
    elif operacao == "AND":
# Operação lógica E bit a bit
        resultado = a & b

    elif operacao == "OR":
# Operação lógica OU bit a bit
        resultado = a | b

    elif operacao == "XOR":
# Tratamento de instrução não suportada pela ULA
        resultado = a ^ b

    else:
# Tratamento de instrução não suportada pela ULA
        raise ValueError(f"Operação inválida: {operacao}")
# Retorna o resultado truncado para 8 bits
    return limitar_8bits(resultado)
