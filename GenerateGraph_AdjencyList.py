print ("hello world")

class IPL:
   PlayerTeam=[]
   association=[]    
   edges=[]
  
   def readInputfile(self,inputfile):
     f = open( inputfile , "r")
     for x in f:
      self.PlayerTeam.append(x)
     f.close()
     
     
   def generateAssociation(self):
      for x in self.PlayerTeam:
          pt =  x.split("/")
          counter = 1
          for a in pt:
              if counter > 1 :   
                self.association.append([a.replace('\n','').replace(' ',''), pt[0].replace(' ','')])
              else :
                counter = counter + 1  
        
   def generateGraph_adjencyList(self):   
     for x in self.PlayerTeam:
       pt =  x.split("/")
       print (pt); 
       counter = 1
       for a in pt:
          if counter > 1 :   
            self.association.append([pt[0].replace(' ',''),a.replace('\n','').replace(' ','')])
          else :
            counter = counter + 1
   
            
            
            
ipl = IPL()
       
print ("--------------------------------" , " Generate Graph ", "-----------------")     

ipl.readInputfile("inputPS28.txt" )

ipl.generateGraph_adjencyList()

print ("--------------------------------" , " Associations are ", "-----------------")   
print(ipl.association)

print ("--------------------------------" , " Edges are ", "-----------------")   
print(ipl.edges)
       
       
