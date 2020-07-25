from modelo_mundo import ModeloMundo
from controlo_react.controlo import Controlo
import psa

class ControloDelib(Controlo):  
            
    def __init__(self, planeador):
        
        self._planeador = planeador
        self._modelo_mundo = ModeloMundo()
        self._objectivos = None
        
        
    def processar(self, percepcao):
        
        self._assimilar(percepcao)
        
        reconsiderar = self._reconsiderar()
        
        if(reconsiderar):
            
            self._deliberar()
            self._planear()
            
        accao = self._executar()

        self.mostrar()
            
        return accao
       
         
    def _assimilar(self, per):
        
        self._modelo_mundo.actualizar(per)
        
        
    def _reconsiderar(self):
        
        return (not self._planeador.plano_pendente() or self._modelo_mundo.alterado or not self._objectivos)
        
        
    def _deliberar(self):
        
        self._objectivos = [estado for estado in self._modelo_mundo.estados() if self._modelo_mundo.obter_elem(estado) == 'alvo']
        
        
    def _planear(self):
        
        if self._objectivos:
            self._planeador.planear(self._modelo_mundo, self._modelo_mundo.estado, self._objectivos)
        
        
    def _executar(self):
        
        if(self._objectivos):
            operador = self._planeador.obter_accao(self._modelo_mundo.estado)
            
            if(operador is not None):
                
                return operador.accao
        
        else:
            self._planeador.terminar_plano()
            
            
    def mostrar(self):
   
        vis = psa.vis(1)
        vis.limpar()
        self._planeador.mostrar(vis, self._modelo_mundo.estado)
        self._modelo_mundo.mostrar(vis)