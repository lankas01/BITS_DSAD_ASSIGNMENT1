#print (".............. IPL Bench : DSE 2020 SEC 4 - Group 280 : Assignment Solution  ........................ ")

class IPL:
   PlayerTeam=[]    
   edges=[]
   players = []
   franchises = []
   associations = []
   printList = []
  
   def clearFileData(self,fileName):
      f=open(fileName,"w");
      f.write("")
      f.close()

   def writeIntoOutFile(self,printLocList,fileName,clearFileReq):

      if (clearFileReq == "Y"):
         ipl.clearFileData(fileName)

      for x in printLocList:
         print(x)

      f=open(fileName,"a");
      for x in printLocList:
         f.write(x)
         f.write("\n")
      f.close()

   def readInputfile(self,inputfile):
     f = open( inputfile , "r")
     for x in f:
      self.PlayerTeam.append(x)
     f.close()
   
   def validatePlayerName(self,pName):
      try:
         tmp = ipl.players.index(pName)
         return "SUCCESS"
      except:
         return "Invalid Player Name " + pName + " or Player is not assoscited with any Franchise"

   def generateAssociations(self):
     for x in self.PlayerTeam:
       pt =  x.split("/")
       
       counter = 1  # to remove space for each player due to reading the CSV , no space for Franchise 
       franchise = pt[0].replace(' ','')
       self.franchises.append(franchise)
       
       for a in pt:
          if counter > 1 :
            player = a.strip()            
            self.associations.append([franchise,player])           
            
          else :
            counter = counter + 1
            
 
   def generatePlayers_fromAssociations(self):

      for tmp_association in self.associations:
         match = 0
         for tmp_player in self.players:
            if (tmp_association[1] == tmp_player) :
               match = match + 1
         if match == 0:  
               self.players.append(tmp_association[1])   
      
   def generateGraph_adjencyList(self):
      
      self.generateAssociations()
  
     # generating franchise and franhiseEdges 
      for x in self.PlayerTeam:
         edge_f = []  
         pt =  x.split("/")   
      
         # edge_f.append(pt[0].replace(' ',''))
         edge_f.append(pt[0].strip())
         for a in pt[1:len(pt)]:
            # edge_f.append(a.replace('\n','').replace(' ',''))
            edge_f.append(a.strip())     

         self.edges.append(edge_f)
         
     
     
      # generating player  and playerEdges    
      self.generatePlayers_fromAssociations()   
  
      for p in self.players:
         edge_p =[]
         edge_p.append(p)    
         edge_ps = [ x for x in self.associations if x[1] == p ]
         for a in edge_ps:
            edge_p.append(a[0])
            
         self.edges.append(edge_p)
     
 
   def displayAll(self):

      ipl.printList.clear()
      var1 = "--------Function displayAll --------"
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "Total no. of franchises: " + str(len(self.franchises));
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "Total no. of player: " + str(len(self.players))
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "\nList of franchises:"
      ipl.printList.insert(len(ipl.printList), var1)
      ipl.printList = ipl.printList + self.franchises 
      var1 = "\nList of players:"
      ipl.printList.insert(len(ipl.printList), var1)
      ipl.printList = ipl.printList + self.players
      ipl.writeIntoOutFile(ipl.printList,"outputPS28.txt","N")


      try:
         f=open("promptsPS28.txt","r");
      except:
         print("promptsPS28.txt File not found")
         quit()
      
      for x in f:

         #--------Call Function displayFranchises --------
         if(x.find('findFranchise:') >= 0):
            ipl.findFranchise(x)

         #--------Call Function displayPlayers --------
         if(x.find('listPlayers:') >= 0):
            ipl.listPlayers(x)

         #--------Call Function franchiseBuddies --------
         if(x.find('franchiseBuddies:') >= 0):
            ipl.findFranchiseBuddies(x)

         #--------Call Function findPlayerConnect --------
         if(x.find('playerConnect:') >= 0):
            ipl.playerConnect(x)

   def findFranchise(self,promptFileLine):
      x= promptFileLine
      plyrNam = x.split("findFranchise:")[1].strip()
      ipl.printList.clear()
      var1 = "\n--------Function displayFranchises --------"
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "Player name: " + plyrNam
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "List of Franchises: \n" + ipl.getStringFromList(ipl.displayFranchises(plyrNam))
      ipl.printList.insert(len(ipl.printList), var1)
      ipl.writeIntoOutFile(ipl.printList,"outputPS28.txt","N")

   def listPlayers(self,promptFileLine):
      x= promptFileLine
      frnchNam = x.split("listPlayers:")[1].strip()
      ipl.printList.clear()
      var1 = "\n--------Function displayPlayers --------"
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "Franchise name: " + frnchNam
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "List of Players: \n" + ipl.getStringFromList(ipl.displayPlayers(frnchNam))
      ipl.printList.insert(len(ipl.printList), var1)
      ipl.writeIntoOutFile(ipl.printList,"outputPS28.txt","N")

   def findFranchiseBuddies(self,promptFileLine):
      x= promptFileLine
      plyrNms = x.split("franchiseBuddies:")[1].strip()
      plyrNmA = plyrNms.split(":")[0].strip()
      plyrNmB = plyrNms.split(":")[1].strip()
      ipl.printList.clear()
      var1 = "\n--------Function franchiseBuddies --------"
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "Player A: " + plyrNmA
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "Player B: " + plyrNmB + "\n"
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = ipl.franchiseBuddies(plyrNmA,plyrNmB)
      ipl.printList.insert(len(ipl.printList), var1)
      ipl.writeIntoOutFile(ipl.printList,"outputPS28.txt","N")


   def playerConnect(self,promptFileLine):
      x= promptFileLine
      plyrNms = x.split("playerConnect:")[1].strip()
      plyrNmA = plyrNms.split(":")[0].strip()
      plyrNmB = plyrNms.split(":")[1].strip()
      ipl.printList.clear()
      var1 = "\n--------Function findPlayerConnect --------"
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "Player A: " + plyrNmA
      ipl.printList.insert(len(ipl.printList), var1)
      var1 = "Player B: " + plyrNmB + "\n"
      ipl.printList.insert(len(ipl.printList), var1)

      var1 = ipl.findPlayerConnect(plyrNmA,plyrNmB)
      ipl.printList.insert(len(ipl.printList), var1)
      ipl.writeIntoOutFile(ipl.printList,"outputPS28.txt","N")


   def getStringFromList(self,locList):
      tempStr = ""
      for x in locList:
         if(len(tempStr)>0):
            tempStr = tempStr + "\n" + x
         else:
            tempStr = tempStr + x
      return tempStr

   def displayFranchises(self,player):
      for tmp_edges in self.edges:
         if (tmp_edges[0] == player ) :
            print("Player " + player + " " + str(tmp_edges[1:len(tmp_edges)]))
            return (tmp_edges[1:len(tmp_edges)])
      
      tmpLst = ["Player " + player + " is not assosciated with any Franchise"]   
      return (tmpLst)
    
   def displayPlayers(self, franchise):
      for tmp_edges in self.edges:
         if (tmp_edges[0] == franchise):
           return (tmp_edges[1:len(tmp_edges)])
      
      tmpLst = ["Invalid Franchise : " + franchise + " or No Player is assosciated with the Franchise"]   
      return (tmpLst)

   def getNeighbours(self,vertex):
      for i in self.edges:
            if (i[0] == vertex):
               #  print ("I am important ........    " , vertex, "     " , len(i)  )
               #  print (i[1:len(i)]  )
               return i[1:len(i)]

   def bfs_traversal(self,sourceVertex,destnationVertex):
         

         # traversal  - find path between 2 players 
         # print (".................   BFS Traversal  between " ,  sourceVertex , " and " ,    destnationVertex, " is  ..................")  
         # print()
         # print()

         queue = []     # Initialize a queue
         visited = []   # List to keep track of visited nodes.
         
         # queue.append("KedarJadhav")
         # visited.append("KedarJadhav")  

         # queue.append("KrunalPandya")
         # visited.append("KrunalPandya")

         queue.append(sourceVertex)
         visited.append(sourceVertex)
         
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it

          
         breakIND = False
         parent = []    
         while queue:
               s = queue.pop(0) 
            #    level.append([s,counter])
               if breakIND == True:
                     break 
                        
               for neighbour in self.getNeighbours(s):
                     if (s == destnationVertex):    
                        breakIND = True
                        break
                     if neighbour not in visited: 
                        visited.append(neighbour)
                        queue.append(neighbour)
                        parent.append([neighbour,s])   
               
         # print()
         # print (visited)
         # print()


         # traversal  - find path between 2 players  with parent 
         # print (".................   Traversal between - KedarJadhav  and  IshanKishan  with parent    ..................")  
         # print(parent)
         # print()
         # print()   


         PATH = []

         PATH.append(destnationVertex) 

         for p in PATH:
            if p == sourceVertex:
               break
            for i in parent:
                  if i[0] == p:
                        PATH.append(i[1])           
         return (PATH)
    
   def franchiseBuddies(self, playerA, playerB):
      
      #-- Validate Player Names
      tmpStatus = ipl.validatePlayerName(playerA)
      if ( tmpStatus != "SUCCESS"): return tmpStatus
      tmpStatus = ipl.validatePlayerName(playerB)
      if ( tmpStatus != "SUCCESS"): return tmpStatus


      TMPPATH = self.bfs_traversal(playerA,playerB)
      # print()
      # print("The PATH ......................")
      # print (TMPPATH)
      if len(TMPPATH)  == 3 :
         #print ("Yes , " ,  playerA , " and " , playerB , " are Buddies " ,  " via " , TMPPATH[1] ) 
         var1 = "Yes , " +  playerA + " and " + playerB + " are Buddies " +  " via " + TMPPATH[1]
         return var1

      else :
         #print ("No , " ,  playerA , " and " , playerB , " are Not Buddies" )
         var1 = "No , " +  playerA + " and " + playerB + " are Not Buddies "
         return var1   
               
   def findPlayerConnect(self, playerA, playerB):

      #-- Validate Player Names
      tmpStatus = ipl.validatePlayerName(playerA)
      if ( tmpStatus != "SUCCESS"): return tmpStatus
      tmpStatus = ipl.validatePlayerName(playerB)
      if ( tmpStatus != "SUCCESS"): return tmpStatus

      TMPPATH = self.bfs_traversal(playerA,playerB)
      if len(TMPPATH)  == 5 :
         TMPPATH.reverse()
         #print ("Yes , " ,  playerA , " and " , playerB,"are player connect " ,  "via" , TMPPATH )     
         return "Related: Yes, " + " > ".join(TMPPATH)
      
      return playerA + " and " + playerB + " are not connected"

   

