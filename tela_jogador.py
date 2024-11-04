class TelaJogador():

    def abre_tela(self):
        print("""-------- O que você quer fazer? ---------
0- Voltar ao Início
1- Ver jogadores do server
2- Ver top jogadores do server
3- Alterar nome da sua conta
4- Deletar sua conta
""")
        return self.jogador_selecionar_opcao_int("Selecione uma opção: ", 4, 0)

    def acoes_login(self):
        print("""-------- O que você quer fazer? ---------
0- Voltar à tela anterior
1- Acessar estatísticas e configurações da conta
2- Jogar partida
3- Histórico de Partidas
4- Adicionar amigo
5- Excluir amigo
6- Listar amigos
""")
        return self.jogador_selecionar_opcao_int("Selecione uma opção: ", 6, 0)

    def jogador_selecionar_opcao_int(self, mensagem, limite_superior, limite_inferior):
        while True:
            try:
                opcao_usuario = int(input(mensagem))
                if not limite_inferior <= opcao_usuario <= limite_superior:
                    raise ValueError
                return opcao_usuario
            except ValueError:
                print("Favor inserir uma opção válida.")
