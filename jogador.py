class Jogador:
    def __init__(self, nome: str, senha: str, email: str, saldo: int = 0, lista_itens_jogador = [],
                 dinheiro_gasto: int = 0, presentes_dados: int = 0,
                 presentes_recebidos: int = 0, partidas_jogadas: int = 0):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__saldo = saldo
        self.__lista_itens_jogador = lista_itens_jogador
        self.__dinheiro_gasto = dinheiro_gasto
        self.__presentes_dados = presentes_dados
        self.__presentes_recebidos = presentes_recebidos
        self.__partidas_jogadas = partidas_jogadas
        self.__amigos = []
        self.__historico_de_compras = []
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        # Idealmente teria toda a checagem pro @, .com etc, tem no projeto antigo inclusive
        # mas por enquanto fica assim mesmo
        try:
            if not isinstance(email, str):
                raise TypeError
            self.__email = email

        except TypeError:
            print("Houve um erro na mudança de email.")

    @property
    def senha(self):
        return self.__senha

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        try:
            if not isinstance(saldo, int):
                raise TypeError
            self.__saldo = saldo

        except TypeError:
            print("Houve um erro ao configurar o saldo do jogador.")

    @property
    def dinheiro_gasto(self):
        return self.__dinheiro_gasto
    
    @property
    def presentes_dados(self):
        return self.__presentes_dados
    
    @property
    def presentes_recebidos(self):
        return self.__presentes_recebidos
    
    @property
    def partidas_jogadas(self):
        return self.__partidas_jogadas
    
    @partidas_jogadas.setter
    def partidas_jogadas(self, partidas_jogadas):
        self.__partidas_jogadas = partidas_jogadas
    
    @property
    def amigos(self):
        return self.__amigos

    @amigos.setter
    def amigos(self, amigos):
        self.__amigos = amigos

    @property
    def lista_itens_jogador(self):
        return self.__lista_itens_jogador

    @lista_itens_jogador.setter
    def lista_itens_jogador(self, lista_itens_jogador):
        self.__lista_itens_jogador = lista_itens_jogador

    @property
    def historico_de_compras(self):
        return self.__historico_de_compras

    @historico_de_compras.setter
    def historico_de_compras(self, historico_de_compras):
        try:
            if not isinstance(historico_de_compras, list) and historico_de_compras:
                raise TypeError
            """ Quando importar compra faz essa checagem também
            for compra in historico_de_compras:
                if not isinstance(compra, Compra):
                    raise TypeError"""
            self.__historico_de_compras = historico_de_compras

        except TypeError:
            print("Houve um erro ao configurar o histórico de compras do jogador.")