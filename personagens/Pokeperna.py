# -*- coding: utf-8 -*-
'''
Created on 14/12/2012

@author: Elias
'''
from direct.actor.Actor import Actor
from direct.task import Task
from pandac.PandaModules import VBase3
from panda3d.ai import AICharacter
from panda3d.ai import AIWorld
from personagem import Personagem

class Pokeperna(Personagem):
    def __init__(self,render, colisaoTerreno):
        self.nome = "Pokeperna"
        self.agi = 10
        self.hp = 10
        self.int = 5
        self.str = 1
        self.dano = 5
        self.bloqueio = False
        self.bloqueado = False
        self.velocAtaque = 0.5
        self.arma = None
        self.escudo = None
        self.armadura = None
        self.segueAlvo = None
        self.segue = False
        
        self.pokeperna = Actor('personagens/Modelos/Pokeperna/p1',
                       {"andar" :"personagens/Modelos/Pokeperna/p1-andar.egg",
                       "saltar" :"personagens/Modelos/Pokeperna/p1-saltar.egg",
                       "correr" : "personagens/Modelos/Pokeperna/p1-correr",
                       "abaixar" : "personagens/Modelos/Pokeperna/p1-abaixar"})
#        self.pokeperna = Actor('personagens/Modelos/Pokeperna/p1',
#                       {"atacar" : "personagens/Modelos/pokepernaTeste-atacar"})
        #self.pokeperna.setScale(0.2,0.2,0.2)
        
        self.render = render 
        self.pokeperna.setTag("Pokeperna","1")
                
        #self.pokeperna.reparentTo(self.noRobot)
        self.pokeperna.setPos(-10,-30.0,2.10)
        self.pokeperna.reparentTo(self.render)
        self.gerenciadorColisao = self.pokeperna.getPos()
        self.goForward = 0
        self.goBackwards = 0
        self.goLeft = 0
        self.goRight = 0
        self.saltar = 0
        self.abaixar = 0
        self.prevtime = 0
        self.correr = 0
        self.move = 0
        self.gerenciadorColisao = colisaoTerreno
        self.gerenciarSelecao = 0
        
        self.setAI()
        taskMgr.add(self.gerenciadorSelecao,"gerenciasSelecao")
    
    def pega(self):
        pass
    
    def abre(self):
        pass
    
    def defende(self):
        pass
    
    def calcDefesa(self):
        pass
    
    def atacar(self):
        self.pokeperna.play("saltar")
        
        #self.ataca = atacar

    def setGoLeft (self,value):
        self.goLeft = value
    
    def setGoRight (self,value):
        self.goRight = value
    
    def setGoForward (self,value):
        self.goForward = value
    
    def setMove (self,value):
        self.move = value
        self.aiBehaviors.pathFollow(01.0)
        self.aiBehaviors.addToPath(self.gerenciadorColisao.getEntry(0).getSurfacePoint(self.render))
        self.aiBehaviors.addToPath(self.pokeperna.getPos())
        
        self.pokeperna.loop("correr",)
        #print self.pokeperna.getAnimControl('andar').isPlaying()
        #print self.gerenciadorColisao.getEntry(0).getSurfacePoint(self.render)
        #print posicao
        if self.segue:
            self.aiBehaviors.seek(self.segueAlvo.pokemao)
            self.aiBehaviors.startFollow("actor")
            print "segue"
        else:
            self.aiBehaviors.startFollow("actor")
        #self.aiBehaviors.pathFindTo((self.gerenciadorColisao.getEntry(0).getSurfacePoint(self.render)),"addPath")
        
        #self.move = value
        
    def setGoBackwards (self,value):
        self.goBackwards = value
    
    def setSaltar(self,value):
        self.saltar = value
    
    def setAbaixar(self, value):
        self.abaixar = value
    
    def setCorrer(self, value):
        self.correr = value
    
    def getModel(self):
        return self.pokeperna
    
    def getPos(self):
        return self.pokeperna.getPos()
    
    
    def update (self, time,traverser,robotGroundHandler):
        elapsed = time - self.prevtime
        
        if self.goLeft:
            self.pokeperna.setH(self.pokeperna.getH() + elapsed * 300)
        if self.goRight:
            self.pokeperna.setH(self.pokeperna.getH() - elapsed * 300)


    # this code moves the avatar forward.
    # "forward" usually means "along the Y axis".  however, since the avatar can turn, 
    # it really means "along the Y axis relative to the direction I'm facing"
    # you can use the getRelativeVector () function to find out what that is
    
        forwardVec =  VBase3(0,-1,0)
        xformedVec = self.render.getRelativeVector(self.pokeperna,forwardVec)
        para = True
        oldPos = self.pokeperna.getPos()
       
        if self.goForward:
            para = False
            if not self.pokeperna.getAnimControl('andar').isPlaying() \
                and not self.pokeperna.getAnimControl('saltar').isPlaying() \
                and not self.abaixar:
                    self.pokeperna.loop("andar",restart = 0)  
            newPos = oldPos + xformedVec * elapsed * 5
            self.pokeperna.setPos(newPos)
      
        if self.goBackwards:
            newPos = oldPos - xformedVec * elapsed * 5
            self.pokeperna.setPos(newPos)   
        
        if self.correr:
            para = False
            if not self.pokeperna.getAnimControl('correr').isPlaying() \
                and not self.pokeperna.getAnimControl('saltar').isPlaying() \
                and not self.abaixar:
                    self.pokeperna.loop("correr",restart = 0)  
            newPos = oldPos + xformedVec * elapsed * 7
            self.pokeperna.setPos(newPos)
    
        if self.saltar:
            para = False
            if not self.pokeperna.getAnimControl('saltar').isPlaying():
                self.pokeperna.play("saltar")
                
        if self.abaixar:
            para = False
            if not self.pokeperna.getAnimControl('abaixar').isPlaying():
                self.pokeperna.play("abaixar")
        
        if para:
