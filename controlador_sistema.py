from tela_sistema import TelaSistema

from controlador_jogador import ControladorJogador
from loja import Loja
from personagem import Personagem
from jogador import Jogador
from skin import Skin

class ControladorSistema:

    def __init__(self):
        self.__controlador_jogador = ControladorJogador(self)
        self.__loja = None
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
    
    @property
    def loja(self):
        return self.__loja

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

"""ornn = Personagem("Ornn", 1000, ["Ornn Florescer Espiritual"])
ornn_flor_esp = Skin("Ornn Florescer Espiritual", 500, ornn)
mordekaiser = Personagem("Mordekaiser", 800)
amale = Jogador("Amale", "amale123", 800)
loja = Loja(amale, [ornn, ornn_flor_esp, mordekaiser])
loja.comprar_item()"""