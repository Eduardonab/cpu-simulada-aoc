"""
===============================================================================
EXECUÇÃO E DEMONSTRAÇÃO PASSO A PASSO
===============================================================================
Disciplina: Arquitetura e Organização de Computadores (AOC)
Descrição: Carrega um programa de exemplo de 8 instruções na memória simulada
           e executa a CPU exibindo a evolução do estado do processador.
===============================================================================
"""

from cpu import CPU

# Instancia a CPU simulada
cpu = CPU()

# =============================================================================
# PROGRAMA DE TESTE (Mínimo de 8 instruções exigido no trabalho)
# =============================================================================
# 0: LOAD R0, 20  -> R0 recebe 20
# 1: LOAD R1, 10  -> R1 recebe 10
# 2: ADD R0, R1   -> R0 = 20 + 10 = 30
# 3: LOAD R2, 5   -> R2 recebe 5
# 4: SUB R0, R2   -> R0 = 30 - 5 = 25
# 5: STORE R0, 14 -> Guarda o valor de R0 (25) na posição 14 da memória
# 6: STORE R1, 15 -> Guarda o valor de R1 (10) na posição 15 da memória
# 7: HALT         -> Encerra o processamento
# =============================================================================

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

# Inicia o loop do ciclo de instruções
cpu.executar()

print()
print("======================================")
print("     RESULTADO FINAL DA MEMÓRIA")
print("======================================")
print(f"Memória [14]: {cpu.memoria[14]} (Esperado: 25)")
print(f"Memória [15]: {cpu.memoria[15]} (Esperado: 10)")
