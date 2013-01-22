'''
Created on 16/01/2013

@author: Elias
'''

#from inimigos import Inimigos
from direct.actor.Actor import Actor
from panda3d.ai import AICharacter
from panda3d.ai import AIWorld
from direct.task import Task
from pandac.PandaModules import *

from itens.items import Items

class Pokemao():#Inimigos):
    def __init__(self,render):
        self.nome = "Pokemao"
        self.agi = 10
        self.int = 5
        self.str = 1
        self.dano = 5
        self.bloqueio = False
        self.bloqueado = False
        self.velocAtaque = 0.5
        self.arma = None
        self.escudo = None
        self.armadura = None
        self.render = render
        self.loadModels()
        self.setAI()
        
        
        
    def loadModels(self):
        # Seeker
        pokemaoPos = Vec3(-10,-30.0,2.10)
        self.pokemao = Actor('personagens/Modelos/Pokeperna/p1',
                        {"andar" :"personagens/Modelos/Pokeperna/p1-andar.egg",
                        "saltar" :"personagens/Modelos/Pokeperna/p1-saltar.egg",
                        "correr" : "personagens/Modelos/Pokeperna/p1-correr",
                        "abaixar" : "personagens/Modelos/Pokeperna/p1-abaixar"})
        
        self.pokemao.reparentTo(self.render)
        #self.wanderer.setScale(0.5)
        self.pokemao.setPos(pokemaoPos)
      
    def setAI(self):
        #Creating AI World
        self.AIworld = AIWorld(self.render)
 
        self.AIchar = AICharacter("wanderer",self.pokemao, 100, 0.05, 5)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        
        self.AIbehaviors.wander(5, 0, 10, 1.0)
        self.pokemao.loop("correr")

        #AI World update        
        taskMgr.add(self.AIUpdate,"AIUpdate")
        
    #to update the AIWorld    
    def AIUpdate(self,task):
        self.AIworld.update()            
        return Task.cont