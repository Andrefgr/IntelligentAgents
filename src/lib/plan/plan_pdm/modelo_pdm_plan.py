# -*- coding: utf-8 -*-

from pdm.modelo_pdm import ModeloPDM
from plan.modelo_plan import ModeloPlan

class ModeloPDMPlan(ModeloPDM, ModeloPlan):
    
    def __init__(self, modelo_plan, objectivos):
        
        self._rmax = 5000
        self._S = []
        self._A = []
        self._T = {}
        self._R = {}
        self._objectivos = objectivos
        self._iniciar_modelo(modelo_plan)
        
        
    def _iniciar_modelo(self, modelo_plan):
        
        self._S = modelo_plan.estados()
        self._A = modelo_plan.operadores()
        for s in self._S:
            for a in self._A:
                self._gerar_modelo(s, a)
                
        
    def _gerar_modelo(self, s, a):
        
        sn = a.aplicar(s)
        if sn is None:
            self._T[(s, a)] = []
        
        else:
            self._T[(s, a)] = [(1, sn)]
            self._R[(s, a, sn)] = self._gerar_recompensa(s, a, sn)
            
        
    def _gerar_recompensa(self, s, a, sn):
        
        r = -a.custo(s, sn)
        
        if sn in self._objectivos:
            r += self._rmax
        
        return r # double
        
        
    def S(self):
        
        return self._S
        
        
    def A(self, _):
        
        return self._A
        
        
    def T(self, s, a):
        
        return self._T[(s, a)] # Transicao
        
        
    def R(self, s, a, sn):
        
        return self._R[(s, a, sn)] # double