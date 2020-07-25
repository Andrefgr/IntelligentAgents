from comport_comp import ComportComp

class Hierarquia(object, ComportComp):
    
    def __init__(self, comportamentos):
        
        self._comportamentos = comportamentos
        
    def seleccionar_resposta(self, respostas):
        
        if respostas:
            return respostas[0]