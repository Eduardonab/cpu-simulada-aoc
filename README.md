# CPU Simulada — 8 Bits
**Disciplina:** Arquitetura e Organização de Computadores (AOC) — 2026.2  
**Instituição:** Universidade Federal do Ceará (UFC) — Campus Sobral  
**Professor:** Wendley S. Silva  
**Aluno:** Eduardo Duarte de Andrade
**Matrícula:** 578525

---

## 1. Visão Geral do Projeto

Este projeto consiste na implementação de uma CPU simulada em Python desenvolvida para fins didáticos. O objetivo é demonstrar a integração dos principais componentes de hardware de um processador: **Registradores**, **Memória**, **Unidade Lógica e Aritmética (ULA)** e **Unidade de Controle**, operando sob o ciclo clássico de execução **Fetch → Decode → Execute**.

---

## 2. Arquitetura da CPU

A CPU foi projetada com uma arquitetura simplificada de 8 bits:

| Componente | Especificação |
| :--- | :--- |
| **Tamanho dos Dados** | 8 bits (valores limitados de 0 a 255 / `0x00` a `0xFF`) |
| **Registradores Gerais** | `R0`, `R1`, `R2` e `R3` (8 bits cada) |
| **Ponteiro de Instrução** | `PC` (Program Counter) |
| **Memória Principal** | 16 posições (`0` a `15`), armazenando instruções ou dados |
| **ULA** | Suporte a `ADD`, `SUB`, `AND`, `OR` e `XOR` |
| **Ciclo de Execução** | Fetch (Busca) → Decode (Decodificação) → Execute (Execução) |

---

## 3. Conjunto de Instruções (ISA)

A CPU suporta 9 instruções fundamentais:

| Instrução | Exemplo | Descrição |
| :--- | :--- | :--- |
| **LOAD** | `LOAD R0, 5` | Carrega um valor imediato no registrador (`R0 <- 5`) |
| **STORE** | `STORE R0, 15` | Grava o valor do registrador na posição de memória (`MEM[15] <- R0`) |
| **ADD** | `ADD R0, R1` | Soma registrador de origem ao destino (`R0 <- R0 + R1`) |
| **SUB** | `SUB R0, R1` | Subtrai registrador de origem do destino (`R0 <- R0 - R1`) |
| **AND** | `AND R0, R1` | Operação lógica E bit a bit (`R0 <- R0 AND R1`) |
| **OR** | `OR R0, R1` | Operação lógica OU bit a bit (`R0 <- R0 OR R1`) |
| **XOR** | `XOR R0, R1` | Operação lógica OU Exclusivo bit a bit (`R0 <- R0 XOR R1`) |
| **JMP** | `JMP 8` | Desvio incondicional no fluxo (`PC <- 8`) |
| **HALT** | `HALT` | Interrompe a execução da CPU |

---

## 4. Estrutura do Projeto

```text
.
├── ula.py        # Implementação das operações aritméticas e lógicas da ULA
├── cpu.py        # Classe principal da CPU, decodificador e ciclo Fetch-Decode-Execute
├── main.py       # Demonstração e execução passo a passo do programa principal
├── testes.py     # Suíte de testes unitários automatizados
└── README.md     # Documentação do projeto
