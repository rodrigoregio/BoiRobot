class Carta:
    def __init__(self):
        self.descricao=''
        self.pontos=0

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self,descreve):
        self._descricao=descreve

    @property
    def pontos(self):
        return self._pontos

    @pontos.setter
    def pontos(self,point):
        self._pontos=point