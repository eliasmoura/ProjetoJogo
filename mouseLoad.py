'''
Created on 15/01/2013

@author: Elias
'''
from pandac.PandaModules import BitMask32
from pandac.PandaModules import CollisionRay
from pandac.PandaModules import CollisionNode
from pandac.PandaModules import CollisionHandlerQueue
from pandac.PandaModules import CollisionTraverser
from pandac.PandaModules import GeomNode

class ControleMouse():
    def __init__(self, render, camera):
        #Since we are using collision detection to do picking, we set it up like any other collision detection system with a traverser and a handler 
        self.picker = CollisionTraverser()            #Make a traverser 
        self.pq     = CollisionHandlerQueue()         #Make a handler 
        #Make a collision node for our picker ray 
        self.pickerNode = CollisionNode('mouseRay') 
        #Attach that node to the camera since the ray will need to be positioned relative to it 
        self.pickerNP = camera.attachNewNode(self.pickerNode) 
        #Everything to be picked will use bit 1. This way if we were doing other collision we could seperate it 
        self.pickerNode.setFromCollideMask(BitMask32.bit(1)) 
        self.pickerRay = CollisionRay()               #Make our ray 
        self.pickerNode.addSolid(self.pickerRay)      #Add it to the collision node 
        #Register the ray as something that can cause collisions 
        self.picker.addCollider(self.pickerNP, self.pq) 
        #self.picker.showCollisions(render) 
        
        self.pst = CollisionTraverser()            #Make a traverser 
        self.hqp     = CollisionHandlerQueue()         #Make a handler 
        #Make a collision node for our picker ray 
        
        self.pstNode = CollisionNode('mouseRaytoObj') 
        #Attach that node to the camera since the ray will need to be positioned relative to it 
        self.pstNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pstNode2 = camera.attachNewNode(self.pstNode) 
        self.pickerRayObj = CollisionRay()   
        #Everything to be picked will use bit 1. This way if we were doing other collision we could seperate it 
        #self.pstNode.setFromCollideMask(BitMask32.bit(1)) 
        self.pstNode.addSolid(self.pickerRayObj)      #Add it to the collision node 
        #Register the ray as something that can cause collisions 
        self.pst.addCollider(self.pstNode2, self.hqp) 
        #self.pst.showCollisions(render) 