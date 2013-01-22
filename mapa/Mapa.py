# -*- coding: utf-8 -*-
'''
Created on 14/12/2012

@author: Elias
'''
from Cidade import Cidade


class Mapa():
    def __init__(self,render):
        self.render = render
        self.mapa = None
        
    def load(self, mapa):
        if mapa == 1:
            self.mapa = Cidade(self.render)
            