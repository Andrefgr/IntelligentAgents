from ecr.hierarquia import Hierarquia
from controlo_react.reaccoes.explorar import Explorar
from controlo_react.reaccoes.evitar import Evitar
from controlo_react.reaccoes.contornar import Contornar
from controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo

class Recolher(Hierarquia):
    
    
    def __init__(self):
        
        super(Recolher, self).__init__([AproximarAlvo(),Evitar(),Contornar(),Explorar()])  