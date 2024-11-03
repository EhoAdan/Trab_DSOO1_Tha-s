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