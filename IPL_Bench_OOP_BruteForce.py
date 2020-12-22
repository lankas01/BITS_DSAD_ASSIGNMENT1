print ("hello world")
# https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
class IPL:
   PlayerTeam=[]    
   edges=[[],[]]
     
   players = []
   franchise = []

   associations=[]
   
#   def __init__(self):
#        """
#         self.
#         docstring
#       """
#       raise NotImplementedError

   def readInputfile(self,inputfile):
     f = open( inputfile , "r")
     for x in f:
      self.PlayerTeam.append(x)
     f.close()
      
     for x in self.PlayerTeam:
       pt =  x.split("/")
       self.franchise.append( pt[0].replace(' ',''))
       counter = 1
       for a in pt:
          if counter > 1 :   
            self.associations.append([pt[0].replace(' ',''),a.replace('\n','').replace(' ','')])
          else :
            counter = counter + 1

   def displayAll(self):
      print(ipl.associations)   
      print("No of Teams : "  , len(ipl.PlayerTeam))
      print ("4th Team is : " , ipl.PlayerTeam[3])
      print ("4th franchise  is : " , ipl.franchise[3])
   
      
      print ("--------------------------------" , " The franchises are ", "-----------------")   
      print ("no of franchises are : " , len(ipl.franchise))
      print (ipl.franchise)
      
      print ("--------------------------------" , " The Players are ", "-----------------")    
      for tmp_association in ipl.associations:
          match = 0
          for tmp_player in ipl.players:
              if (tmp_association[1] == tmp_player) :
                match = match + 1
          if match == 0  :  
            ipl.players.append(tmp_association[1])
      print ("no of player are : " , len(ipl.players))
      print (ipl.players)
 
   def displayFranchises(self,player):
       tmpFranchises = []
       for tmp_association in ipl.associations:
            if (tmp_association[1] == player ) :
                  tmpFranchises.append(tmp_association[0])
       return (tmpFranchises)

   def displayPlayers(self,franchise):
      tmpPlayers = []
      for tmp_association in ipl.associations:
         if (tmp_association[0] == 'SRH'):
           tmpPlayers.append(tmp_association[1])
      return tmpPlayers

   def franchiseBuddies(self, playerA, playerB):
       tmp_frans = []
       for tmp_association in self.associations:
            if (tmp_association[1] == playerA ) :
                        tmp_frans.append(tmp_association[0])

       for tmp_fran in tmp_frans:
            for tmp_association in self.associations:
                  if (tmp_association[1] == playerB and tmp_association[0] == tmp_fran ) :
                   print ( "yes , in the franchise : " ,  tmp_fran )
                   return tmp_fran 
             
   def findPlayerConnect(self, playerA, playerB):
        FRA_A= []
        FRA_B = []

        Buddies_A = []
        Buddies_B = []

        for tmp_association in self.associations:
            if (tmp_association[1] == playerA) :
               FRA_A.append(tmp_association[0])
            if (tmp_association[1] == playerB) :
               FRA_B.append(tmp_association[0])

        for tmp_FRA_A in FRA_A:
            for tmp_association in self.associations:
                if (tmp_association[0] == tmp_FRA_A )  :
                    Buddies_A.append(tmp_association[1])


            for tmp_FRA_B in FRA_B:
                  for tmp_association in self.associations:
                    if (tmp_association[0] == tmp_FRA_B )  :
                        Buddies_B.append(tmp_association[1])   

        print ("--------------------------------" , " Buddies of playerA  ", "-----------------")                   
        print(Buddies_A)
        print ("--------------------------------" , " Buddies of PlayerB ", "-----------------")     
        print(Buddies_B)

        print ("--------------------------------" , " Common Buddies of ChrisWoakes and BenStokes are ", "-----------------")    

        for bud_tmp1 in Buddies_A :
                  for bud_tmp2 in Buddies_B :
                        if bud_tmp1 == bud_tmp2 :
                              print (bud_tmp1)      

         
         

ipl = IPL()
       
# print ("--------------------------------" , " Initialised ", "-----------------")     

ipl.readInputfile("inputPS28.txt" )
       
print ("--------------------------------" , " Display IPL Graph ", "-----------------")     

ipl.displayAll()

#print ("--------------------------------" , " DIRECT ACCESS of Graph ", "-----------------")     
#print(ipl.associations[0][0])


print ("--------------------------------" , " The franchises associations of BenStokes are  ", "-----------------")   
ipl.displayFranchises("BenStokes") 


print ("--------------------------------" , " The players of franchises - SRH are  ", "-----------------")   
ipl.displayPlayers("SRH") 

print ("--------------------------------" , " Are  KedarJadhav and IshanKishan a franchises - buddies  ", "-----------------")   

ipl.franchiseBuddies( "KedarJadhav" , "IshanKishan")


print ("--------------------------------" , " are there any connected players between -  KedarJadhav and IshanKishan  ", "-----------------")   
ipl.findPlayerConnect( "KedarJadhav", "IshanKishan")