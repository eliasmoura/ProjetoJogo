'''
Created on 09/01/2013

@author: Elias
'''
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText 
import sys

class Personagem():
    def __init__(self, render):
        self.fram = DirectFrame(frameSize=(100,100,100,100),
                                 frameColor=(255,0,0,0),
                                 pos=(0.0,0,0))
        #self.fram.setPos(-1,0)
        #render.attachNewNode (self.frame)
    
    def hp(self,base):
        self.hp = OnscreenText(text = "100", pos=(0,0,0), parent = base.aspect2d)
        #self.NewButton = DirectButton(frameColor = (0, 0, 0, 0), parent = base.aspect2d, text = ("Testing"), scale = 0.08, command = sys.exit) 
        self.hp.setPos(-1.25, 0) 
        #self.hp.setFrame(self.fram)
    
    def experiencia(self):
        pass
    
    