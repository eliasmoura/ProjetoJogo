'''
Created on 22/01/2013

@author: Elias
'''

import math
from direct.task import Task

class Combate():
    def __init__(self,de = None,para=None):
        self.de = de
        self.para = para
        #taskMgr.add(self.gerenciadorSelecao,"gerenciasSelecao")
    
    
    def atacar(self, de, para):
        dePos = de.getPos()
        paraPos = para.getPos()
        distancia = math.sqrt(math.fabs(math.pow((paraPos.getX() - dePos.getX()),2)) +  
                              math.fabs(math.pow((paraPos.getY() - dePos.getY()),2)) + 
                              math.fabs(math.pow((paraPos.getZ() - dePos.getZ()),2)))
        print "distancia",distancia
        if distancia < 10:
            
            if para.bloqueio:
                if para.escudo != None:
                    para.bloqueado = True
                elif para.arma != None:
                    para.bloqueado = True
                else:
                    para.bloqueado = False
            de.atacar()
            self.calcularDanoSofrido(de, para)
        else:
            de.segue = True
            de.segueAlvo = para
    
    
    def calcularDanoSofrido(self, de, para):
        if not para.bloqueado:
            danoSofrido = para.armadura.defesa - de.dano
            if  danoSofrido < 0:
                para.hp = para.hp + danoSofrido  
        