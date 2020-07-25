from plan.planeador import Planeador
from pdm.pdm import PDM
from plan.plan_pdm.modelo_pdm_plan import ModeloPDMPlan

class PlanPDM(Planeador):
    
    def __init__(self):
        
        self._gama = 0.9
        self._delta_max = 1
        self._pdm = PDM(self._gama, self._delta_max) 
        self._politica = None
        self._modelo_pdm = None
        self._utilidade = {}
        
        
    def gama(self):
        
        return self._gama
        
        
    def delta_max(self):
        
        return self._delta_max
        
        
    def planear(self, modelo_plan, estado, objectivos):
        
        if(objectivos):
            self._modelo_pdm = ModeloPDMPlan(modelo_plan, objectivos)
            self._politica = self._pdm.resolver(self._modelo_pdm)[1]
            self._utilidade = self._pdm.resolver(self._modelo_pdm)[0]
            
        
    def obter_accao(self, s):
        
        if(self._politica):
            return self._politica[s]
        
        
    def plano_pendente(self):
        
        return self._politica # boolean
        
        
    def terminar_plano(self):
        
        self._politica = None
        
        
    def mostrar(self, vis, estado):
        vis.limpar()
        vis.campo(self._utilidade)
        if(self._politica):
            vis.politica(self._politica)
        vis.marcar([estado], linha = 1)