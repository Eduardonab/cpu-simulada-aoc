"""
===============================================================================
MÓDULO PRINCIPAL DA CPU SIMULADA (8 BITS)
===============================================================================
Disciplina: Arquitetura e Organização de Computadores (AOC)
Descrição: Define a estrutura do processador, contendo o banco de registradores,
           a memória principal, o Program Counter (PC) e a Unidade de Controle
           responsável pelo ciclo Fetch -> Decode -> Execute.
===============================================================================
"""

from ula import ula, limitar_8bits


class CPU:

    def __init__(self):
        """
        Inicializa o estado físico e lógico da CPU:
          - Banco de 4 Registradores Gerais (R0, R1, R2, R3) de 8 bits.
          - Memória principal com 16 posições de 8 bits (inicializadas a zero).
          - Program Counter (PC) apontando para o endereço inicial (0).
          - Signal flag 'halted' para controle de encerramento do ciclo.
        """
        # Banco de Registradores de uso geral
        self.registradores = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }

        # Memória principal de 16 posições (suporta dados ou instruções)
        self.memoria = [0] * 16

        # Program Counter (PC) — Aponta para a instrução em execução
        self.pc = 0

        # Flag de interrupção (indica se a CPU executou HALT)
        self.halted = False

    def executar_instrucao(self, instrucao):
        """
        Fase de DECODIFICAÇÃO (Decode) e EXECUÇÃO (Execute):
          1. Trata a string da instrução separando o mnemônico dos operandos.
          2. Identifica qual instrução foi requisitada.
          3. Executa a alteração correspondente em Registradores, Memória ou PC.
        """
        # Limpa vírgulas e divide a instrução por espaços em branco
        # Exemplo: "LOAD R0, 5" -> ['LOAD', 'R0', '5']
        partes = instrucao.replace(",", "").split()
        operacao = partes[0]

        # =====================================================================
        # TRANSFERÊNCIA DE DADOS
        # =====================================================================
        # LOAD Reg, Imadiato -> Coloca um valor direto no registrador especificado
        if operacao == "LOAD":
            registrador = partes[1]
            valor = int(partes[2])
            self.registradores[registrador] = limitar_8bits(valor)
            self.pc += 1  # Avança o PC para a próxima instrução

        # STORE Reg, Endereço -> Grava o conteúdo do registrador na Memória
        elif operacao == "STORE":
            registrador = partes[1]
            endereco = int(partes[2])
            # Armazena o valor contido no registrador na posição correspondente da memória
            self.memoria[endereco] = self.registradores[registrador]
            self.pc += 1

        # =====================================================================
        # OPERAÇÕES ARITMÉTICAS E LÓGICAS (ULA)
        # Formato: OP RegDestino, RegOrigem (ex: ADD R0, R1 -> R0 = R0 + R1)
        # =====================================================================
        elif operacao == "ADD":
            reg1, reg2 = partes[1], partes[2]
            val1 = self.registradores[reg1]
            val2 = self.registradores[reg2]
            self.registradores[reg1] = ula("ADD", val1, val2)
            self.pc += 1

        elif operacao == "SUB":
            reg1, reg2 = partes[1], partes[2]
            val1 = self.registradores[reg1]
            val2 = self.registradores[reg2]
            self.registradores[reg1] = ula("SUB", val1, val2)
            self.pc += 1

        elif operacao == "AND":
            reg1, reg2 = partes[1], partes[2]
            val1 = self.registradores[reg1]
            val2 = self.registradores[reg2]
            self.registradores[reg1] = ula("AND", val1, val2)
            self.pc += 1

        elif operacao == "OR":
            reg1, reg2 = partes[1], partes[2]
            val1 = self.registradores[reg1]
            val2 = self.registradores[reg2]
            self.registradores[reg1] = ula("OR", val1, val2)
            self.pc += 1

        elif operacao == "XOR":
            reg1, reg2 = partes[1], partes[2]
            val1 = self.registradores[reg1]
            val2 = self.registradores[reg2]
            self.registradores[reg1] = ula("XOR", val1, val2)
            self.pc += 1

        # =====================================================================
        # CONTROLE DE FLUXO E DESVIOS
        # =====================================================================
        # JMP Endereço -> Altera incondicionalmente o PC para o endereço especificado
        elif operacao == "JMP":
            endereco = int(partes[1])
            if endereco < 0 or endereco >= len(self.memoria):
                raise ValueError("Endereço de salto inválido na memória")
            self.pc = endereco  # O PC recebe o novo endereço sem fazer incrementação

        # HALT -> Sinaliza para a CPU encerrar o processamento
        elif operacao == "HALT":
            self.halted = True

        else:
            raise ValueError(f"Instrução desconhecida recebida pela Unidade de Controle: {operacao}")

    def ciclo(self):
        """
        Executa um único ciclo completo da CPU: Fetch -> Decode -> Execute.
        """
        if self.halted:
            return

        # ---------------------------------------------------------------------
        # 1. FETCH (Busca): Lê a instrução na memória na posição apontada pelo PC
        # ---------------------------------------------------------------------
        instrucao = self.memoria[self.pc]

        print()
        print("--------------------------------")
        print("ETAPA FETCH (Busca)")
        print("PC:", self.pc)
        print("Instrução buscada:", instrucao)

        # ---------------------------------------------------------------------
        # 2. DECODE + EXECUTE (Decodificação e Execução)
        # ---------------------------------------------------------------------
        print("ETAPA DECODE + EXECUTE")
        self.executar_instrucao(instrucao)

        # ---------------------------------------------------------------------
        # 3. EXIBIÇÃO DO ESTADO ATUAL DOS REGISTRADORES
        # ---------------------------------------------------------------------
        self.mostrar_estado()

    def executar(self, max_ciclos=100):
        """
        Loop principal de execução da CPU até encontrar HALT ou atingir o limite
        de segurança de ciclos (evita loops infinitos durante simulação).
        """
        ciclos = 0

        while not self.halted:
            if ciclos >= max_ciclos:
                raise RuntimeError(
                    "Número máximo de ciclos excedido. "
                    "Verifique se o programa possui um loop infinito sem desvio de saída."
                )

            self.ciclo()
            ciclos += 1

    def mostrar_estado(self):
        """
        Exibe os valores atuais armazenados nos registradores gerais em formato
        Hexadecimal (8 bits) e Decimal.
        """
        print("Registradores:")
        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:02X} (Decimal: {valor})")
