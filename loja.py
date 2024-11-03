from jogador import Jogador
from personagem import Personagem
from skin import Skin
from tela_loja import TelaLoja


class Loja:

    def __init__(self, jogador: Jogador, itens = []):
        # Serve como o controlador de itens
        try:
            if not isinstance(jogador, Jogador) and jogador:
                raise TypeError 
            if not isinstance(itens, list) and itens:
                raise TypeError
            for objeto in itens:
                if not isinstance(objeto, Skin) and not isinstance(objeto, Personagem):
                    raise TypeError
            self.__jogador = jogador
            self.__itens = itens
            self.__tela_loja = TelaLoja()

        except TypeError:
            print("Houve um erro ao instanciar a loja.")

    @property
    def jogador(self):
        return self.__jogador

    @property
    def itens(self):
        return self.__itens

    @property
    def tela_loja(self):
        return self.__tela_loja

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