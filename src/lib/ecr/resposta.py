# -*- coding: utf-8 -*-
class Resposta:
    
    @property
    def accao(self):
        
        return self._accao
        
    @property
    def prioridade(self):
        
        return self._prioridade
        
    def __init__(self, accao, prioridade = 0): # prioridade = 0 cria 
                                               # valor por omissão.
        self._accao = accao
        self._prioridade = prioridade