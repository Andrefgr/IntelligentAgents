import sys

sys.path.append("../lib")
sys.path.append("../agente_prosp")

import psa

from psa import *
from agenteProspector import AgenteProspector
from controlo_delib.controlo_delib import ControloDelib
from controlo_react.reaccoes.recolher import Recolher

from ecr.comportamento import Comportamento
from ecr.resposta import Resposta

from pee.melhorprim.procura_aa import ProcuraAA
from plan.plan_pdm.plan_pdm import PlanPDM

planeador = PlanPDM()
controlo = ControloDelib(planeador)
agente = AgenteProspector(controlo)

psa.iniciar("amb/amb1.das", alvo_ini = True, detalhe = 1)
psa.executar(agente)