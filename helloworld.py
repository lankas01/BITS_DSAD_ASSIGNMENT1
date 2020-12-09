
print ("hello world")
players = []
franchise = []
PlayerTeam=[]
associations=[]

f = open("inputPS28.txt" , "r")
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
        
print ("--------------------------------" , " The Associations ", "-----------------")            
print(associations)   

print("No of Teams : "  , len(PlayerTeam))
print ("4th Team is : " , PlayerTeam[3])
print ("4th franchise  is : " , franchise[3])

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

print ("--------------------------------" , " The franchises are ", "-----------------")   
print ("no of franchises are : " , len(franchise))
print (franchise)


print ("--------------------------------" , " The franchises associations of BenStokes are  ", "-----------------")   

for tmp_association in associations:
  if (tmp_association[1] == 'BenStokes') :
    print (tmp_association[0])
    
print ("--------------------------------" , " The players of franchises - SRH are  ", "-----------------")   

for tmp_association in associations:
  if (tmp_association[0] == 'SRH') :
    print (tmp_association[1])
    
print ("--------------------------------" , " Are  GlennMaxwell and SanjuSamson a franchises - buddies  ", "-----------------")   

tmp_frans = []
for tmp_association in associations:
      if (tmp_association[1] == 'GlennMaxwell') :
        tmp_frans.append(tmp_association[0])

for tmp_fran in tmp_frans:
         for tmp_association in associations:
           if (tmp_association[1] == 'SanjuSamson' and tmp_association[0] == tmp_fran ) :
              print ( "yes , in the franchise : " ,  tmp_fran )

#Can two players A and B be connected such that there exists another player C 
#         where A and C are franchise buddies and C and B are franchise buddies.
# Step 1 : Buddies of A and Buddies of B.
# Step 2 : Match the buddies , if does , print the player 

print ("--------------------------------" , " Buddies of  GlennMaxwel  ", "-----------------")   

for tmp_association in associations:
      if (tmp_association[1] == 'GlennMaxwell') :
        tmp_frans.append(tmp_association[0])
    