#            if not self.pokeperna.getAnimControl('saltar').isPlaying():
                self.pokeperna.stop()
        
        # do collisions
        traverser.traverse(self.render)

        startpos = self.pokeperna.getPos()
        
        entries = []
        for i in range(robotGroundHandler.getNumEntries()):
            entry = robotGroundHandler.getEntry(i)
            entries.append(entry)
        entries.sort(lambda x,y: cmp(y.getSurfacePoint(self.render).getZ(),
                                     x.getSurfacePoint(self.render).getZ()))
    
        if (len(entries)>0) and (entries[0].getIntoNode().getName() == "Grid"):
            self.pokeperna.setZ(entries[0].getSurfacePoint(self.render).getZ())
            #print entries[0].getSurfacePoint(self.render).getZ(),self.pokeperna.getPos()
        #self.pokeperna.setZ(1000)
        else:
            self.pokeperna.setPos(startpos)
      
        self.prevtime = time
        return Task.cont
    
    def setAI(self):
        #Creating AI World
        self.AIworld = AIWorld(self.render)
 
        self.AIchar = AICharacter("pokeperna",self.pokeperna, 60, 0.05, 5)
        self.AIworld.addAiChar(self.AIchar)
        self.aiBehaviors = self.AIchar.getAiBehaviors()
        #self.aiBehaviors.initPathFind("mapa/Modelos/cidade/navmesh.csv")
 
        #Path follow (note the order is reveresed)
        #AI World update
        taskMgr.add(self.AIUpdate,"AIUpdate")
    
    def gerenciadorSelecao(self, task):
        
        return Task.cont
    
    def AIUpdate(self,task):
        #print self.pokeperna.getAnimControl('andar').isPlaying()
        if self.move and self.aiBehaviors.behaviorStatus("pathfollow") == "done":
#            if not self.pokeperna.getAnimControl('andar').isPlaying():
#                print "anda"
#                self.pokeperna.loop("andar",restart = 0)
            #print "gerenciadorColisao",self.gerenciadorColisao.getEntry(0).getSurfacePoint(self.render)
            #print "pokeperna",self.pokeperna.getPos()
            self.pokeperna.stop()
            self.pokeperna.pose("andar",0)
            
            #print "andando"
        else:
            pass
            #print "parado", self.move
#            self.pokeperna.stop()
#            self.pokeperna.pose("andar",0)
        self.AIworld.update()            
        return Task.cont