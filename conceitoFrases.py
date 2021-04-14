class FraseConceito:
    def __init__(self,id=0,frase='',pontuacao=0):
        self.__id=id
        self.__palavra=frase
        self.__pontuacao=pontuacao
    
    def get_id():
        return self.__id
    
    def set_id(id):
        self.__id=id
    
    def get_palavra():
        return self.__palavra
    
    def set_palavra(frase):
        self.__palavra=frase

    def get_pontuacao():
        return self.pontuacao
    
    def set_pontuacao(ponto):
        self.pontuacao=ponto