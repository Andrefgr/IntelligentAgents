from sel_accao import SelAccao
import random

class SelAccaoEGreedy(SelAccao):
    
    def __init__(self, mem_aprend, accoes, epsilon):
        
        self._epsilon = epsilon
        self._mem_aprend = mem_aprend
        self._accoes = accoes
        
    
    def seleccionar_accao(self, s):
        
        var = random.random()
        accao = None
        
        if (var < self._epsilon):
            
            accao = self.explorar(s)
            
        else:
            
            accao = self.max_accao(s)
        
        return accao # Accao
        
    
    def max_accao(self, s):
        
        return max(self._accoes, key = lambda a : self._mem_aprend.obter(s, a)) # Accao
        
    
    def explorar(self, s):
        
        return random.choice(self._accoes) # Accao
        
    
    @property    
    def epsilon(self):
        
        return self._epsilon
        
    
    @property    
    def mem_aprend(self):
        
        return self._mem_aprend
        
    
    @property
    def accoes(self):
        
        return self._accoes