from graph import *
from vertex import *
from bfs import *
from cs151queue import *

def kevinbaconnumber(actor):
    actors = open("actors.txt","r")
    movies = open("movies.txt","r")
    movieactors = open("movieactors.txt","r")

    actordic = {}
    actorlist = []
    for aline in actors:
        actorlist = aline.split("|")
        editactor = actorlist[1].replace("\n","")
        actordic[int(actorlist[0])] = editactor

    actors = open("actors.txt","r")
    revactordic = {}
    revactorlist = []
    for aline in actors:
        revactorlist = aline.split("|")
        editactorrev = revactorlist[1].replace("\n","")
        revactordic[editactorrev] = int(revactorlist[0])

    moviedic = {}
    movielist = []
    for aline in movies:
        movielist = aline.split("|")
        editmovie = movielist[1].replace("\n","")
        moviedic[int(movielist[0])] = editmovie

    madic = {}
    malist = []
    for aline in movieactors:
        malist = aline.split("|")
        editma = malist[1].replace("\n","")
        if int(malist[0]) in madic:
            madic[int(malist[0])].append(int(editma))
        else:
            madic[int(malist[0])] = []
            madic[int(malist[0])].append(int(editma))
            

    kbg = Graph()
    actors = open("actors.txt","r")
    actorlist = []
    for aline in actors:
        actorlist = aline.split("|")
        kbg.addVertex(int(actorlist[0]))
        

    movies= open("movieactors.txt","r")
    movielist = []
    for aline in movies:
        movielist = aline.split("|")
        movienum = int(movielist[0])
        edges = madic[movienum]
        while len(edges) >= 1:
            for i in range(len(edges)-1):
                kbg.addEdge(edges[0],edges[i+1],movienum)
                kbg.addEdge(edges[i+1],edges[0],movienum)
            edges.pop(0)

    bfs(kbg,63)

    if actor in revactordic:
        if kbg.getVertex(revactordic[actor]).getDistance() > 2000:
            print("This actor is not related to Kevin Bacon")
        else:
            vert = kbg.getVertex(revactordic[actor])
            print("Kevin Bacon Number:",vert.getDistance())
            actornum = revactordic[actor]
            while actornum != 63:
                nextactor = kbg.getVertex(actornum).getPred()
                commonmovie = kbg.getVertex(actornum).getCost(nextactor)
                print(actordic[actornum],"was in",moviedic[commonmovie],"which also starred")
                actornum = nextactor.getId()
            print("Kevin Bacon")
    else:
        print("This actor is not in our database (check spelling)")

def main():
    actor =""
    while actor != "Quit":
        actor = input("Enter an actor (Type Quit to exit)")
        if actor != "Quit":
            kevinbaconnumber(actor)

main()

