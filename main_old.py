'''
Created on 17/12/2012

@author: Elias
'''
# -*- coding: utf-8 -*-

'''
Created on 14/12/2012

@author: Elias
'''

import direct.directbase.DirectStart
from pandac.PandaModules import *
import random
from direct.task import Task
from direct.showbase import DirectObject
from direct.actor import Actor


##################
class World(DirectObject.DirectObject):
  def __init__(self):
    
    light1 = PointLight ('light1')
    lightNode1 = render.attachNewNode (light1)
    lightNode1.setPos(0,-20,50)
    render.setLight(lightNode1)
    
    #base.disableMouse()
    self.robot = Actor.Actor('personagens/Modelos/Pokeperna/p1',
                       {"run":"personagens/Modelos/Pokeperna/p1-correr.egg",
                       "jump":"personagens/Modelos/Pokeperna/p1-saltar.egg"})
    self.robot.setScale(0.2,0.2,0.2)
    
    #self.robot.reparentTo(self.noRobot)
    self.robot.setPos(-10,0,1.9)
    self.robot.reparentTo(render)
   
    wall1 = loader.loadModel("mapa/Modelos/terreno2")
    wall1.reparentTo (render)
    wall1.setPos(0,0,0)
    wall1.setHpr(0,0,0) 

    base.camera.setPos(0,-20,8)
    base.camera.lookAt(self.robot)

  
    
    base.cTrav = CollisionTraverser('collision traverser')
    self.traverser = base.cTrav
    # collision setup for the robot
    self.robotcolnp = CollisionNode('colNode')
    #fromObject = self.robot.attachNewNode()
    #fromObject.node().addSolid(CollisionRay(0, 0, 0, 0, 0, 0.1))
    self.robotcolnp.addSolid(CollisionRay(0, 0, 2, 0, 0,-0.1))
    self.noRobot = self.robot.attachNewNode(self.robotcolnp)
    self.noRobot.setPos(0,0,0)
    self.noRobot.show()
    self.robotGroundHandler = CollisionHandlerQueue()
    #self.traverser.addCollider(fromObject, self.robotGroundHandler)
    self.traverser.addCollider(self.noRobot, self.robotGroundHandler)

    
    self.lifter = CollisionHandlerFloor()
    self.lifter.setMaxVelocity(100)
    #self.lifter.addCollider(fromObject, self.robot)
    # set up keyboard controls
    
    self.goForward=0
    self.goBackwards=0
    self.goLeft=0
    self.goRight=0


    self.accept ("arrow_left", self.setGoLeft, [1])
    self.accept ("arrow_left-up", self.setGoLeft, [0])
    
    self.accept ("arrow_right", self.setGoRight, [1])
    self.accept ("arrow_right-up", self.setGoRight, [0])
    
    self.accept ("arrow_up", self.setGoForward, [1])
    self.accept ("arrow_up-up", self.setGoForward, [0])
  
    self.accept ("arrow_down", self.setGoBackwards, [1])
    self.accept ("arrow_down-up", self.setGoBackwards, [0])
    
    #self.accept ("


    # set up update task
    self.prevtime = 0
    taskMgr.add(self.update,"updateTask")
    
    
    
  def setGoLeft (self,value):
    self.goLeft = value
    
  def setGoRight (self,value):
    self.goRight = value
    
  def setGoForward (self,value):
    self.goForward = value
    
  def setGoBackwards (self,value):
    self.goBackwards = value

        
  # update task
  
  def update (self, task):
    
    elapsed = task.time - self.prevtime
    
    if self.goLeft:
      self.robot.setH(self.robot.getH() + elapsed * 300)
    if self.goRight:
      self.robot.setH(self.robot.getH() - elapsed * 300)





    # this code moves the avatar forward.
    # "forward" usually means "along the Y axis".  however, since the avatar can turn, 
    # it really means "along the Y axis relative to the direction I'm facing"
    # you can use the getRelativeVector () function to find out what that is
    
    forwardVec =  VBase3(0,-1,0)
    xformedVec = render.getRelativeVector(self.robot,forwardVec)
    
    oldPos = self.robot.getPos()
    if self.goForward:  
      newPos = oldPos + xformedVec * elapsed * 5
      self.robot.setPos(newPos)
      
    if self.goBackwards:
      
      newPos = oldPos - xformedVec * elapsed * 5
      self.robot.setPos(newPos)   
      
    # do collisions
    
    self.traverser.traverse(render)

    startpos = self.robot.getPos()
        
    entries = []
    for i in range(self.robotGroundHandler.getNumEntries()):
        entry = self.robotGroundHandler.getEntry(i)
        entries.append(entry)
    entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                     x.getSurfacePoint(render).getZ()))
    
    if (len(entries)>0) and (entries[0].getIntoNode().getName() == "Grid"):
        self.robot.setZ(entries[0].getSurfacePoint(render).getZ())
        print entries[0].getSurfacePoint(render).getZ(),self.robot.getPos()
        #self.robot.setZ(1000)
    else:
            self.robot.setPos(startpos)
      
    self.prevtime = task.time
    return Task.cont

d =World()
run()
