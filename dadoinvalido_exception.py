class DadoInvalidoException(Exception):
    def __init__(self, message="""Dado Inválido.
                 Voltando à tela anterior"""):
        super().__init__(message)
