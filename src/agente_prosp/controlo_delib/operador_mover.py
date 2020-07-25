from psa.util import mover, dist
from psa.accao import Mover

class OperadorMover:
    
    def __init__(self, modelo_mundo, ang):
        
        self._modelo_mundo = modelo_mundo
        self._ang = ang
        self._accao = Mover(ang, ang_abs = True)
        
    def aplicar(self, estado): 
        
        nova_pos = mover(estado, self._ang)
        
        if(self._modelo_mundo._elementos.get(nova_pos) == 'alvo' or self._modelo_mundo._elementos.get(nova_pos) == 'vazio'):
            
	   return nova_pos
        
    def custo(self, estado, novo_estado):
        
        return max(1, dist(estado, novo_estado))
        
    @property
    def accao(self):
        
        return self._accao
        
    
    @property
    def ang(self):
        
        return self._ang