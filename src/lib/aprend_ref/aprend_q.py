from aprend_ref import AprendRef

class AprendQ(AprendRef):
    
    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        
        super(AprendQ, self).__init__(mem_aprend, sel_accao)
        self._alfa = alfa
        self._gama = gama
        
        
    def aprender(self, s, a, r, sn):
        
        qsa = self._mem_aprend.obter(s, a)
        an = self._sel_accao.max_accao(sn)
        qsnan = self._mem_aprend.obter(sn, an)
        
        q = qsa + self._alfa * (r + self._gama * qsnan - qsa)
        
        self._mem_aprend.actualizar(s, a, q)
        
        
    # @property
    # def alfa(self):
        
        # return self._alfa
        
    
    # @property
    # def gama(self):
        
        # return self._gama
        
    
    # @property
    # def mem_aprend(self):
        
        # return self._mem_aprend
        
    
    # @property
    # def sel_accao(self):
        
        # return self._sel_accao