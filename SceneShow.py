#
# This the Scene Show all player's information
#

import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *
import Constants
from turtle import *
import RaceWidgets


class SceneShow(pyghelpers.Scene):
    def __init__(self, window, sceneKey):
        # Save window and sceneKey in instance variables
        self.window = window
        self.sceneKey = sceneKey
 
        self.messageField = pygwidgets.DisplayText(self.window, (30, 55), 'Show player informatin one by one', \
                                              fontSize=30, textColor=Constants.PURPLE, width=510, justified='center')
    
        self.oStartButton = pygwidgets.TextButton(self.window, (250, 100), 'Show', textColor=Constants.WHITE)

        self.oTurtle = Turtle()
        self.oHare = Turtle()
                        
        self.speedFile='speedRate.txt'
        self.winnerRecordFile='winnerRecords.txt'

        self.oRace = RaceWidgets.Racing
        
        
    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.oStartButton.handleEvent(event):
                self.oRace.show_player(self)
                
                print('Clicked on the nav button - typically add a: self.goToScene("NewScene")')
                #self.goToScene(Constants.SCENE_STARTRACE)

    def update(self):
        pass       

    def draw(self):
        self.window.fill(Constants.BLACK)
        self.messageField.draw()
        self.oStartButton.draw()


    def leave(self):
        """
        This method is called once when your code has asked to move on to a new scene
        It should return any data that this scene wants to pass on to the next scene
        """
        
           