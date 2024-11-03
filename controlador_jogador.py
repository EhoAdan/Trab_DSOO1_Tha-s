from telas.tela_jogador import TelaJogador

from entidades.jogador import Jogador

from exceptions.dadoinvalido_exception import DadoInvalidoException

#Fazer tratamento de exceções

class ControladorJogador:

    def __init__(self, controlador_sistema):
        self.__jogadores = [Amale, Tchali, B_de_Bingança, Teste]
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema
        self.__jogador_logado = 0

    @property
    def jogador_logado(self):
        return self.__jogador_logado

    @jogador_logado.setter
    def jogador_logado(self, jogador_logado):
        self.__jogador_logado = jogador_logado

    def abre_tela(self):
        opcoes_tela = {0: self.__controlador_sistema.abre_tela,
                1: self.criar_conta,
                2: self.listar,
                3: self.alterar,
                4: self.deletar,
                5: self.login
                }
        
        while True:
            opcoes_tela[self.__tela_jogador.abre_tela()]()
    
    def acoes_login(self):
        opcoes_jogador = {0: self.abre_tela,
                1: self.jogar_partida,
                2: self.historico_partidas,
                3: self.adicionar_amigo,
                4: self.excluir_amigo,
                5: self.listar_amigos
                }
        
        while True:
            opcoes_jogador[self.__tela_jogador.acoes_login()]()

    def login(self):
        email_informado = input("Favor, digite seu endereço de e-mail: ")
        senha_informada = input("Favor, digite sua senha: ")
        for usuario_registrado in self.__jogadores:
            if usuario_registrado.email == email_informado:
                if usuario_registrado.senha == senha_informada:
                    self.__jogador_logado = usuario_registrado
                    print(f"Você logou como: {self.__jogador_logado.nome}")
                    self.acoes_login()
        return None

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

    def criar_conta(self):
        while True:
            # Caso não surja o NameError, ou seja, ter o email certo, quebra o loop
            try:
                #Funciona
                email = str(input("Digite seu endereço de e-mail: "))
                if any(email_usado.email == email for email_usado in self.__jogadores):
                    print("E-mail já está em uso")
                    raise NameError
                if ("@" not in email or email[0] == "@" or email[-1] == "@"):
                    raise NameError
                break
            except NameError:
                print("Favor inserir um e-mail válido")
        while True:
            try:
                #Funciona
                nome = str(input("Digite seu nome de usuário: "))
                if any(usuario_existe.nome == nome for usuario_existe in self.__jogadores):
                    print("Nome de usuário já existe")
                    raise NameError
                break
            except NameError:
                print("Favor inserir um nome válido")
        while True:
            try:
                #Funciona
                senha = input("""Digite sua senha
Ela deve possuir:
Ao menos 8 caracteres
Ao menos um número
Ao menos uma letra
""")
                if len(senha) < 8:
                    print("Senha muito curta!")
                    raise NameError
                if not any(caractere.isnumeric() for caractere in senha):
                    print("Senha não possui número!")
                    raise NameError
                if not any(caractere.isalpha() for caractere in senha):
                    print("Senha não possui letra!")
                    raise NameError
                break
            except NameError:
                print("Favor inserir uma senha válida")
        jogador_novo = nome #Dessa forma evitamos de ter um item jogador_novo sendo modificado na lista toda vez que tentamos criar outro
        jogador_novo = Jogador(nome, email, senha)
        self.__jogadores.append(jogador_novo)
        print(f"""Nova conta criada com sucesso!
Seu nome de Jogador é: {nome}
Seu e-mail é: {email}
Sua senha é: {senha}
""")
        
    def listar(self):
        for jogador in self.__jogadores:
            print(jogador.nome)

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

Amale = Jogador("Amale", "amale@gmail.com", "amale123", 999999)
Tchali = Jogador("Tchali", "tchali123@gmail.com.br", "tchali123")
B_de_Bingança = Jogador("B de Bingança", "B@B", "123")
Teste = Jogador("Teste", "a", "a")