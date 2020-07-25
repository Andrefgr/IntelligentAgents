from plan.modelo_plan import ModeloPlan
from operador_mover import OperadorMover
from psa.util import dirmov

class ModeloMundo(ModeloPlan):
    
    
    def __init__(self):
        
        self._alterado = False
        self._elementos = []
        self._estado = None
        self._estados = []
        self._operadores = [OperadorMover(self, direccao) for direccao in dirmov()]
    
    
    def actualizar(self, percepcao):
        
        self._estado = percepcao.posicao
        
        if(self._elementos != percepcao.imagem):

            self._elementos = percepcao.imagem
            self._estados = percepcao.imagem.keys()
            self.alterado = True
            
        else:
            
            self.alterado = False
        
        
    def obter_elem(self, estado):
        
        return self._elementos.get(estado)
        
        
    @property
    def alterado(self):
        
        return self._alterado
        
        
    @property
    def estado(self):
        
        return self._estado
        
        
    def estados(self):
        
        return self._estados
        
        
    def operadores(self):
        
        return self._operadores
        
        
    def mostrar(self, vis):
        alvos_obst = {k : v for (k, v) in self._elementos.items() if v in ['alvo', 'obst']}
        vis.elementos(alvos_obst)