'''
Created on 20/12/2012

@author: Elias
'''

from pandac.PandaModules import *

class Cidade():
    def __init__(self, render):
        self.chao = loader.loadModel("mapa/Modelos/cidade/teste")
        self.chao.reparentTo (render)
        self.chao.setTag("chao","11")
        self.p = []
        for i in range(1,11):
            self.p.append(loader.loadModel("mapa/Modelos/cidade/construcoes-predio"+str(i)))
            self.p[i-1].reparentTo (self.chao)
        #p10 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio11")
        #p10.reparentTo (chao)
        self.chao.setPos(0, 0, 0)
        #chao.setHpr(0, 0, 0) 
    def getNode(self):
        return self.chao