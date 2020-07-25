from comportamento import Comportamento

class ComportComp(Comportamento):
    
    def __init__(self, comportamentos):
        
        self._comportamentos = comportamentos
        
    def activar(self, percepcao):
        
        respostas = []
        
        for i in self._comportamentos:
            
            resposta = i.activar(percepcao)
            
            if(resposta is not None):
            
                respostas.append(resposta)
        
        if respostas:    
            
            return self.seleccionar_resposta(respostas)
        
    def seleccionar_resposta(self, respostas):
        
        abstract