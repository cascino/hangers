from graphics import GraphWin, Point, Text, Rectangle
from random import randrange
from button import Button

def hangWord(title):

  list = open(title,"r")
  
  listread = list.readlines()
  
  wordIndex = randrange(0,len(listread))

  word = listread[wordIndex]
  
  list.close()
  
  return(word)

def hangPuzzle(word):
  
  puzzle = []
  
  for i in word:
    if 96 < ord(i.lower()) < 123:

      puzzle.append("*")

    else:

      puzzle.append(i)

  return (puzzle)

def hangIn(guess, word, puzzle):

  flag = False

  for i in range(len(word)):

    if guess == word[i].lower():

      puzzle[i] = word[i]

      flag = True

  return flag

def hangDraw(win,puzzle):
  stars = "".join(puzzle)
  currentword = Text(Point(260,260),stars)
  currentword.setSize(20)
  currentword.draw(win)
  return(currentword)

def errorDraw(win,errors):
  eDraw = Text(Point(460,460),"Errors:"+str(errors))
  eDraw.setSize(20)
  eDraw.draw(win)
  return(eDraw)

def sDraw(win,score):
  sDraw = Text(Point(460,420),"Score"+str(score))
  sDraw.setSize(20)
  sDraw.draw(win)
  return(sDraw)