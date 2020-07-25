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

from pee.prof.procura_prof import ProcuraProf
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.larg.procura_larg import ProcuraLarg

from pee.melhorprim.procura_aa import ProcuraAA
from pee.melhorprim.procura_custo_unif import ProcuraCustoUnif
from pee.melhorprim.procura_sofrega import ProcuraSofrega

from plan.plan_pee.plan_pee import PlanPEE

# mec_procura = ProcuraAA()
# mec_procura = ProcuraLarg()
# mec_procura = ProcuraProf()
# mec_procura = ProcuraCustoUnif()
# mec_procura = ProcuraProfIter()
mec_procura = ProcuraSofrega()
planeador = PlanPEE(mec_procura)
controlo = ControloDelib(planeador)
agente = AgenteProspector(controlo)

psa.iniciar("amb/amb3.das", perexec=0.25, alvo_ini = True)
psa.executar(agente)