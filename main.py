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
##################
class World(DirectObject):
    def __init__(self):
        
        #configuracoes de tela
        altura = base.pipe.getDisplayHeight()
        largura = base.pipe.getDisplayWidth()
        
        wp = WindowProperties()
        #wp.setSize(largura, altura)
        #wp.setFullscreen(True)
        
        base.win.requestProperties(wp)
        
        
        self.controleMouse = ControleMouse(render, base.camera)
        
        
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
        
        self.robot = Pokeperna(render)
        
        self.controleItens = controle.Controleitens() 
        self.controleItens.setItensAleatorios(self.robot)
        self.controleItens.setItensAleatorios(self.inimigos.pokemao)
        
        #enumerar modelos
        #print self.inimigos.pokemao.pokemao.setTag("isso","2")
        #decobre qual  melo
        #print self.inimigos.pokemao.pokemao.getTag("isso")
    
        # self.robot.reparentTo(self.noRobot)
        # self.robot.setPos(-10,0,1.9)
        # self.robot.reparentTo(render)
   
        self.wall = Mapa(render)
        self.wall.load(1)
        base.disableMouse()
    
        base.cTrav = CollisionTraverser('collision traverser')
        self.traverser = base.cTrav
        # collision setup for the robot
        self.robotcolnp = CollisionNode('colNode')
        # fromObject = self.robot.attachNewNode()
        # fromObject.node().addSolid(CollisionRay(0, 0, 0, 0, 0, 0.1))
        self.robotcolnp.addSolid(CollisionRay(0, 0, 2, 0, 0, -0.1))
        self.noRobot = self.robot.getModel().attachNewNode(self.robotcolnp)
        self.noRobot.setPos(0, 0, -5)
        self.noRobot.show()
        self.robotGroundHandler = CollisionHandlerQueue()
        # self.traverser.addCollider(fromObject, self.robotGroundHandler)
        self.traverser.addCollider(self.noRobot, self.robotGroundHandler)

    
        self.lifter = CollisionHandlerFloor()
        self.lifter.setMaxVelocity(100)
        # self.lifter.addCollider(fromObject, self.robot)
        # set up keyboard controls
    
        self.move = 0


        self.accept ("a", self.robot.setGoLeft, [1])
        self.accept ("a-up", self.robot.setGoLeft, [0])
        
        self.accept ("A", self.robot.setGoLeft, [1])
        self.accept ("A-up", self.robot.setGoLeft, [0])
    
        self.accept ("d", self.robot.setGoRight, [1])
        self.accept ("d-up", self.robot.setGoRight, [0])
    
        self.accept ("w", self.robot.setGoForward, [1])
        self.accept ("w-up", self.robot.setGoForward, [0])
  
        self.accept ("s", self.robot.setGoBackwards, [1])
        self.accept ("s-up", self.robot.setGoBackwards, [0])
    
        self.accept ("space", self.robot.setSaltar, [1])
        self.accept ("space-up", self.robot.setSaltar, [0])
        
        self.accept ("shift", self.robot.setCorrer, [1])
        self.accept ("shift-up", self.robot.setCorrer, [0])
        
        self.accept ("control", self.robot.setAbaixar, [1])
        self.accept ("control-up", self.robot.setAbaixar, [0])
        
        
        self.accept ("mouse1", self.setMove, [1])
        self.accept ("mouse1-up", self.setMove, [0])
        
        self.render = render

        # set up update task
        self.prevtime = 0
        taskMgr.add(self.update, "updateTask")
        taskMgr.add(self.cameraTask, "cameraTask")
        taskMgr.add(self.mouseTask, "mouseTask")
    
    
    
    def setGoLeft (self, value):
        self.robot().goLeft= value
    
    def setGoRight (self, value):
        self.robot().goRight =value 
    
    def setGoForward (self, value):
        self.robot().setGoForward(value)
    
    def setMove (self, value):
        #print "definido"
        if value == 1:
            if self.controleMouse.pq.getNumEntries() > 0: 
                #print self.controleMouse.pq.getEntries()[0].getSurfacePoint(self.render)
                self.robot.setMove(True,self.controleMouse.pq)
        else:
            self.robot.move = False
        #print "definido agora"
    
    def setGoBackwards (self, value):
        self.robot().setGoBackwards(value)
        
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
            self.controleMouse.pst.traverse(self.wall.mapa.getNode()) 
#            print self.Mouseload.pq.getEntry(0) 
#            print self.Mouseload.pq.getNumEntries() 
            if self.controleMouse.hqp.getNumEntries() > 0: 
                #if we have hit something, sort the hits so that the closest is first, and highlight that node 
                self.controleMouse.hqp.sortEntries()
            
            if (self.controleMouse.hqp.getNumEntries()>0) and (self.controleMouse.hqp.getEntries()[0].getIntoNode().getName() == "Pokeperna"): 
                print "aqui"
       
        return Task.cont 
        
        # update task
    def cameraTask(self, task):
        pos  = self.robot.getModel().getPos()
        pos.z = pos.z+40
        pos.y = pos.y-30
        base.camera.setPos(pos)
        base.camera.lookAt(self.robot.getModel())
        base.camera.setP(-50)
        return Task.cont
        #base.camera.setPosZ(base.camera.getPosZ()+10) 
        
    def update (self, task):
    
        self.robot.update(task.time, self.traverser, self.robotGroundHandler)
      
        self.prevtime = task.time
        return Task.cont

d = World()
run()
