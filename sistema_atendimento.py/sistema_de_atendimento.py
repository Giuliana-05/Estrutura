import heapq

class Cliente:
    def __init__(self, nome, cpf, prioridade=False, nivel_prioridade=0):
        self.nome = nome
        self.cpf = cpf
        self.prioridade = prioridade
        self.nivel_prioridade = nivel_prioridade  # Menor valor = mais prioridade

    def __lt__(self, outro):
        return self.nivel_prioridade < outro.nivel_prioridade

    def __str__(self):
        tipo = "Prioritário" if self.prioridade else "Comum"
        return f"{self.nome} ({tipo})"

class SistemaAtendimento:
    def __init__(self):
        self.fila_comum = []
        self.heap_prioritarios = []
        self.pilha_ultimos_atendimentos = []

    def cadastrar_cliente(self, nome, cpf, prioridade=False, nivel_prioridade=0):
        cliente = Cliente(nome, cpf, prioridade, nivel_prioridade)
        if prioridade:
            heapq.heappush(self.heap_prioritarios, cliente)
        else:
            self.fila_comum.append(cliente)
        print(f"Cliente {cliente.nome} cadastrado com sucesso!")

    def iniciar_atendimento(self):
        if self.heap_prioritarios:
            cliente = heapq.heappop(self.heap_prioritarios)
        elif self.fila_comum:
            cliente = self.fila_comum.pop(0)
        else:
            print("Não há clientes para atender.")
            return

        self.pilha_ultimos_atendimentos.append(cliente)
        print(f"Atendendo cliente: {cliente}")

    def desfazer_atendimento(self):
        if not self.pilha_ultimos_atendimentos:
            print("Nenhum atendimento para desfazer.")
            return

        cliente = self.pilha_ultimos_atendimentos.pop()
        if cliente.prioridade:
            heapq.heappush(self.heap_prioritarios, cliente)
        else:
            self.fila_comum.insert(0, cliente)  # Volta ao início da fila
        print(f"Atendimento desfeito: {cliente}")

    def listar_fila(self):
        print("\n--- Fila de Espera ---")
        print("Clientes Prioritários:")
        for c in sorted(self.heap_prioritarios):
            print(f"  - {c.nome} (Prioridade {c.nivel_prioridade})")
        print("Clientes Comuns:")
        for c in self.fila_comum:
            print(f"  - {c.nome}")
        print("----------------------\n")

def menu():
    sistema = SistemaAtendimento()
    while True:
        print("\n--- MENU ---")
        print("[1] Cadastrar Cliente")
        print("[2] Iniciar Atendimento")
        print("[3] Desfazer Último Atendimento")
        print("[4] Listar Fila de Espera")
        print("[5] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            tipo = input("Cliente prioritário? (s/n): ").lower()
            if tipo == 's':
                nivel = int(input("Nível de prioridade (1 = mais urgente): "))
                sistema.cadastrar_cliente(nome, cpf, True, nivel)
            else:
                sistema.cadastrar_cliente(nome, cpf)

        elif opcao == "2":
            sistema.iniciar_atendimento()

        elif opcao == "3":
            sistema.desfazer_atendimento()

        elif opcao == "4":
            sistema.listar_fila()

        elif opcao == "5":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
