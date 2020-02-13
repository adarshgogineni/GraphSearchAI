import queue






class node:
    def __init__(self,x,y,prv):
        self.nodex = x
        self.nodey = y
        self.prvnode = prv

def up(x , y):
    if(x>0):
        return x-1 , y
def down(x,y,n):
    if(x<n-1):
        return x+1 ,y
def right(x,y,n):
    if(y<n-1):
        return x , y+1
def left(x,y):
    if(y>0):
        return x , y-1


def add(q, start , arr , n):
    x = start.nodex
    y = start.nodey
    xtmp = 0
    ytmp = 0
    a = 0
    if( (xtmp, ytmp == up(x,y))!= None):
        temp = node(xtmp,ytmp,start)
        if( temp != None):
            q.put(temp)
            a = 1
    if( (xtmp, ytmp == down(x,y,n))!= None):
        temp = node(xtmp,ytmp,start)
        if( temp != None):
            q.put(temp)
            a = 1
    if( (xtmp, ytmp == right(x,y,n))!= None):
        temp = node(xtmp,ytmp,start)
        if( temp != None):
            q.put(temp)
            a =1
    if( (xtmp, ytmp == left(x,y))!= None):
        temp = node(xtmp,ytmp,start)
        if( temp != None):
            q.put(temp)
            a=1
    return a
def bfs(arr,n):
    start = node(0,0,None)
    temp = start
    q = queue.Queue(maxsize=n*n)
    add(q,start, arr , n)
    while((temp.nodex!=n and temp.nodey != n) or q.empty() != true  ):
        temp = q.get()
        if( add(q,temp, arr , n) == 0):
            return None
    if( (temp.nodex!=n and temp.nodey != n) ):
        return temp
