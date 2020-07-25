import random
from psa.accao import Mover
from psa.actuador import ESQ, FRT, DIR
from ecr.comportamento import Comportamento
from ecr.resposta import Resposta

class Explorar(Comportamento):
    
    def activar(self, percepcao):
        
        accao = random.choice([Mover(ESQ), Mover(FRT), Mover(DIR)])
        return Resposta(accao)