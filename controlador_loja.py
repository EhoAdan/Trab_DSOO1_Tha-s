from jogador import Jogador
from personagem import Personagem
from skin import Skin
from tela_loja import TelaLoja
from controlador_jogador import ControladorJogador



class ControladorLoja:

    def __init__(self, jogador: Jogador, controlador_sistema, itens = []):
        # Serve como o controlador de itens
        self.__tela_loja = TelaLoja()
        self.__itens = itens
        self.__controlador_sistema = controlador_sistema
        self.__controlador_jogador = ControladorJogador(controlador_sistema)
        self.__jogador = jogador
        self.__jogador_logado = 0

    @property
    def jogador(self):
        return self.__jogador

    @property
    def itens(self):
        return self.__itens

    @property
    def tela_loja(self):
        return self.__tela_loja

    @property
    def jogador_logado(self):
        return self.__jogador_logado
    
    @jogador.setter
    def jogador(self, jogador):
        try:
            if not isinstance(jogador, Jogador):
                raise TypeError
            self.__jogador = jogador

        except TypeError:
            print("Houve um erro ao modificar o jogador.")

    @itens.setter
    def itens(self, itens):
        try:
            if not isinstance(itens, list):
                raise TypeError
            for objeto in itens:
                if not isinstance(objeto, Personagem) and not isinstance(objeto, Skin):
                    raise TypeError
            self.__itens = itens

        except TypeError:
            print("Houve um erro ao modificar a lista de itens da loja.")

    @tela_loja.setter
    def tela_loja(self, tela_loja):
        try:
            if not isinstance(tela_loja, TelaLoja):
                raise TypeError
            self.__tela_loja = tela_loja

        except TypeError:
            print("Houve um erro ao modificar a tela da loja.")

    @jogador_logado.setter
    def jogador_logado(self, jogador_logado):
        self.__jogador_logado = jogador_logado

    def login(self):
        print("Para acessar a Loja é necessário fazer Log In")
        email_informado = input("Favor, digite seu endereço de e-mail: ")
        senha_informada = input("Favor, digite sua senha: ")
        for usuario_registrado in self.__controlador_jogador._ControladorJogador__jogadores:
            if usuario_registrado.email == email_informado:
                if usuario_registrado.senha == senha_informada:
                    self.__jogador_logado = usuario_registrado
                    print(f"Você logou como: {self.__jogador_logado.nome}")
                    self.abre_tela()
        return None

    def abre_tela(self):
        opcoes_loja = {0: self.__controlador_sistema.abre_tela,
                1: self.buscar_todos_itens_loja,
                2: self.buscar_itens_disponiveis,
                3: self.comprar_item,
                }
        
        while True:
            opcoes_loja[self.__tela_loja.abre_tela()]()
    
    def buscar_todos_itens_loja(self):
        i = 0
        lista_itens_num = {0: None}
        print("0: Retornar")
        for item in self.__itens:
            i += 1
            print(f"{i}: {item.nome}")
            lista_itens_num[i] = item
        opcao_usuario = self.__tela_loja.buscar_itens(i)
        return lista_itens_num[opcao_usuario]

    def buscar_itens_disponiveis(self, comprar = False):
        i = 0
        lista_itens_num = {0: None}
        print("0: Retornar")
        for item in self.__itens:
            if (item not in self.__jogador.lista_itens_jogador and
                (isinstance(item, Personagem) or item.personagem in self.__jogador.lista_itens_jogador)):
                # Basicamente, verifica se o item tá na lista de itens do jogador,
                # caso não esteja, verifica se é um personagem ou skin, caso seja skin,
                # verifica se o jogador tem o personagem ao qual a skin pertence
                i += 1
                mensagem_mostrar = f"{i}: {item.nome}"
                if comprar:
                    mensagem_mostrar += f" por {item.preco}"
                print(mensagem_mostrar)
                lista_itens_num[i] = item
        opcao_usuario = self.__tela_loja.buscar_itens(i)
        return lista_itens_num[opcao_usuario]

    def comprar_item(self):
        # Vou deixar sem presentear por enquanto, mas se puxar do controlador de jogador
        # Deve dar sem muito problema
        while True:
            print(f"Saldo atual: {self.__jogador.saldo}")
            item_comprado = self.buscar_itens_disponiveis(True)
            if not item_comprado:
                return None
            if self.__jogador.saldo >= item_comprado.preco:
                self.__jogador.saldo -= item_comprado.preco
                self.__jogador.lista_itens_jogador.append(item_comprado)
                return None
            print("Saldo insuficiente.")
    def abre_tela(self):
        pass

# Lista preliminar de jogadores e itens

"""Amale = Jogador("Amale", "amale@gmail.com", "amale123", 999999)
Tchali = Jogador("Tchali", "tchali123@gmail.com.br", "tchali123")
B_de_Bingança = Jogador("B de Bingança", "B@B", "123")
Teste = Jogador("Teste", "a", "a", 10000)

ornn = Personagem("Ornn", 1000, ["Ornn Florescer Espiritual"])
ornn_flor_esp = Skin("Ornn Florescer Espiritual", 500, ornn)
mordekaiser = Personagem("Mordekaiser", 800)
kratos = Personagem("Kratos", 500, ["Kratos Nórdico"])
kratos_nordico = Skin("Kratos Nórdico", 200, kratos)
pikachu = Personagem("Pikachu", 52, ["Pikachu Surfista", "Pikachu-Ash", "Pikachu Luta-Libre", "Pikachu Gigantamax"])
pikachu_surf = Skin("Pikachu Surfista", 2, pikachu)
pikachu_ash = Skin("Pikachu Ash", 22, pikachu)
pikachu_wwe = Skin("Pikachu Luta-Libre", 30, pikachu)
pikachu_gmax = Skin("Pikachu Gigantamax", 1200, pikachu)
loja = ControladorLoja(Teste, [ornn, ornn_flor_esp, mordekaiser, kratos, kratos_nordico, pikachu, pikachu_ash,
                    pikachu_gmax, pikachu_surf, pikachu_wwe])
loja.comprar_item()"""
