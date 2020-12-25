
PlayerTeam = []
associations = []
edges = []
players = []
frachises = []

f = open( "inputPS28.txt"  , "r")
for x in f:
  PlayerTeam.append(x)
f.close()

pt= []
     
for x in PlayerTeam:

  pt =  x.split("/")   

  counter1D = 1   # to remove space for each player due to reading the CSV , no space for Franchise 
  frachise = pt[0].replace(' ','')
  frachises.append(frachise)
  
  for a in pt:
    if counter1D > 1 :
        player = a.replace('\n','').replace(' ','')
        associations.append([player, frachise ])
      
    else :
        counter1D = counter1D + 1  
 
print ("--------------------------------" , " The Associations are ", "-----------------")             
print(associations)     
print()
print() 

print (".................   franchise are  ..................")     

print(frachises)      
print()
print()

print (".................   franchise Edges  ..................")     

for x in PlayerTeam:
  edge_f = []  
  pt =  x.split("/")   
  
  edge_f.append(pt[0].replace(' ',''))
  
  for a in pt[1:len(pt)]:
 
        edge_f.append(a.replace('\n','').replace(' ',''))
      
  edges.append (edge_f) 
  
  
  
print (edges)
print()
print()


print ("--------------------------------" , " The Players are  ", "-----------------")    
for tmp_association in associations:
    match = 0
    for tmp_player in players:
        if (tmp_association[0] == tmp_player) :
         match = match + 1
    if match == 0:  
     players.append(tmp_association[0])
# print ("no of player are : " , len(players))
# print (players)
# print()
# print()


print (".................   player Edges  ..................")     

for p in players:
    print ("................. " , p , "..................")          
    edge_p = [ x for x in associations if x[0] == p ]
    # print (edgeBen_Ex)
    counter = 1    
    for a in edge_p:
       if counter == 1 :  
            edge  = a 
            counter =  0
       else:
         edge.append(a[1])
        
    edges.append(edge)
  
print (edges) 
print()
print()

def getNeighbours(vertex):
    for i in edges:
         if (i[0] == vertex):
            #  print ("I am important ........    " , vertex, "     " , len(i)  )
            #  print (i[1:len(i)]  )
             return i[1:len(i)]


S = "PYYY"
D = "PUUU"




# traversal  - find path between 2 players 
print (".................   Traversal between - KedarJadhav  and  IshanKishan  are  ..................")  
print()
print()

queue = []     # Initialize a queue
visited = []   # List to keep track of visited nodes.

# queue.append("KedarJadhav")
# visited.append("KedarJadhav")  

# queue.append("KrunalPandya")
# visited.append("KrunalPandya")

queue.append(S)
visited.append(S)

    # Get all adjacent vertices of the
    # dequeued vertex s. If a adjacent
    # has not been visited, then mark it
    # visited and enqueue it

counter = 0    
breakIND = False
level = []
parent = []    
while queue:
        s = queue.pop(0) 
    #    level.append([s,counter])
        if breakIND == True:
            break 
        print ( s, end = " ") 
             
        for neighbour in getNeighbours(s):
            if (s == "KieronPollard"):    
                
                # IshanKishan
                
                
              breakIND = True
              break
            if neighbour not in visited: 
               visited.append(neighbour)
               queue.append(neighbour)
               queue.append(neighbour)
               parent.append([neighbour,s])   
          
              
print()
print()


# traversal  - find path between 2 players  with parent 
print (".................   Traversal between - KedarJadhav  and  IshanKishan  with parent    ..................")  
print(parent)
print()
print()   


PATH = []

PATH.append(D) 

for p in PATH:
  if p == S:
    break
  for i in parent:
      if i[0] == p:
            PATH.append(i[1])
          #  print (D ,"child is " , i[1])
print (PATH)  

print()
print()      

if len(PATH)  == 3 :
  print ("Yes , " ,  S , " and " , D ,"are Buddies" )         
elif len(PATH)  == 5 :          
  print ("Yes , " ,  S , " and " , D ,"are player connect  : " ) 
  PATH.reverse()
  print  (PATH)  
elif len(PATH) <= 1:
   print ("Yes , " ,  D , " and " , S ,"are not  associated : " , PATH )   
   
else :
      print ("Yes , " ,  D , " and " , S ,"are long distance associated : " , PATH )   
      
          
      # if i[0] == S:    
      #          PATH.append(i[1])
      #          break
      # if i[0] == "MI":
      #    print ("MI child is :" , i[1])     
      # if i[0] == "KrunalPandy":
      #   print ("KrunalPandy child is :" , i[1])     
      

# print (".................  DFS Traversal between - KedarJadhav  and  IshanKishan      ..................")  

# queueD = []     # Initialize a queue
# visitedD = []   # List to keep track of visited nodes.

# queue1.append("KedarJadhav")

# path = []
# while queue1:
#         path.append(queue1.pop(0))
#         vertex = path[-1]
#     #    level.append([s,counter])
#         if  vertex == "IshanKishan":
#             print (path)
#             break 
#         elif vertex not in visited1: 
#             print ("I am here ", vertex)            
#             for n in getNeighbours(vertex):
                
#                 new_path = list(path)
#                 new_path.append(n)
#                 queue1.append(new_path)
#                   # Mark the vertex as visited
#         visited1.append(n)

  
  



