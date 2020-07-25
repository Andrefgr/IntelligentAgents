from aprend_ref.memoria_esparsa import MemoriaEsparsa
from aprend_ref.aprend_q import AprendQ
from aprend_ref.sel_accao_e_greedy import SelAccaoEGreedy
import psa

class MecAprend:
    
    def __init__(self, accoes):
        
        self._accoes = accoes
        epsilon = 0.01
        gama = 0.9
        alfa = 0.5
        self._mem_aprend = MemoriaEsparsa()
        self._sel_accao = SelAccaoEGreedy(self._mem_aprend, accoes, epsilon)
        self._aprend_ref = AprendQ(self._mem_aprend, self._sel_accao, alfa, gama)
        
    
    def aprender(self, s, a, r, sn):
        
        self._aprend_ref.aprender(s, a, r, sn) # void
        self.mostrar(sn)
        
    
    def seleccionar_accao(self, s):
        
        return self._sel_accao.seleccionar_accao(s)
        
        
    # @property
    # def accoes(self):
        
        # return self._accoes
        
    
    # @property
    # def mem_aprend(self):
        
        # return self._mem_aprend
        
      
    # @property  
    # def aprend_ref(self):
        
        # return self._aprend_ref
        
    
    # @property    
    # def sel_accao(self):
        
        # return self._sel_accao
        
        
    def mostrar(self, s):
        psa.vis(1).limpar()
        psa.vis(1).aprendref(self._aprend_ref)
        psa.vis(2).accoesestado(s, self._accoes, self._mem_aprend.memoria)