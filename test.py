from graphics import *
import numpy as np
import math

"""
win = GraphWin("My maze", 500, 500)
shape = Rectangle(Point(80,0), Point(120,40) )
shape.setOutline("red")
shape.setFill("red")
shape.draw(win)
win.getMouse()
win.close()

"""
def probmatrix(n, p):
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
val = np.array(probmatrix(n,0.4)).reshape((n,n))
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
w.getMouse()
w.close()


"""
def arraygeneration(n):
    a = []
    for i in range(0,n):
        for j in range(0,n):
            a.append(rand(0,1))
    return a

a = arraygeneration(4)
a = np.array((4,4))
"""
