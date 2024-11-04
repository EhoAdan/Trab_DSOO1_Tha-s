from tela_jogador import TelaJogador

from jogador import Jogador

from dadoinvalido_exception import DadoInvalidoException

#Fazer tratamento de exceções

class ControladorJogador:

    def __init__(self, controlador_sistema):
        self.__jogadores = [Amale, Tchali, B_de_Bingança, Teste]
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema
        self.__jogador_logado = False

    @property
    def jogador_logado(self):
        return self.__jogador_logado

    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @jogadores.setter
    def jogadores(self, jogadores):
        self.__jogadores = jogadores

    @jogador_logado.setter
    def jogador_logado(self, jogador_logado):
        self.__jogador_logado = jogador_logado

    def abre_tela(self):
        opcoes_tela = {0: None,
                1: self.listar,
                2: self.estats,
                3: self.alterar,
                4: self.deletar}
        
        while True:
            opcao = opcoes_tela[self.__tela_jogador.abre_tela()]
            if not opcao:
                return None
            opcao()

    def acoes_login(self):
        opcoes_jogador = {0: None,
                1: self.abre_tela,
                2: self.jogar_partida,
                3: self.historico_partidas,
                4: self.adicionar_amigo,
                5: self.excluir_amigo,
                6: self.listar_amigos
                }
        
        while True:
            opcao = opcoes_jogador[self.__tela_jogador.acoes_login()]
            if not opcao:
                return None
            opcao()

    def jogar_partida(self):
        print("Você jogou uma partida")
        self.__jogador_logado.partidas_jogadas += 1
        print(f"Você já jogou {self.__jogador_logado.partidas_jogadas} partidas")
    
    def historico_partidas(self):
        print(f"Você já jogou {self.__jogador_logado.partidas_jogadas} partidas")

    def eh_jogador(self, nome_jogador):
        for jogador_existe in self.__jogadores:
            if jogador_existe.nome == nome_jogador:
                return jogador_existe
        return None

    def adicionar_amigo(self):
        nome_jogador = input("Digite o nome do jogador que quer adicionar: ")
        jogador_existe = self.eh_jogador(nome_jogador)
        if not isinstance(jogador_existe, Jogador):
            print("Houve uma tentativa de adicionar um não-jogador como amigo.")
        elif jogador_existe.nome == self.__jogador_logado.nome:
            print("Você não pode se adicionar como amigo.")
        elif any(jogador_existe.nome == amigo.nome for amigo in self.__jogador_logado.amigos):
            print(f"{jogador_existe.nome} já é seu amigo.")
        else:
            self.__jogador_logado.amigos.append(jogador_existe)
            print(f"{jogador_existe.nome} adicionado com sucesso à sua lista de amigos.")
        return self.acoes_login()

    def excluir_amigo(self):
        nome_jogador = input("Digite o nome do amigo que quer excluir: ")
        jogador_existe = self.eh_jogador(nome_jogador)
        for amigo in self.__jogador_logado.amigos:
            if jogador_existe.nome == amigo.nome:
                self.__jogador_logado.amigos.remove(amigo)
            return self.acoes_login()

    def listar_amigos(self):
        print("Esta é sua lista atual de amigos:")
        for amigo in self.__jogador_logado.amigos:
            print(amigo.nome)
        return self.acoes_login()
        
    def listar(self):
        for jogador in self.__jogadores:
            print(jogador.nome)

    def estats(self):
        mais_dinheiro_gasto = 0
        mais_presentes_dados = 0
        mais_partidas_jogadas = 0
        jog_mais_dinheiro_gasto = 0
        jog_mais_presenteador = 0
        jog_mais_partidas = 0
        for jogador in self.__jogadores:
            if jogador.dinheiro_gasto > mais_dinheiro_gasto:
                jog_mais_dinheiro_gasto = jogador
                mais_dinheiro_gasto = jogador.dinheiro_gasto
            if jogador.presentes_dados > mais_presentes_dados:
                jog_mais_presenteador = jogador
                mais_presentes_dados = jogador.presentes_dados
            if jogador.partidas_jogadas > mais_partidas_jogadas:
                jog_mais_partidas = jogador
                mais_partidas_jogadas = jogador.partidas_jogadas
        print(f"""O jogador que mais investiu no jogo foi:
{jog_mais_dinheiro_gasto.nome}!!!
com um aporte total de {mais_dinheiro_gasto}!!!""")
        print(f"""O jogador candidato à Papai Noel é:
{jog_mais_presenteador.nome}!!!
presenteando um total de {mais_presentes_dados} vezes!!!""")
        print(f"""O jogador ProPlayer do momento:
{jog_mais_partidas.nome}!!!
jogando {mais_partidas_jogadas} partidas!!!""")
    
    def alterar(self):
        email_informado = input("Favor, confirme seu endereço de e-mail: ")
        senha_informada = input("Favor, confirme sua senha: ")
        for usuario_registrado in self.__jogadores:
            if usuario_registrado.email == email_informado:
                if usuario_registrado.senha == senha_informada:
                    novo_nome = input("Favor, digite seu novo nome: ")
                    if any(usuario_registrado.nome == novo_nome for usuario_registrado in self.__jogadores):
                        print("Nome de usuário já existe")
                        raise DadoInvalidoException
                    else:
                        usuario_registrado.nome = novo_nome
                        print(f"""Nome alterado com sucesso!
Seu novo nome é: {usuario_registrado.nome}""")
                    return None
                break


    def deletar(self):
        email_informado = input("Favor, confirme seu endereço de e-mail: ")
        senha_informada = input("Favor, confirme sua senha: ")
        try:
            for usuario_registrado in self.__jogadores:
                if usuario_registrado.email == email_informado:
                    if usuario_registrado.senha == senha_informada:
                        print("""Excluir uma conta é um processo permanente!
Tem certeza que deseja excluí-la?
0- Não, não desejo excluir minha conta.
9- Sim, desejo excluir minha conta.
""")
                        resposta = int(input())
                        if resposta == 9:
                            self.__jogadores.remove(usuario_registrado)
                            print("""Conta excluída com sucesso!
Retornando à tela anterior.""")
                            self.abre_tela()
                        elif resposta == 0:
                            print("Que bom que decidiu não excluir sua conta e continuar conosco!")
                            self.abre_tela()
                        else:
                            print("Opção inválida! Retornando a tela anterior.")
                            self.abre_tela()
        except ValueError:
            print("Opção inválida! Retornando a tela anterior.")
            return self.abre_tela()

#Lista preliminar de jogadores

Amale = Jogador("Amale", "amale123", "amale@gmail.com", 9999999)
Tchali = Jogador("Tchali", "tchali123", "tchali123@gmail.com.br")
B_de_Bingança = Jogador("B de Bingança", "123", "b@b.com")
Teste = Jogador("Teste", "a", "a", 10000)
