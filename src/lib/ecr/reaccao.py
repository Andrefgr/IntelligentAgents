from comportamento import Comportamento

class Reaccao(Comportamento):
    
    def activar(self, percepcao):
        
        estimulo = self._detectar_estimulo(percepcao)
        
        if(estimulo is not None and estimulo):
            
            return self._gerar_resposta(estimulo)
        
    def _gerar_resposta(self, estimulo):
        
        abstract
        
    def _detectar_estimulo(self, percepcao):
        
        abstract