import os
print (".............. IPL Bench : DSE 2020 SEC 4 - Group 280 : Assignment Solution  ........................ ")

class IPL:
    printList = []

    def writeIntoOutFile(self,printLocList,fileName,clearFileReq):

        print("clearFileReq " + clearFileReq)

        if (clearFileReq == "Y"):
            if (os.path.exists(fileName)):
                os.remove(fileName)

        f=open(fileName,"a");
        for x in printLocList:
            f.write(x)
            f.write("\n")
            f.close()

ipl = IPL()
var1 = "Total no of franchises : ";
print(var1)
ipl.printList.insert(len(ipl.printList), var1)
ipl.writeIntoOutFile(ipl.printList,"outputPS28.txt","Y")

try:
    f=open("mix1.txt","r");
except:
    print("File not found")
    quit()
    
    
print("proceeding")

