class TelaLoja():

    def buscar_itens(self, num_itens: int):
        while True:
            try:
                input_usuario = int(input("Selecione uma opção pelo número: "))
                if not 0 <= input_usuario <= num_itens:
                    raise ValueError
                return input_usuario
            except ValueError:
                print("Valor fora do alcance.")
            except TypeError:
                print("Entrada deve ser um número inteiro.")

    def abre_tela(self):
        print("""-------- O que você quer fazer? ---------
0- Voltar à tela anterior
1- Ver todos os itens
2- Ver itens disponíveis para mim
3- Comprar item
""")
        return self.jogador_selecionar_opcao_int("Selecione uma opção: ", 3, 0)

    def jogador_selecionar_opcao_int(self, mensagem, limite_superior, limite_inferior):
        while True:
            try:
                opcao_usuario = int(input(mensagem))
                if not limite_inferior <= opcao_usuario <= limite_superior:
                    raise ValueError
                return opcao_usuario
            except ValueError:
                print("Favor inserir uma opção válida.")
