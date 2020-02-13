from graphics import *
import numpy as np
import math
import bfs
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
n = 4


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

val = np.array(probmatrix(n,0.4)).reshape((n,n))
print(val[3][3])

if( val[0][0] == 0 or val[n-1][n-1] == 0):
    val = changesourcedest(val, n)
def buildmaze(n):
    win = GraphWin("My maze" , n*40 ,n*40)
    arr = []
    l = 0
    k = 40
    for i in range(0,n):
        for j in range(0,n):
            shape = Rectangle(Point(l, i*40), Point(k,40*(i+1)))
            #print(l)
            shape.setOutline("blue")
            shape.setFill("white")
            arr.append(shape)
            l = l+40
            k = k+40
        l=0
        k =40
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

valt = [ [1 , 0, 1 , 1] ,
        [1, 1 , 1, 0 ],
        [ 0, 1, 1, 1],
        [0,0,0,1]]
#print(valt)
value = bfs.bfs(val,n)
if( value == None):
    print( "no path to be found")
w.getMouse()
w.close()
