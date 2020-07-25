from memoria_aprend import MemoriaAprend

class MemoriaEsparsa(MemoriaAprend):
    
    def __init__(self, valor_omissao = 0):
        
        self._valor_omissao = valor_omissao
        self._Q = {}
        
        
    def actualizar(self, s, a, q):
        
        self._Q[(s, a)] = q
        
        
    def obter(self, s, a):
        
        return self._Q.get((s, a), self._valor_omissao) # double
        
    
    @property
    def memoria(self):
        
        return self._Q