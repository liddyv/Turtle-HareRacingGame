#
# This the Scene to Start Race
#

import pygwidgets
import pyghelpers
import pygame
#from pygame.locals import *
#from Constants import *
import Constants
import RaceWidgets
from turtle import *


class SceneStart(pyghelpers.Scene):
    def __init__(self, window, sceneKey):
        # Save window and sceneKey in instance variables
        self.window = window
        self.sceneKey = sceneKey
        
        self.messageField = pygwidgets.DisplayText(self.window, (40, 55), 'Start the Race!!!', \
                                              fontSize=30, textColor=Constants.BLUE, width=510, justified='center')
        self.oStartButton = pygwidgets.TextButton(self.window, (250, 100), 'Start', textColor=Constants.BLACK)
         
        self.oTurtle = Turtle()
        self.oHare = Turtle()
                
        self.speedFile='speedRate.txt'
        self.winnerRecordFile='winnerRecords.txt'

        self.oRace = RaceWidgets.Racing
        
        
    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.oStartButton.handleEvent(event):
                self.oRace.create_turtle(self)
                self.oRace.create_hare(self)
                self.oRace.start_race(self)
                
                self.goToScene(Constants.SCENE_SHOW)

    def update(self):
        pass       

    def draw(self):
        self.window.fill(Constants.PINK)
        self.messageField.draw()
        self.oStartButton.draw()


            