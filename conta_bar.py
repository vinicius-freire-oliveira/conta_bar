# Definição da classe ContaBar
class ContaBar:
    def __init__(self, nome_cliente):
        # Inicializa o objeto ContaBar com o nome do cliente e uma lista vazia de itens consumidos
        self.nome_cliente = nome_cliente
        self.itens_consumidos = []

    def adicionar_item(self, nome_item, quantidade, preco_unitario):
        # Adiciona um item à lista de itens consumidos
        self.itens_consumidos.append({
            'nome': nome_item,            # Nome do item
            'quantidade': quantidade,     # Quantidade consumida
            'preco_unitario': preco_unitario  # Preço unitário do item
        })

    def calcular_total_conta(self):
        # Calcula o total da conta somando o preço de todos os itens multiplicado pela quantidade consumida
        total = sum(item['quantidade'] * item['preco_unitario'] for item in self.itens_consumidos)
        return total

    def imprimir_conta(self):
        # Imprime o detalhamento da conta do cliente
        print(f"==== Conta de {self.nome_cliente} ====")
        for item in self.itens_consumidos:
            # Imprime cada item consumido com seu nome, quantidade, preço unitário e total por item
            print(f"{item['nome']} x{item['quantidade']}  R${item['preco_unitario']:.2f}  R${item['quantidade']*item['preco_unitario']:.2f}")
        print("-----------------------")
        # Calcula o total da conta
        total_conta = self.calcular_total_conta()
        # Imprime o total a pagar
        print(f"Total a Pagar: R${total_conta:.2f}")
        print("=======================")

# Exemplo de uso:
conta_john = ContaBar("John")  # Criação da conta para o cliente John

# Adicionando itens à conta do John
conta_john.adicionar_item("Cerveja", 6, 5.0)              # Adiciona 6 cervejas a R$ 5,00 cada
conta_john.adicionar_item("Porção de Batata Frita", 1, 15.0)  # Adiciona 1 porção de batata frita a R$ 15,00
conta_john.adicionar_item("Água", 2, 3.0)                  # Adiciona 2 águas a R$ 3,00 cada

# Imprimir o detalhamento da conta do John
conta_john.imprimir_conta()

# Outra pessoa
conta_outra_pessoa = ContaBar("outra pessoa")  # Criação da conta para outra pessoa

# Adicionando itens à conta de outra pessoa
conta_outra_pessoa.adicionar_item("Whisky", 2, 25.0)       # Adiciona 2 whiskies a R$ 25,00 cada
conta_outra_pessoa.adicionar_item("Picanha", 1, 40.0)      # Adiciona 1 picanha a R$ 40,00
conta_outra_pessoa.adicionar_item("Suco de Laranja", 1, 5.0)   # Adiciona 1 suco de laranja a R$ 5,00
conta_outra_pessoa.adicionar_item("Caldinho de Feijão", 2, 8.0) # Adiciona 2 caldinhos de feijão a R$ 8,00 cada
conta_outra_pessoa.adicionar_item("Camarão", 3, 30.0)      # Adiciona 3 porções de camarão a R$ 30,00 cada

# Imprimir o detalhamento da conta de outra pessoa
conta_outra_pessoa.imprimir_conta()

# Calcular subtotal da conta do John
subtotal_john = conta_john.calcular_total_conta()
print(f"Subtotal da conta de {conta_john.nome_cliente}: R${subtotal_john:.2f}")

# Calcular subtotal da conta de outra pessoa
subtotal_outra_pessoa = conta_outra_pessoa.calcular_total_conta()
print(f"Subtotal da conta de {conta_outra_pessoa.nome_cliente}: R${subtotal_outra_pessoa:.2f}")

# Calcula e imprime o total combinado das duas contas
print("Total: R$", format(subtotal_john + subtotal_outra_pessoa, ".2f"))
