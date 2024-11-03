class ControladorLoja:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def abre_tela(self):
        print("Tela ainda não implementada")
        exit()