import bfs
import math
import queue
def EDhuristic(node, n):
    x = node.nodex
    y = node.nodey
    xp = x-(n-1)
    yp = y - (n-1)
    xp = xp*xp
    yp = yp*yp
    return math.sqrt(xp+yp)
def getneighbor(arr, node , n):
    x = node.nodex
    y = node.nodey
    q = queue.Queue(maxsize=4)
    if( bfs.up(x,y) != None):
        xtmp, ytmp = bfs.up(x,y)
        #print(str(xtmp) + " " + str(ytmp))
        if( arr[xtmp][ytmp] != 0):
            temp = bfs.node(xtmp,ytmp,node)
            q.put(temp)
    if( bfs.down(x,y,n) != None):
        xtmp, ytmp = bfs.down(x,y,n)

        if(  arr[xtmp][ytmp] != 0):
            temp = bfs.node(xtmp,ytmp,node)
            q.put(temp)
    if( bfs.left(x,y) != None):
        xtmp, ytmp = bfs.left(x,y)
        #print(str(xtmp) + " " + str(ytmp))
        if(arr[xtmp][ytmp] != 0):
            temp = bfs.node(xtmp,ytmp,node)
            q.put(temp)

    if(bfs.right(x,y,n) != None):
        xtmp, ytmp = bfs.right(x,y,n)
        #print(str(xtmp) + " " + str(ytmp))
        if(arr[xtmp][ytmp] != 0 ):
            temp = bfs.node(xtmp,ytmp,node)
            q.put(temp)
    return q

def checkin(qu, tmpr):
    x = tmpr.nodex
    y = tmpr.nodey
    if ( len(qu) == 0):
        return False
    for i in range(0,len(qu)):
        t = qu[i]
        if( t[0].nodex == x and t[0].nodey == y):
            return True
    return False

def astarED(arr , n):
    start = bfs.node(0,0,None)
    nbr = getneighbor(arr, start , n)
    minnode =start
    visited = queue.Queue(maxsize=n*n)
    qu = []
    while(nbr.empty() != True and (minnode.nodex != n-1 or minnode.nodey !=n-1) ):
        #print( str(minnode.nodex) + " " + str(minnode.nodey))
        minher = -1
        for q in nbr.queue:
            tmphr = EDhuristic(q, n)

            if ( minher == -1):
                if(bfs.vt(visited,q.nodex, q.nodey) == False):
                    minher = tmphr
                    minnode = q
            elif( tmphr < minher):
                if(bfs.vt(visited,q.nodex, q.nodey) == False):
                    #print(minher)
                    minher = tmphr
                    minnode = q
                    qu.append((q,tmphr))
            else:
                if(bfs.vt(visited,q.nodex, q.nodey) == False):
                    if(checkin(qu, q)== False):
                        qu.append((q,tmphr))
                        print(str(q.nodex) + " " +str(q.nodey)+ "->")

        if(minher == -1):
            if(len(qu) == 0):
                return None
            else:
                rnode = 0
                sm= n*n
                for i in range(0,len(qu)):
                    t = qu[i]

                    #print(t)
                    if(t[1] < sm):
                        if(bfs.vt(visited,t[0].nodex, t[0].nodey) == False ):
                            minnode = t[0]
                            sm = t[1]
                            rnode = t
                if(rnode != 0):
                    qu.remove(rnode)

        print( str(minnode.nodex) + " " + str(minnode.nodey))
        #print(str(minnode.nodex) + " " + str(minnode.nodey))
        print("nbr")
        #print(qu)
        if( bfs.vt(visited,minnode.nodex, minnode.nodey) == False):
            visited.put(minnode)
        else:
            return None
        nbr = getneighbor(arr, minnode , n)
        for q_item in nbr.queue:
            print (str(q_item.nodex) + " " + str( q_item.nodey))
        print("next")
    if( minnode == start):
        return None
    return minnode
