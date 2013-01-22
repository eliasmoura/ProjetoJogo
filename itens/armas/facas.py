# -*- coding: utf-8 -*-
'''
Created on 14/12/2012

@author: Elias
'''

from itens.armas.armas import Arma

class Facas(Arma):
    def __init__(self):
        self.nome = "joao"
        self.propriedadeMagica = None
        self.intReq = 0
        self.strReq = 0
        self.agiReq = 0
        self.integridade = 5
        self.dano = 2
        self.infAgi = 0.9
        self.infInt = 0
        self.infStr = 0.1
    