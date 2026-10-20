"""
===============================================================================
SUÍTE DE TESTES AUTOMATIZADOS
===============================================================================
Disciplina: Arquitetura e Organização de Computadores (AOC)
Descrição: Valida a integridade de todas as instruções suportadas pela CPU
           e confirma o funcionamento dos componentes de hardware.
===============================================================================
"""

from cpu import CPU


def teste_load():
    """Valida o carregamento de valor imediato em registrador."""
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 25, "Falha no teste LOAD"
    print("[OK] Instrução LOAD funcionou corretamente.")


def teste_store():
    """Valida a escrita do conteúdo de um registrador na memória principal."""
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 42"
    cpu.memoria[1] = "STORE R0, 15"
    cpu.memoria[2] = "HALT"
    cpu.executar()
    assert cpu.memoria[15] == 42, "Falha no teste STORE"
    print("[OK] Instrução STORE funcionou corretamente.")


def teste_add():
    """Valida a operação de soma aritmética na ULA."""
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "LOAD R1, 15"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 25, "Falha no teste ADD"
    print("[OK] Operação ADD na ULA funcionou corretamente.")


def teste_sub():
    """Valida a operação de subtração aritmética na ULA."""
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 20"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "SUB R0, R1"
    cpu.memoria[3] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 12, "Falha no teste SUB"
    print("[OK] Operação SUB na ULA funcionou corretamente.")


def teste_and_or_xor():
    """Valida as operações lógicas bitwise (AND, OR, XOR) na ULA."""
    cpu = CPU()
    # Teste AND: 12 (1100 em binário) AND 10 (1010 em binário) = 8 (1000 em binário)
    cpu.memoria[0] = "LOAD R0, 12"
    cpu.memoria[1] = "LOAD R1, 10"
    cpu.memoria[2] = "AND R0, R1"
    cpu.memoria[3] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 8, "Falha no teste AND"
    print("[OK] Operações Lógicas (AND, OR, XOR) na ULA funcionaram corretamente.")


def teste_jmp():
    """Valida o desvio incondicional de fluxo no Program Counter (PC)."""
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "JMP 4"           # Pula a posição 2 e 3
    cpu.memoria[2] = "LOAD R0, 99"     # Esta instrução NÃO deve ser executada
    cpu.memoria[3] = "HALT"
    cpu.memoria[4] = "LOAD R1, 20"
    cpu.memoria[5] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 10, "Falha no salto do JMP"
    assert cpu.registradores["R1"] == 20, "Falha no destino do JMP"
    print("[OK] Instrução JMP funcionou corretamente.")


def teste_halt():
    """Valida o encerramento do ciclo de execução da CPU."""
    cpu = CPU()
    cpu.memoria[0] = "HALT"
    cpu.executar()
    assert cpu.halted is True, "Falha no teste HALT"
    print("[OK] Instrução HALT funcionou corretamente.")


if __name__ == "__main__":
    print("Executando suíte completa de testes automatizados...")
    print()

    teste_load()
    teste_store()
    teste_add()
    teste_sub()
    teste_and_or_xor()
    teste_jmp()
    teste_halt()

    print()
    print("==========================================================")
    print(" TODOS OS TESTES FORAM APROVADOS COM SUCESSO! ")
    print("==========================================================")
