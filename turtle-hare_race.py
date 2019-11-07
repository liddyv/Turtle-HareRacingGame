#!/bin/python3
"""
@Final project: Turtle-Hare Racing game
@Description:  This project will use loops to create a racing turtle game 
- 1. Load image of animal
- 2. draw a race track.
- 3. player choose animal to play (Type in text)
- 4. start racing by reading speed/rest rate from 'speedRate.txt' file
- 5. Announce winner when finished. (loser will list how many steps behine)
- 6. Write winner to 'winnerRecords.txt' file
- To-Do later (Enhancemnets): 
    Seperate screen to start the game. 
    User can choose animal to play by clicking images
    Machine will choose random player
    Display the winner date better (i.e. with some cute image)
    Add sounds
    
@author: Liddy Hsieh

"""
# Import libraries
from turtle import *
from random import randint
        
# Initialize variables
penup()
goto(-100, -200)
oTurtle =  Turtle()
oHare = Turtle()
oPlayer = Turtle()
hare_img="images/hare.gif"
#turtle_img="images/turtle.gif" #use default turtle in this game
speedFile='speedRate.txt'
winnerRecordFile='winnerRecords.txt'


def load_gif(image):
    # add images
    screen=Screen()
    screen.addshape(image)


def build_trace(NoOfLines):
    # Build a Race track
    for step in range(NoOfLines):
      write('Player: %s' % step, align='center') # print line# in center
      left(90)
      for num in range(20):
        penup()
        forward(10)
        pendown()
        forward(10)
      penup()
      backward(400)
      right(90)
      forward(80)


def create_turtle():
    #oTurtle.shape(turtle_img) # custom image
    oTurtle.shape('turtle') # default image
    oTurtle.color('red') # turn turtle and trace run in red color
    
    oTurtle.penup() #don't draw when pen is up
    oTurtle.goto(-100, -200)
    oTurtle.pendown() #draw when pen is down
    
    #turn 450 degree left(10 times*45 degree each time)
    for turn in range(10):
        oTurtle.left(45)
    
    
def create_hare():
    oHare.shape(hare_img)
    oHare.color('blue') # trace run in blue color
    
    oHare.penup() #don't draw when pen is up
    oHare.goto(-20, -200)
    oHare.pendown() #draw when pen is down
    '''
    oHare.circle(5) #go into small circle
    oHare.left(90) #head turn 90 degree left
    '''
    for turn in range(10):
        oHare.left(45)
    

''' To-Do: combine create_turtle() and create_hare(). 
    Challenges: currently it's not working since players cannot face up (it face right)
    Hints: goto(x, y) & turn() 
def create_player(player, playerImage, playerColor, x=0, y=0):
    oPlayer.shape(playerImage) # player's image
    oPlayer.color(playerColor) # turn turtle and trace run in red color
    
    oPlayer.penup() #don't draw when pen is up
    oPlayer.goto(x, y)
    oPlayer.pendown() #draw when pen is down
    
    
    # if turtle, turn 
    if player.lower() == "turtle": #player   
        #turn 450 degree left(10 times*45 degree each time)
        for turn in range(10):
            oPlayer.left(45)
    else: # else, run in circle
        oPlayer.circle(5) #go into small circle
        oPlayer.left(90) #head turn 90 degree left
'''        


def start_race():   
    file = open(speedFile, 'r') #open file on read mode
    for line in file.read().splitlines():
        turtleSpeed, turtleRest, hareSpeed, hareRest = map(int, line.split(' '))
    file.close() # close file
    
    while True:
        for turn in range(100):
          #oTurtle.speed(1)
          #oTurtle.forward(randint(0,6))
          #running
          oTurtle.forward(randint(0,turtleSpeed))
          oTurtle.backward(randint(0,turtleRest)) 
          #print(oTurtle.position())
          
          #oHare.speed(10)
          #oHare.forward(randint(0,6))
          #running
          oHare.forward(randint(0,hareSpeed))
          oHare.backward(randint(0,hareRest))
          #print(oHare.position())
          
          # check who reach 200 first
          try: 
              if ( round(oTurtle.ycor(), 2) >= 200.00 ) : # turtle wins
                  #oTurtle.goto(-100, 200)
                  
                  oTurtle.write('Turtle is the winner!!', align='center')
                  make_winnerCake(oTurtle, -100, 220)
                  
                  oHare.write("Hare is only %d steps behind. \nWill not wondering around next time" \
                              % (oTurtle.pos()[1]-oHare.pos()[1]) )
                  #print("I am only %d steps behind. Will not wonder around next time" \
                  #            % (oTurtle.pos()[1]- oHare.pos()[1]) )
                  #print('Turtle is the winner!')
                  
                  #append the winner to a file
                  f = open(winnerRecordFile, 'a')
                  f.write("Turtle ")
                  f.close()
                  
                  return False
              elif ( round(oHare.ycor(), 2) >= 200.00 ) : # hare wins
                  
                  #oHare.goto(-20, 200)
                  oHare.write('Hare is the winner!')
                  make_winnerCircle(oHare, -20, 250)
                  
                  oTurtle.write("Turtle is %d steps behind. \nWill try harder next time" \
                              % (oHare.pos()[1]- oTurtle.pos()[1]), align='center')
                  
                  #print('Hare is the winner!')
                  #append the winner to a file
                  f = open(winnerRecordFile, 'a')
                  f.write("Hare ")
                  f.close()

                  return False
              else:
                  raise
          except:
              print( 'Running.. Almost there!!.' )
              

def make_winnerCircle(winner, x=0, y=0):
    colors = ["orange", "green", "purple"]
    winner.goto(x, y)
    for each_color in colors:
        angle = 360 / len(colors)
        winner.color(each_color)
        winner.circle(5)
        winner.right(angle)
        winner.forward(7)


def make_winnerCake(winner, x=0, y=0):
    winner.penup()
    winner.color('pink')
    winner.goto(x, y)
    winner.pendown()
    winner.begin_fill()
    winner.goto(x + 20, y)
    winner.goto(x + 20, y + 20)
    winner.goto(x - 20, y + 20)
    winner.goto(x - 20, y)
    winner.goto(x, y)  
    winner.end_fill()
    winner.goto(x, y + 20)
    winner.color('yellow')
    winner.goto(x, y + 35)
    winner.goto(x, y + 30)
    winner.color('black')
    winner.goto(x, y + 20)
    winner.penup()
    winner.goto(x, y + 10)

        
# main  
# 1. load images    
load_gif(hare_img)
#load_gif(turtle_img)
    
# 2. build how many lines of trace
build_trace(2)

# 3. ask user to choose animal to play and getting animal ready at starting line
try: 
    oShape = input("Please choose turtle or hare: ")
    
    if oShape.lower() == "turtle":
        write("You are turtle: Player 0, Good luck racing!")
        #create_player('turtle', 'turtle', 'red', -100, -200)
        #create_player('hare', hare_img, 'blue', -20, -200)
        create_turtle()
        create_hare()
    elif oShape.lower() == "hare":
        write("You are hare: Player 1, Good luck racing!")
        #create_player('hare', hare_img, 'blue', -20, -200)
        #create_player('turtle', 'turtle', 'red', -100, -200)
        create_hare()
        create_turtle()
except:
    write("I don't understand that anamil. Are you typing turtle or hare?")

# 4. start racing - Read speed/rest numbers from a file and wrint winner to anohter file.
start_race()

