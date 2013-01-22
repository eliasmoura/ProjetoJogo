'''
Created on 22/01/2013

@author: Elias
'''
class Controleitens():    
    def setItensAleatorios(self, personagem):
        personagem.arma = Facas()
        personagem.armadura = Courinho()

from itens.armaduras.courinho import Courinho
from itens.armas.facas import Facas