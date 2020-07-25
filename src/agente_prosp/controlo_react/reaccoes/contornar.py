from random import choice

from psa.accao import Mover
from psa.actuador import ESQ, FRT, DIR
from ecr.reaccao import Reaccao
from ecr.resposta import Resposta

class Contornar(Reaccao):
    
    def _detectar_estimulo(self, percepcao):
        return((percepcao[DIR].obstaculo and percepcao[DIR].contacto) or 
                (percepcao[ESQ].obstaculo and percepcao[ESQ].contacto))
        
    def _gerar_resposta(self, estimulo):
        
        if estimulo:
            accao = Mover(FRT)
            return Resposta(accao)