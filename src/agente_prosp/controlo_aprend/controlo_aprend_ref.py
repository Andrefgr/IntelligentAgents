from controlo_react.controlo import Controlo
from mec_aprend import MecAprend
from psa.accao import Mover
import psa

class ControloAprendRef(Controlo):
    
    def __init__(self):
        
        self._rmax = 100
        self._s = None
        self._a = None
        self._accoes = [Mover(ang, ang_abs = True) for ang in psa.dirmov()]
        self._mec_aprend = MecAprend(self._accoes)
        
        
    def processar(self, percepcao):
        
        sn = percepcao.posicao
        r = self._gerar_reforco(percepcao)
        
        if(self._a):
            
            self._mec_aprend.aprender(self._s, self._a, r, sn)
            
        self._s = sn
        
        an = self._mec_aprend.seleccionar_accao(sn)
        
        self._a = an
        
        return an # Accao
        
        
    def _gerar_reforco(self, percepcao):
        
        r = percepcao.custo_mov * -1
        
        if(percepcao.carga):
            
            r += self._rmax
            
        if(percepcao.colisao):
            
            r -= self._rmax
        
        return r # double
        
    
    # @property    
    # def s(self):
        
        # return self._s
        
    
    # @property    
    # def a(self):
        
        # return self._a
        
    
    # @property    
    # def rmax(self):
        
        # return self._rmax
        
    
    # @property    
    # def mec_aprend(self):
        
        # return self._mec_aprend