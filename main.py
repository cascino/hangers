from graphics import GraphWin, Point, Text, Rectangle
from button import Button
from hangmethods import *
from shortcuts import *

#Day 2 working on Final Hangman Assignment

#Finished Menu Function
#  -Looking for a way to reduce the list clutter

#Finished Keyboard Function
#  -Yet to add in other keyboard layouts such as dvorak

#Created "shortcuts" to better organize and reduce clutter of code (creating graphical windows and buttons in a standardized fashion)
#  -Looking for a way to create shortcuts for button presses to simplify even more (dont have to do individual programming of each button)

#Finished Mode Function
#  -Yet to add different modes
#  -Yet to add meaning to these modes through "game win/exit conditions"

#Finished Difficulty Function
#  -Yet to add different difficulty meanings
#  -What does higher difficulty entail?

#Finished Lists Function
#  -Add more lists

#Started working on Leaderboard function
#Started working on a HowTo function
#  -It will just be a large block of Text

def menu():
  name, val = windowMake("Main Menu",windowList,leaves)
  leaves[val].deactivate()
  entry = ["Play","Keyboards","Modes","Difficulty","Lists","Leaderboard","HowTo"]
  buttons = ["Play","Keyboards","Modes","Difficulty","Lists","Leaderboard","HowTo"]
  massButtoner(entry,name)
  point = name.getMouse()
  while True:
    for i in range(5):
      if entry[i].clicked(point):
        x = buttons.index(entry[i].getLabel())
        name.close()
        functionList[x]()
    point = name.getMouse()

def Play():
  name, val = windowMake("Hangman Game",windowList,leaves)

  keySel = open("preferences/selectedKey.txt","r")
  keyboards = open("preferences/keyboards.txt","r")
  
  listType = open("preferences/wordList.txt","r")
  
  keytype = keyboards.readlines()[int(keySel.read())].split(",")
  wordInd = int(listType.read()[0:1])
  
  words = ["Countries","Pets","Foods","League"]
  word = hangWord("categories/"+words[wordInd]+".txt")

  score = 0
  errors = 0
  puzzle = hangPuzzle(word)
  j = hangDraw(name,puzzle)
  e = errorDraw(name,errors)
  s = sDraw(name,score)
  
  keylist = []
  
  for i in range(27):
    keylist.append("key" + str(i))
  keyboard(keytype,name,keylist)
  

  point = name.getMouse()
  while (not leaves[val].clicked(point)):
    for i in range(26):
      if keylist[i].clicked(point):
        guess = keylist[i].getLabel()
        keylist[i].deactivate()
        if hangIn(guess,word,puzzle) == True:
          errors += 0
          score += 10
        else:
          errors += 1
          score = int(score/2)
      j.setText("".join(puzzle))
      e.setText("Errors:"+str(errors))
      s.setText("Score:"+str(score))
    point = name.getMouse()

  
  keySel.close()
  listType.close()
  keyboards.close()
  name.close()
  
  menu()
  return
  
def Keyboards():
  name,val = windowMake("Keyboard Selection",windowList,leaves)
  keyboard = ["qwerty","abcdef","dvorak"]
  massButtoner(keyboard,name)
  prefWriteLoop(keyboard,name,val,"preferences/selectedKey.txt",leaves)
  name.close()
  menu()
  return

def keyboard(keytype,win,keylist):
  for i in range(10):
    keylist[i] = Button(win,Point(160+25*i,100),25,25,keytype[i])
    keylist[i].activate()
  for i in range(10,19):
    keylist[i] = Button(win,Point(147.5+25*(i-9),75),25,25,keytype[i])
    keylist[i].activate()
  for i in range(19,27):
    keylist[i] = Button(win,Point(85+25*(i-15),50),25,25,keytype[i])
    keylist[i].activate()

def Modes():
  name, val = windowMake("Modes",windowList,leaves)
  modes = ["Minesweeper","Spy","Reverse","Infinite","Flawless"]
  massButtoner(modes,name)
  prefWriteLoop(modes,name,val,"preferences/modes.txt",leaves)
  name.close()
  menu()
  return
def Difficulty():
  name, val = windowMake("Difficulty",windowList,leaves)
  difficulties = ["Beginner","Intermediate","Advanced","Expert","Prophet"]
  massButtoner(difficulties,name)
  prefWriteLoop(difficulties,name,val,"preferences/difficulty.txt",leaves)
  name.close()
  menu()
  return
  
def Lists():
  name, val= windowMake("Word Lists",windowList,leaves)
  words = ["Countries","Pets","Foods","League"]
  massButtoner(words,name)
  prefWriteLoop(words,name,val,"preferences/wordList.txt",leaves)
  name.close()
  menu()
  return

def Leaderboard():
  return

def HowTo():
  return

functionList = [Play,Keyboards,Modes,Difficulty,Lists,Leaderboard,HowTo]

windowList = []
leaves = []


menu()




