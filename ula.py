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
    a = limitar_8bits(a)
    b = limitar_8bits(b)

    if operacao == "ADD":
        resultado = a+b

    elif operacao == "SUB":
        resultado = a-b

    elif operacao == "AND":
        resultado = a & b

    elif operacao == "OR":
        resultado = a | b

    elif operacao == "XOR":
        resultado = a ^ b

    else:
        raise ValueError(f"Operação inválida: {operacao}")

    return limitar_8bits(resultado)
