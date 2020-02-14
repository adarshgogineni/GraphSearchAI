from graphics import *
import numpy as np
import math
import bfs
import BidBFS
import Astar
"""
win = GraphWin("My maze", 500, 500)
shape = Rectangle(Point(80,0), Point(120,40) )
shape.setOutline("red")
shape.setFill("red")
shape.draw(win)
win.getMouse()
win.close()

"""
def probmatrix(n, p):   #meathod for calculating the initial matrix
    one = 1-p
    z = p
    total = n*n
    z = int(math.floor(total * z))

    one = int(math.ceil(total * one))
    arr = []
    #print(z)
    for i in range(0,z):
        arr.append(0)
    for i in range(0,one):
        arr.append(1)

    np.random.shuffle(arr)
    return arr
n =4


def changesourcedest(arr , n): #this meathod is to fix the source and the destination block problem. I am basically changing the
    if(val[0][0] == 0): #the values of the source and the destination if they are blocked. I am keeping the probability same by swiching some other value to 0.
        for i in range(0,n):
            a = 0
            for j in range(1,n):
                if(val[i][j] == 1 and (i!=n-1 or j != n-1) ):
                    val[i][j] =0; #if the values encountered is one then switch it to zero to keep the probability same.
                    val[0][0]= 1;  # switch the source to one.
                    a = 1
                    break;
            if(a == 1):
                break;
    if(val[n-1][n-1] == 0):  #this is for the destination value. you are doing the same thing again.
        for i in range(0,n):
            a = 0
            for j in range(1,n):
                if(val[i][j] == 1):
                    val[i][j] =0;
                    val[n-1][n-1]= 1;
                    a = 1
                    break;
            if(a == 1):
                break;
    return arr
h = 10
val = np.array(probmatrix(n,0.3)).reshape((n,n))
print(val[3][3])

if( val[0][0] == 0 or val[n-1][n-1] == 0):
    val = changesourcedest(val, n)
def buildmaze(n):
    win = GraphWin("My maze" , n*h ,n*h)
    arr = []
    l = 0
    k = h
    for i in range(0,n):
        for j in range(0,n):
            shape = Rectangle(Point(l, i*h), Point(k,h*(i+1)))
            #print(l)
            shape.setOutline("blue")
            shape.setFill("white")
            arr.append(shape)
            l = l+h
            k = k+h
        l=0
        k =h
    return win, arr

w , arr = buildmaze(n)
w.setBackground('black')
arr = np.array(arr)
arr = arr.reshape((n,n))
print( arr.shape)
for i in range(0,n):
    for j in range( 0 , n):
        #print(arr[i][j])
        if( val[i][j] == 0):
            arr[i][j].setFill("black")
            arr[i][j].draw(w)
        else:
            arr[i][j].draw(w)
#m = np.array((10,10))
print(val)
#print(valt)
#value = bfs.bfs(val,n)
""" #this is for bidirectional BFS
value1, value2 = BidBFS.bidbfs(val, n)
print(value1,value2)
if(value1 != 0 and value2 !=0):
    while( value1 != None):
        print(str(value1.nodex) + " " + str(value1.nodey) )
        arr[value1.nodex][value1.nodey].setFill("red")
        value1 = value1.prvnode
    while( value2 != None):
        print(str(value2.nodex) + " " + str(value2.nodey) )
        arr[value2.nodex][value2.nodey].setFill("red")
        value2 = value2.prvnode
"""

""" #this is for regular bfs
if( value == None):
    print( "no path to be found")
else:
    while( value.prvnode != None):
        print(str(value.prvnode.nodex) + " " + str(value.prvnode.nodey) )
        arr[value.prvnode.nodex][value.prvnode.nodey].setFill("red")
        value = value.prvnode
if(value !=None):
    arr[n-1][n-1].setFill("red")

"""
w.getMouse()
w.close()
valt = [[1,1,1,0],[1, 1 ,0,0],[1, 0, 1, 1],[1,1,1,1]]
print(valt)
value = Astar.astarED(valt,n)
if( value == None):
    print( "no path to be found")
else:
    while( value.prvnode != None):
        #print(str(value.prvnode.nodex) + " " + str(value.prvnode.nodey) )
        arr[value.prvnode.nodex][value.prvnode.nodey].setFill("red")
        value = value.prvnode
if(value !=None):
    arr[n-1][n-1].setFill("red")

print(value)
