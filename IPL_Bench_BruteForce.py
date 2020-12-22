print ("hello world")
# https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array

players = []
franchise = []
PlayerTeam=[]
associations=[]


def readInputfile(inputfile):
  f = open( inputfile , "r")
  for x in f:
      PlayerTeam.append(x)
  f.close()
      
  for x in PlayerTeam:
      pt =  x.split("/")
      franchise.append( pt[0].replace(' ',''))
      counter = 1
      for a in pt:
          if counter > 1 :   
            associations.append([pt[0].replace(' ',''),a.replace('\n','').replace(' ','')])
          else :
            counter = counter + 1


def displayAll():
      print(associations)   
      print("No of Teams : "  , len(PlayerTeam))
      print ("4th Team is : " , PlayerTeam[3])
      print ("4th franchise  is : " , franchise[3])
  
   
      
      
      print ("--------------------------------" , " The franchises are ", "-----------------")   
      print ("no of franchises are : " , len(franchise))
      print (franchise)
      
      print ("--------------------------------" , " The Players are ", "-----------------")    
      for tmp_association in associations:
          match = 0
          for tmp_player in players:
              if (tmp_association[1] == tmp_player) :
                match = match + 1
          if match == 0  :  
            players.append(tmp_association[1])
      print ("no of player are : " , len(players))
      print (players)



      
      

def displayFranchises(player):
    tmpFranchises = []
    for tmp_association in associations:
      if (tmp_association[1] == player ) :
            tmpFranchises.append(tmp_association[0])
    return (tmpFranchises)

def displayPlayers(franchise):
      tmpPlayers = []
      for tmp_association in associations:
         if (tmp_association[0] == 'SRH') :
           tmpPlayers.append(tmp_association[1])
      return tmpPlayers
      


        
# print ("--------------------------------" , " The Self - initialised ", "-----------------")     

readInputfile("inputPS28.txt" )

       
print ("--------------------------------" , " The Self - display  ", "-----------------")     

displayAll()

print ("--------------------------------" , " The Self - DIRECT ACCESS  ", "-----------------")     
print(associations[0][0])


print ("--------------------------------" , " The franchises associations of BenStokes are  ", "-----------------")   
print  (displayFranchises("BenStokes") )   


print ("--------------------------------" , " The players of franchises - SRH are  ", "-----------------")   
print( displayPlayers("SRH") )


    
print ("--------------------------------" , " Are  GlennMaxwell and SanjuSamson a franchises - buddies  ", "-----------------")   

tmp_frans = []
for tmp_association in associations:
      if (tmp_association[1] == 'GlennMaxwell') :
        tmp_frans.append(tmp_association[0])

for tmp_fran in tmp_frans:
         for tmp_association in associations:
           if (tmp_association[1] == 'SanjuSamson' and tmp_association[0] == tmp_fran ) :
              print ( "yes , in the franchise : " ,  tmp_fran )

# Can two players A and B be connected such that there exists another player C 
#         where A and C are franchise buddies , and C and B are franchise buddies.
# Step 1a : Get Francises of A  in FRANS-A[]
# Step 1b : Get players of A's Francises in  Buddies_A[]
# Similarly get buddies of B.
# Step 2 : Buddies of A and Buddies of B.
# Step 2 : Match the buddies , if does , print the player 

FRA_A= []
FRA_B = []

Buddies_A = []
Buddies_B = []

for tmp_association in associations:
      if (tmp_association[1] == 'BenStokes') :
        FRA_A.append(tmp_association[0])
      if (tmp_association[1] == 'ChrisWoakes') :
        FRA_B.append(tmp_association[0])



for tmp_FRA_A in FRA_A:
      for tmp_association in associations:
          if (tmp_association[0] == tmp_FRA_A )  :
                Buddies_A.append(tmp_association[1])


for tmp_FRA_B in FRA_B:
      for tmp_association in associations:
          if (tmp_association[0] == tmp_FRA_B )  :
                Buddies_B.append(tmp_association[1])   

print ("--------------------------------" , " Buddies of BenStokes  ", "-----------------")                   
print(Buddies_A)
print ("--------------------------------" , " Buddies of ChrisWoakes ", "-----------------")     
print(Buddies_B)

print ("--------------------------------" , " Common Buddies of ChrisWoakes and BenStokes are ", "-----------------")    

for bud_tmp1 in Buddies_A :
      for bud_tmp2 in Buddies_B :
            if bud_tmp1 == bud_tmp2 :
                  print (bud_tmp1)

