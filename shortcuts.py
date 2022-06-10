from graphics import *
from button import *


def windowMake(windowName,list,leaves):
  list.append(windowName)
  leaves.append(windowName)
  lval = leaves.index(windowName)
  val = list.index(windowName)
  list[val] = GraphWin(windowName,520,520)
  list[val].setCoords(0,0,520,520)
  list[val].setBackground("grey")
  leaves[lval] = Button(list[val],Point(100,50),50,25,"Menu")
  leaves[lval].activate()
  return list[val], val

def massButtoner(list,win):
  for i in range(len(list)):
    list[i] = Button(win,Point(260,410-50*i),125,25,list[i])
    list[i].activate()

def prefWriteLoop(list,win,val,file,leaves):
  point = Point(0,0)
  while not leaves[val].clicked(point):
    for i in range(len(list)):
      if list[i].clicked(point):
        file = open(file,"w")
        file.write(str(i))
        file.close()
        win.close()
        return
    point = win.getMouse()

