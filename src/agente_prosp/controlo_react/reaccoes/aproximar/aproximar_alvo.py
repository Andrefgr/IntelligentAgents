import pygame
import psa
from psa.agente import Agente
from psa.accao import Avancar
from psa.accao import Mover
from psa.accao import Rodar
from psa.actuador import ESQ, FRT, DIR

from ecr.reaccao import Reaccao
from ecr.prioridade import Prioridade
from random import choice

from controlo_react.reaccoes.aproximar.aproximar_alvo_dir import AproximarAlvoDir

class AproximarAlvo(Prioridade):
    
    def __init__(self):
        
        super(AproximarAlvo, self).__init__(
             [AproximarAlvoDir(ESQ), 
              AproximarAlvoDir(FRT), 
              AproximarAlvoDir(DIR)])