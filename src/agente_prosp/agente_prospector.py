# -*- coding: utf-8 -*-

from psa.agente import Agente
                        
"""
Classe herda de Agente, classes com herança têm (superclass) a seguir ao nome.

Interfaces não existem em Python, portanto não são criadas.
"""
        
class AgenteProspector(Agente):
    
    def __init__(self, controlo):
        
        self.controlo = controlo
        
    def executar(self):
        
        percepcao = self._percepcionar()
        accao = self._processar(percepcao)
        if(accao is not None):
            self._actuar(accao)
        
    def _percepcionar(self):
        
        return self.sensor_multiplo.detectar()
        
    def _processar(self, percepcao):
        
        return self.controlo.processar(percepcao)
        
    def _actuar(self, accao):
        
        self.actuador.actuar(accao)