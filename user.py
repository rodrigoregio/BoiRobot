class User:
    def __init__(self, id,display_name):
        self.__id=id
        self.__displayName=display_name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def displayName(self):
        return self.__displayName