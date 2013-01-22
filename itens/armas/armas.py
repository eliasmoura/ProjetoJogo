'''
Created on 22/01/2013

@author: Elias
'''
from itens.items import Items

class Arma(Items):
    def __init__(self):
        self.dano = None
        self.infAgi = None #quanto o atributo influencia no calculo de dano
        self.infInt = None #quanto o atributo influencia no calculo de dano
        self.infStr = None #quanto o atributo influencia no calculo de dano 
