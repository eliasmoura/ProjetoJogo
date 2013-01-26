# -*- coding: utf-8 -*-

'''
Created on 14/12/2012

@author: Elias
'''

from panda3d.core import loadPrcFile
loadPrcFile("./config.prc")

import direct.directbase.DirectStart
from pandac.PandaModules import *
import random
from direct.task import Task
from direct.showbase.DirectObject import DirectObject
from direct.actor import Actor
from personagens.Pokeperna import Pokeperna
from mapa.Mapa import Mapa
from mouseLoad import ControleMouse
from personagens.inimigos import Inimigos

from panda3d.core import ConfigVariableString
from interface.personagemStatus import Personagem
from itens import controle
from sistemaBatalha import Combate
##################
class World(DirectObject):
    def __init__(self):
        self.base = base
        self.render = render
        #configuracoes de tela
        altura = base.pipe.getDisplayHeight()
        largura = base.pipe.getDisplayWidth()
        
        wp = WindowProperties()
        #wp.setSize(largura, altura)
        #wp.setFullscreen(True)
        
        base.win.requestProperties(wp)
        
        
        self.controleMouse = ControleMouse(self.render, base.camera)
        
        
        light1 = PointLight ('light1')
        lightNode1 = render.attachNewNode (light1)
        lightNode1.setPos(0, -20, 50)
        render.setLight(lightNode1)
        
        self.perStatus = Personagem(render)
        self.perStatus.hp(base)
        
        self.inimigos = Inimigos(1,0,1)
        self.inimigos.setInimigos(render)
        # base.disableMouse()
        # sss = Pokeperna(11)
      
        DirectObject.window_title = "Pokeperna"
        
        self.wall = Mapa(render)
        self.wall.load(1)
        self.base.disableMouse()
        
        self.pokeperna = Pokeperna(render,self.controleMouse.pq)
        
        self.controleItens = controle.Controleitens() 
        self.controleItens.setItensAleatorios(self.pokeperna)
        self.controleItens.setItensAleatorios(self.inimigos.pokemao)
        
        #enumerar modelos
        #print self.inimigos.pokemao.pokemao.setTag("isso","2")
        #decobre qual  melo
        #print self.inimigos.pokemao.pokemao.getTag("isso")
    
        # self.pokeperna.reparentTo(self.noRobot)
        # self.pokeperna.setPos(-10,0,1.9)
        # self.pokeperna.reparentTo(render)
   
        base.cTrav = CollisionTraverser('collision traverser')
        self.traverser = base.cTrav
        # collision setup for the pokeperna
        self.robotcolnp = CollisionNode('colNode')
        # fromObject = self.pokeperna.attachNewNode()
        # fromObject.node().addSolid(CollisionRay(0, 0, 0, 0, 0, 0.1))
        self.robotcolnp.addSolid(CollisionRay(0, 0, 2, 0, 0, -0.1))
        self.noRobot = self.pokeperna.getModel().attachNewNode(self.robotcolnp)
        self.noRobot.setPos(0, 0, -5)
        self.noRobot.show()
        self.robotGroundHandler = CollisionHandlerQueue()
        # self.traverser.addCollider(fromObject, self.robotGroundHandler)
        self.traverser.addCollider(self.noRobot, self.robotGroundHandler)

    
        self.lifter = CollisionHandlerFloor()
        self.lifter.setMaxVelocity(100)
        # self.lifter.addCollider(fromObject, self.pokeperna)
        # set up keyboard controls
    
        self.move = 0
        
        self.sistemaBatalha = Combate()

        self.accept ("a", self.pokeperna.setGoLeft, [1])
        self.accept ("a-up", self.pokeperna.setGoLeft, [0])
        
        self.accept ("A", self.pokeperna.setGoLeft, [1])
        self.accept ("A-up", self.pokeperna.setGoLeft, [0])
    
        self.accept ("d", self.pokeperna.setGoRight, [1])
        self.accept ("d-up", self.pokeperna.setGoRight, [0])
    
        self.accept ("w", self.pokeperna.setGoForward, [1])
        self.accept ("w-up", self.pokeperna.setGoForward, [0])
  
        self.accept ("s", self.pokeperna.setGoBackwards, [1])
        self.accept ("s-up", self.pokeperna.setGoBackwards, [0])
    
        self.accept ("space", self.pokeperna.setSaltar, [1])
        self.accept ("space-up", self.pokeperna.setSaltar, [0])
        
        self.accept ("shift", self.pokeperna.setCorrer, [1])
        self.accept ("shift-up", self.pokeperna.setCorrer, [0])
        
        self.accept ("control", self.pokeperna.setAbaixar, [1])
        self.accept ("control-up", self.pokeperna.setAbaixar, [0])
        
        
        self.accept ("mouse1", self.setMove, [1])
        self.accept ("mouse1-up", self.setMove, [0])
        
        

        # set up update task
        self.prevtime = 0
        taskMgr.add(self.update, "updateTask")
        taskMgr.add(self.cameraTask, "cameraTask")
        taskMgr.add(self.mouseTask, "mouseTask")
    
    
    
    def setGoLeft (self, value):
        self.pokeperna().goLeft= value
    
    def setGoRight (self, value):
        self.pokeperna().goRight =value 
    
    def setGoForward (self, value):
        self.pokeperna().setGoForward(value)
    
    def setMove (self, value):
        #print "definido"
        if base.mouseWatcherNode.hasMouse() and value:
            mPos = base.mouseWatcherNode.getMouse()
            self.controleMouse.pickerRayObj.setFromLens(base.camNode,
                                                    mPos.getX(),
                                                    mPos.getY())
            self.controleMouse.pst.traverse(self.render)
            if (self.controleMouse.hqp.getNumEntries() > 0):
                self.controleMouse.hqp.sortEntries()
                entry = self.controleMouse.hqp.getEntry(0)
                selecao = entry.getIntoNodePath()
                if not selecao.isEmpty():
                    #print "sim"
                    pos = entry.getSurfacePoint(self.render)
                    personagem = entry.getIntoNodePath().getNetTag("inimigo")
                    print personagem
                    #print pos, "objeto:", personagem#, "tipo:", type( personagem)
                    if  personagem:
                        self.sistemaBatalha.atacar(self.pokeperna, self.inimigos.getInimigos(personagem))
                        print "pokeperna:", self.pokeperna.hp, "pokemao:", self.inimigos.getInimigos(personagem).hp
                        print "atacar"
                    
                
        if self.controleMouse.pq.getNumEntries() > 0 and value: 
            #print self.controleMouse.pq.getEntries()[0].getSurfacePoint(self.render)
            self.pokeperna.setMove(True)
        else:
            self.pokeperna.move = False
        #print "definido agora"
    
    def setGoBackwards (self, value):
        self.pokeperna().setGoBackwards(value)
        
    def mouseTask(self, task): 
        #Check to see if we can access the mouse. We need it to do anything else 
        if base.mouseWatcherNode.hasMouse(): 
            #get the mouse position 
            mpos = base.mouseWatcherNode.getMouse() 
      
            #Set the position of the ray based on the mouse position 
            self.controleMouse.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY()) 
            
            #Do the actual collision pass (Do it only on the terrain for efficiency purposes) 
            self.controleMouse.picker.traverse(self.wall.mapa.getNode()) 
