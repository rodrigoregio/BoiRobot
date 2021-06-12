class Carta:
    def __init__(self):
        self.descricao=''
        self.pontos=0
        self.numero=0

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero=numero

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
    
    def __str__(self) -> str:
        return "carta: ["+str(self.pontos)+", "+str(self.numero)+", "+self.descricao+"]"