ipl = IPL()
       
# print ("--------------------------------" , " Initialised ", "-----------------")     

ipl.readInputfile("inputPS28.txt" )
ipl.generateGraph_adjencyList()
       
#print ("--------------------------------  Display IPL Graph  -----------------")     


var1="--------------------------------  Display IPL Graph  -----------------";
ipl.printList.insert(len(ipl.printList), var1)
ipl.writeIntoOutFile(ipl.printList,"outputPS28.txt","Y")




ipl.displayAll()

#print ("--------------------------------" , " DIRECT ACCESS of Graph ", "-----------------")     
#print(ipl.associations[0][0])


# print ("--------------------------------" , " The franchises associations of BenStokes are  ", "-----------------")   
# ipl.displayFranchises("BenStokes") 


# print ("--------------------------------" , " The players of franchises - SRH are  ", "-----------------")   
# ipl.displayPlayers("SRH") 

#print ("--------------------------------" , " Are KedarJadhav and IshanKishan a franchises - buddies  ", "-----------------")

# ipl.printList.clear()
# var1 = "-------------------------------- Are KedarJadhav and IshanKishan a franchises - buddies  -----------------"
# ipl.printList.insert(len(ipl.printList), var1)
# ipl.writeIntoOutFile(ipl.printList,"outputPS28.txt","N")

# ipl.franchiseBuddies( "KedarJadhav" , "IshanKishan")


# #print ("--------------------------------" , " Are there any connected players between -  KedarJadhav and IshanKishan  ", "-----------------")   
# ipl.printList.clear()
# var1 = "-------------------------------- Are there any connected players between -  KedarJadhav and IshanKishan  -----------------"
# ipl.printList.insert(len(ipl.printList), var1)
# ipl.writeIntoOutFile(ipl.printList,"outputPS28..txt","N")

# ipl.findPlayerConnect( "KedarJadhav", "IshanKishan")