#            print self.Mouseload.pq.getEntry(0) 
#            print self.Mouseload.pq.getNumEntries() 
            if self.controleMouse.pq.getNumEntries() > 0: 
                #if we have hit something, sort the hits so that the closest is first, and highlight that node 
                self.controleMouse.pq.sortEntries()
                #print dir(self.controleMouse.pq.getEntries()[0])
                #print self.controleMouse.pq.getEntries()[0].getSurfacePoint(self.render)
                #print "Hit"
        if base.mouseWatcherNode.hasMouse(): 
            #get the mouse position 
            mpos = base.mouseWatcherNode.getMouse() 
      
            #Set the position of the ray based on the mouse position 
            self.controleMouse.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY()) 
            
            #Do the actual collision pass (Do it only on the terrain for efficiency purposes) 
            #self.controleMouse.pst.traverse(self.wall.mapa.getNode()) 
#            print self.Mouseload.pq.getEntry(0) 
#            print self.Mouseload.pq.getNumEntries() 
            #if self.controleMouse.hqp.getNumEntries() > 0: 
                #if we have hit something, sort the hits so that the closest is first, and highlight that node 
                #self.controleMouse.hqp.sortEntries()
            
            #if (self.controleMouse.hqp.getNumEntries()>0) and (self.controleMouse.hqp.getEntries()[0].getIntoNode().getName() == "Pokeperna"): 
                #print "aqui"
       
        return Task.cont 
        
        # update task
    def cameraTask(self, task):
        pos  = self.pokeperna.getModel().getPos()
        pos.z = pos.z+40
        pos.y = pos.y-30
        base.camera.setPos(pos)
        base.camera.lookAt(self.pokeperna.getModel())
        base.camera.setP(-50)
        return Task.cont
        #base.camera.setPosZ(base.camera.getPosZ()+10) 
        
    def update (self, task):
    
        self.pokeperna.update(task.time, self.traverser, self.robotGroundHandler)
      
        self.prevtime = task.time
        return Task.cont

d = World()
run()
