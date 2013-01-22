'''
Created on 16/01/2013

@author: Elias
'''
from personagem import Personagem
from pokemao import Pokemao

class Inimigos(Personagem):
    def __init__(self, mapa, dificuldade, num_jogadores):
        self.mapa = mapa
        self.dificuldade = dificuldade
        self.num_jogadores = num_jogadores
        
    def setInimigos(self,render):
        self.pokemao = Pokemao(render)
        
        