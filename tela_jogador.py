class TelaJogador():

    def abre_tela(self):
        print("""-------- O que você quer fazer? ---------
0- Voltar ao Início
1- Criar conta
2- Ver jogadores do server
3- Ver Top Jogadores do server
4- Alterar nome da sua conta
5- Deletar sua conta
6- Log In
""")
        return self.jogador_selecionar_opcao_int("Selecione uma opção: ", 5, 0)

    def acoes_login(self):
        print("""-------- O que você quer fazer? ---------
0- Voltar à tela anterior
1- Jogar partida
2- Histórico de Partidas
3- Adicionar amigo
4- Excluir amigo
5- Listar amigos
""")
        return self.jogador_selecionar_opcao_int("Selecione uma opção: ", 5, 0)

    def jogador_selecionar_opcao_int(self, mensagem, limite_superior, limite_inferior):
        while True:
            try:
                opcao_usuario = int(input(mensagem))
                if not limite_inferior <= opcao_usuario <= limite_superior:
                    raise ValueError
                return opcao_usuario
            except ValueError:
                print("Favor inserir uma opção válida.")
