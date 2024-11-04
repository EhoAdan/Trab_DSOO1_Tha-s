from tela_sistema import TelaSistema

from controlador_jogador import ControladorJogador
from controlador_loja import ControladorLoja
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
                    2: self.__loja.abre_tela,}
        while True:
            tela_opcoes[self.__tela_sistema.menu_opcoes()]()

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
amale = Jogador("Amale", "tantofaz123", "amale123", 800)
loja = ControladorLoja(amale, [ornn, ornn_flor_esp, mordekaiser, kratos, kratos_nordico, pikachu, pikachu_ash,
                    pikachu_gmax, pikachu_surf, pikachu_wwe])
loja.comprar_item()