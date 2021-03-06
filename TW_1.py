#Graph Building

VertexList=[str(i) for i in range(0,7)]

EdgeList=[(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(5,2),(6,4),(4,6)] #undirected Graph

AdjList=[[] for vertex in VertexList] #empty initialy

for edge in EdgeList:
    AdjList[edge[0]].append(edge[1])#List of Adjacent Vertices

#DFS for a graph
    
def DFS():
    Target=int(input("Enter Target Vertex>>>   "))  
    Stack=[]
    Stack.append(0)
    visitedList=[]
    DFSstep=0
    while Stack:
        current=Stack.pop()
        
        for neighbour in AdjList[current]:
            DFSstep+=1
            if not neighbour in visitedList:
                Stack.append(neighbour)
              
        visitedList.append(current)
        if current==Target:
            break
    print("Output of Deapth First Search >>>>> ",visitedList)  
    print("Comparative Factor >>>>>{}".format(DFSstep))
    
DFS()    


def BFS():
    Target=int(input("Enter Target Vertex>>>   "))  
    Queue=[]
    Queue.append(0)
    visitedList=[]
    BFSstep=0
    while Queue:
        current=Queue.pop()
        for neighbour in AdjList[current]:
            BFSstep+=1
            if not neighbour in visitedList:
                Queue.insert(0,neighbour)
               
        visitedList.append(current)
       
        if current==Target:
            break
    print("Output of Breadth First Search >>>>",visitedList)    
    print("Comparative Factor >>>>>{}".format(BFSstep))

BFS()


#IDDFS => DFID
IDDFSStep=0
def IDDFS(currentVertex,DestVertex,limit):#Its depth limited search
    #print("Checkiing for Destination",currentVertex)
    if currentVertex==DestVertex:
        return True
    if limit<=0:
        return False
    
    for Vertex in AdjList[currentVertex]:        
        print(currentVertex,AdjList[currentVertex])
        if IDDFS(Vertex,DestVertex,limit-1):
            return True
        
    return False

def mainIDDFS(currentVertex,DestVertex,maxDepth):#its IDDFS search
    IDDFSStep=0#Comparison parameter
    for limit in range(maxDepth):
        IDDFSStep+=1
        if IDDFS(currentVertex,DestVertex,limit):        
            print("Comparative Factor >>>>>{}".format(IDDFSStep))
            return True
    return False

if   not mainIDDFS(0,6,4):

    print("Path is not Available within specified Depth!!!")
    
else:
    
    print("Path is Available!!!")

