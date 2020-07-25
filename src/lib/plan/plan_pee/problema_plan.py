from pee.modprob.problema_heur import ProblemaHeur
from psa.util import dist

class ProblemaPlan(ProblemaHeur):
    
    def __init__(self, estado_inicial, estado_final, operadores):
        
        ProblemaHeur.__init__(self, estado_inicial, operadores)
        self._estado_final = estado_final
        
        
    def objectivo(self, estado):
        
        return estado == self._estado_final
        
        
    def heuristica(self, estado):
            
        return dist(estado, self._estado_final)