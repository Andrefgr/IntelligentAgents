import sys

sys.path.append("../lib")
sys.path.append("../agente_prosp")

import psa

from psa import *
from agenteProspector import AgenteProspector
from controlo_aprend.controlo_aprend_ref import ControloAprendRef

psa.iniciar("amb/amb3.das", alvo_ini = True)

controlo = ControloAprendRef()
agente = AgenteProspector(controlo)

psa.executar(agente)