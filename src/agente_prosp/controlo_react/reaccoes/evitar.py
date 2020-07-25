from random import choice

from psa.accao import Rodar
from psa.actuador import ESQ, FRT, DIR
from ecr.reaccao import Reaccao
from ecr.resposta import Resposta

class Evitar(Reaccao):
    
    def _detectar_estimulo(self, percepcao):
        return(percepcao[FRT].obstaculo and percepcao[FRT].contacto)
        
    def _gerar_resposta(self, estimulo):
        
        accao = Rodar(DIR)
        return Resposta(accao)