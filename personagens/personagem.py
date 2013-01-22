'''
Created on 16/01/2013

@author: Elias
'''

class Personagem():
    def __init__(self):
        self.nome = None
        self.agi = 10
        self.int = 5
        self.str = 1
        self.dano = 0
        self.bloqueio = False
        self.bloqueado = False
        self.velocAtaque = 0
        self.arma = None
        self.escudo = None
        self.armadura = None
        
        
    def defende(self):
        pass
    
    def calcDefesa(self):
        pass
    
    def calcDano(self):
        self.dano = self.arma.dano + (self.agi * self.arma.infAgi) + (self.int * self.arma.infInt) + (self.str * self.arma.infStr)