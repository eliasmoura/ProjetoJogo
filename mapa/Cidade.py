'''
Created on 20/12/2012

@author: Elias
'''

from pandac.PandaModules import *

class Cidade():
    def __init__(self, render):
        self.chao = loader.loadModel("mapa/Modelos/cidade/teste")
        self.p1 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio1")
        self.p2 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio2")
        self.p3 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio3")
        self.p4 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio4")
        self.p5 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio5")
        self.p6 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio6")
        self.p7 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio7")
        self.p8 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio8")
        self.p9 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio9")
        self.p10 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio10")
        #p10 = loader.loadModel("mapa/Modelos/cidade/construcoes-predio11")
        self.chao.reparentTo (render)
        self.p1.reparentTo (self.chao)
        self.p2.reparentTo (self.chao)
        self.p3.reparentTo (self.chao)
        self.p4.reparentTo (self.chao)
        self.p5.reparentTo (self.chao)
        self.p6.reparentTo (self.chao)
        self.p7.reparentTo (self.chao)
        self.p8.reparentTo (self.chao)
        self.p9.reparentTo (self.chao)
        self.p10.reparentTo (self.chao)
        #p10.reparentTo (chao)
        self.chao.setPos(0, 0, 0)
        #chao.setHpr(0, 0, 0) 
    def getNode(self):
        return self.chao