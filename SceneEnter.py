#
# This the Scene Enter into game
#

import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *
import Constants
from turtle import *
import RaceWidgets

class SceneEnter(pyghelpers.Scene):
    def __init__(self, window, sceneKey):
        # Save window and sceneKey in instance variables
        self.window = window
        self.sceneKey = sceneKey

        self.messageField = pygwidgets.DisplayText(self.window, (15, 25), 'Welcome to Turtle-Hare Race!', \
                                              fontSize=50, textColor=Constants.GRAYA, width=610, justified='center')
        self.oEnterButton = pygwidgets.TextButton(self.window, (250, 100), 'Enter')
        
        self.hare = pygwidgets.Image(window, (150, 100), 'images/hare.gif')
        self.turtle = pygwidgets.Image(window, (390, 100), 'images/turtle.gif')
        
        self.oRace = RaceWidgets.Racing

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.oEnterButton.handleEvent(event):
                self.oRace.build_trace(self, 2)
                self.goToScene(Constants.SCENE_START)

    def update(self):
        self.hare.rotate(8)
        self.turtle.rotate(-8)


    def draw(self):
        self.window.fill(Constants.WHITE)
        self.messageField.draw()
        self.oEnterButton.draw()
        self.hare.draw()
        self.turtle.draw()

        