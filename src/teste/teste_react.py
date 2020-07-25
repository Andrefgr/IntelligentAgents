import sys

sys.path.append("../lib")
sys.path.append("../agente_prosp")

import psa

from psa import *
from agente_prospector import AgenteProspector
from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.recolher import Recolher

from ecr.comportamento import Comportamento
from ecr.resposta import Resposta

comportamento = Recolher()
controlo = ControloReact(comportamento)
agente = AgenteProspector(controlo)

psa.iniciar("amb/amb1.das")
psa.executar(agente)