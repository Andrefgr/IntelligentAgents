import pygame
import psa
from psa.agente import Agente
from psa.accao import Avancar
from psa.accao import Mover
from psa.accao import Rodar
from psa.actuador import ESQ
from psa.actuador import FRT
from psa.actuador import DIR

from ecr.reaccao import Reaccao
from ecr.resposta import Resposta
from random import choice

class AproximarAlvoDir(Reaccao):
    
    def __init__(self, direc):
        self.direc = direc
    
    def _detectar_estimulo(self,percepcao):
        if (percepcao[self.direc].alvo):
            return (percepcao[self.direc].distancia)
        
    def _gerar_resposta(self,estimulo):
        accao = Mover(self.direc)
        p = 1/(1+estimulo)
        
        return Resposta(accao, p)