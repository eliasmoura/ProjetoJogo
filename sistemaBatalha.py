'''
Created on 22/01/2013

@author: Elias
'''

class Combate():
    def __init__(self):
        pass
    
    
    def ataque(self, atacante, atacado):
        if atacado.bloqueio:
            if atacado.escudo != None:
                atacado.bloqueado = True
            elif atacado.arma != None:
                atacado.bloqueado = True
        else:
            atacado.bloqueado = False
    
    
    def calcularDanoSofrido(self, atacante, atacado):
        danoSofrido = atacado.armadura.defesa - atacante.dano
        if  danoSofrido < 0:
            atacado.hp = atacado.hp - danoSofrido  
        