"""
MAIN — Demonstração do código-base
AOC 2026.2

Este programa utiliza somente LOAD, JMP e HALT,
que já estão implementados no código-base.

Depois de implementar as demais instruções, substitua
o programa de teste por um programa mais completo.
"""

from cpu import CPU


cpu = CPU()

# ==========================================
# PROGRAMA DE TESTE
# ==========================================
#
# A instrução JMP faz a CPU pular da posição 1
# para a posição 4.
#
# Portanto, LOAD R0, 99 nunca será executado.
#
# Resultado esperado:
# R0 = 5
# R1 = 8
#

cpu.memoria[0] = "LOAD R0, 20"
cpu.memoria[1] = "LOAD R1, 10"
cpu.memoria[2] = "ADD R0, R1"
cpu.memoria[3] = "LOAD R2, 5"
cpu.memoria[4] = "SUB R0, R2"
cpu.memoria[5] = "STORE R0, 14"
cpu.memoria[6] = "STORE R1, 15"
cpu.memoria[7] = "HALT"


print("======================================")
print("       CPU SIMULADA — 8 BITS")
print("======================================")

cpu.executar()

print()
print("======================================")
print("RESULTADO FINAL DA MEMÓRIA")
print("======================================")
print(f"Memória [14]: {cpu.memoria[14]}")
print(f"Memória [15]: {cpu.memoria[15]}")
