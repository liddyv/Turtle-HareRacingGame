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
from random import choice
from turtle import *
from random import randint
        

class Racing:

    def build_trace(self, NoOfLines):
        penup()
        goto(-100, -200)
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
    
    
    def create_turtle(self):
        #oTurtle.shape(turtle_img) # custom image
        self.oTurtle.shape('turtle') # default image
        self.oTurtle.color('red') # turn turtle and trace run in red color
        
        self.oTurtle.penup() #don't draw when pen is up
        self.oTurtle.goto(-100, -200)
        self.oTurtle.pendown() #draw when pen is down
        
        #turn 450 degree left(10 times*45 degree each time)
        for turn in range(10):
            self.oTurtle.left(45)
        
        
    def create_hare(self):
        hare_img='images/hare.gif' # custom image
        screen=Screen()
        screen.addshape(hare_img)
        self.oHare.shape(hare_img)
        self.oHare.color('blue') # trace run in blue color
        
        self.oHare.penup() #don't draw when pen is up
        self.oHare.goto(-20, -200)
        self.oHare.pendown() #draw when pen is down
        
        self.oHare.circle(5) #go into small circle
        self.oHare.left(90) #head turn 90 degree left
        
        
    def start_race(self):   
        file = open(self.speedFile, 'r') #open file on read mode
        for line in file.read().splitlines():
            turtleSpeed, turtleRest, hareSpeed, hareRest = map(int, line.split(' '))
        file.close() # close file'
              
        while True:
            for turn in range(100):
              
              #self.oTurtle.speed(1)
              #self.oTurtle.forward(randint(0,6))
              #running
              self.oTurtle.forward(randint(0,turtleSpeed))
              self.oTurtle.backward(randint(0,turtleRest)) 
              '''
              print(oTurtle.position())
              if ( round(self.oTurtle.ycor(), 2) >= 200.00 ) : 
                  print(self.oTurtle.ycor())
              '''

              
              #self.oHare.speed(10)
              #self.oHare.forward(randint(0,6))
              #running
              self.oHare.forward(randint(0,hareSpeed))
              self.oHare.backward(randint(0,hareRest))
              '''
              print(oHare.position())
              if ( round(self.oHare.ycor(), 2) >= 200.00 ) : 
                  print(round(self.oHare.ycor(), 2))
              '''
              # check who reach 200 first
              try: 
                  if ( round(self.oTurtle.ycor(), 2) >= 200.00 ) : # turtle wins
                      #oTurtle.goto(-100, 200)
                      
                      self.oTurtle.write('Turtle is the winner!!', align='center')
                      #self.make_winnerCake(self.oTurtle, -100, 220)
                      self.oTurtle.penup()
                      self.oTurtle.color('pink')
                      self.oTurtle.goto(-100, 220)
                      self.oTurtle.pendown()
                      self.oTurtle.begin_fill()
                                      
                      self.oHare.write("Hare is only %d steps behind. \nWill not wondering around next time" \
                                  % (self.oTurtle.pos()[1]-self.oHare.pos()[1]) )
                      #print("I am only %d steps behind. Will not wonder around next time" \
                      #            % (oTurtle.pos()[1]- oHare.pos()[1]) )
        
                      #print('Turtle is the winner!')
                      #append the winner to a file
                      f = open(self.winnerRecordFile, 'a')
                      f.write("Turtle ")
                      f.close()
                      return False
                  
                  elif ( round(self.oHare.ycor(), 2) >= 200.00 ) : # hare wins
                      
                      #oHare.goto(-20, 200)
                      self.oHare.write('Hare is the winner!')
                      #self.make_winnerCircle(self.oHare, -20, 250)
                      colors = ["orange", "green", "purple"]
                      self.oHare.goto(-20, 250)
                      for each_color in colors:
                          angle = 360 / len(colors)
                          self.oHare.color(each_color)
                          self.oHare.circle(5)
                          self.oHare.right(angle)
                          self.oHare.forward(7)
                      
                      self.oTurtle.write("Turtle is %d steps behind. \nWill try harder next time" \
                                  % (self.oHare.pos()[1]- self.oTurtle.pos()[1]), align='center')

                      #print('Hare is the winner!')
                      #append the winner to a file
                      f = open(self.winnerRecordFile, 'a')
                      f.write("Hare ")
                      f.close()
                      return False    
                      
                  else:
                      raise
              except:
                  print( 'Running.. Almost there!!.' )
                     

    def show_player(self):
        players = {}
        screen=Screen()
        file = open('playersInfo.txt', 'r')
        
        for line in file.read().splitlines():
            name, speed, rest, image = line.split(', ')
            players[name] = [speed, rest, image]
            screen.addshape(image)
        
        file.close()    
        print(players)
        
        for player in players:
            stats = players[player]
            style = ('Arial', 14, 'bold')
            clear()
            goto(0, 100)
            shape(stats[2])
            setheading(90)
            stamp()
            setheading(-90)
            forward(60)
            write('Name: ' + player, font=style, align='center')
            forward(25)
            write('forward speed' + stats[0], font=style, align='center')
            forward(25)
            write('rest speend' + stats[1], font=style, align='center')
       

    

