from plan.planeador import Planeador
from problema_plan import ProblemaPlan

class PlanPEE(Planeador):
    
    def __init__(self, mec_pee):
        
        self._plano = None
        self._mec_pee = mec_pee
        
        
    def planear(self, modelo_plan, estado_inicial, objectivos):
        
        estado_final = objectivos[0]
        operadores = modelo_plan.operadores()
        problema = ProblemaPlan(estado_inicial, estado_final, modelo_plan.operadores())
        solucao = self._mec_pee.resolver(problema)
        if solucao:
            self._plano = [no.operador for no in solucao[1:]]
        
        
    def obter_accao(self, estado):
        
        if(self._plano):
            return self._plano.pop(0)
        
        
    def plano_pendente(self):
        
        return self._plano
        
        
    def terminar_plano(self):
        
        self._plano = None
        
        
    def mostrar(self, vis, estado):
        vis.campo(self._mec_pee.obter_explorados())
        vis.plano(estado, self._plano)
        vis.marcar([estado], linha = 1)