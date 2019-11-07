## Scenes Demo Main

# 1 - Import packages
import pygame
import pyghelpers
import Constants
import SceneEnter
#import SceneTrack
#import SceneHare
#import SceneStartRace

from Constants import *
from SceneEnter import *
from SceneStart import *
from SceneShow import *


# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 180
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
# Create instances of all scenes.  Pass in the window and a scene key (string) for each scene
oSceneEnter = SceneEnter(window, Constants.SCENE_ENTER)
oSceneStart = SceneStart(window, Constants.SCENE_START)
oSceneShow = SceneShow(window, Constants.SCENE_SHOW)


# Build a dictionary of all scenes
#scenesDict = {Constants.SCENE_ENTER: oSceneEnter, Constants.SCENE_TURTLE : oSceneTurtle, Constants.SCENE_HARE : oSceneHare, Constants.SCENE_STARTRACE : oSceneStartRace}
scenesDict = {Constants.SCENE_ENTER: oSceneEnter, Constants.SCENE_START : oSceneStart, Constants.SCENE_SHOW : oSceneShow}

# Create the Scene Manager, passing in the scenes dictionary, the starting scene, and the FPS
oSceneMgr = pyghelpers.SceneMgr(scenesDict, Constants.SCENE_ENTER, FRAMES_PER_SECOND)

# Tell the Scene Manager to start running
oSceneMgr.run()
