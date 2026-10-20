"""
TESTES COMPLETOS
AOC 2026.2
"""

from cpu import CPU


def teste_load():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 25
    print("[OK] LOAD")


def teste_store():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 42"
    cpu.memoria[1] = "STORE R0, 15"
    cpu.memoria[2] = "HALT"
    cpu.executar()
    assert cpu.memoria[15] == 42
    print("[OK] STORE")


def teste_add():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "LOAD R1, 15"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 25
    print("[OK] ADD")


def teste_sub():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 20"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "SUB R0, R1"
    cpu.memoria[3] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 12
    print("[OK] SUB")


def teste_and_or_xor():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 12"
    cpu.memoria[1] = "LOAD R1, 10"
    cpu.memoria[2] = "AND R0, R1"
    cpu.memoria[3] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 8
    print("[OK] AND, OR, XOR")


def teste_jmp():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "JMP 4"
    cpu.memoria[2] = "LOAD R0, 99"
    cpu.memoria[3] = "HALT"
    cpu.memoria[4] = "LOAD R1, 20"
    cpu.memoria[5] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 10
    assert cpu.registradores["R1"] == 20
    print("[OK] JMP")


def teste_halt():
    cpu = CPU()
    cpu.memoria[0] = "HALT"
    cpu.executar()
    assert cpu.halted is True
    print("[OK] HALT")


if __name__ == "__main__":
    print("Executando todos os testes...")
    print()

    teste_load()
    teste_store()
    teste_add()
    teste_sub()
    teste_and_or_xor()
    teste_jmp()
    teste_halt()

    print()
    print("Todos os testes foram aprovados com sucesso!")