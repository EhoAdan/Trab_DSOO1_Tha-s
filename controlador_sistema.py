from telas.tela_sistema import TelaSistema

from controladores.controlador_jogador import ControladorJogador
from controladores.controlador_loja import ControladorLoja

class ControladorSistema:

    def __init__(self):
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_loja = ControladorLoja(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
    
    @property
    def controlador_loja(self):
        return self.__controlador_loja

    def inicializa_sistema(self):
        self.abre_tela()
    
    def encerrar(self):
        print("Jogo encerrado")
        exit()

    def abre_tela(self):
        tela_opcoes = {0: self.encerrar,
                    1: self.__controlador_jogador.abre_tela,
                    2: self.__controlador_loja.abre_tela,}
        while True:
            tela_opcoes[self.__tela_sistema.menu_opcoes()]()