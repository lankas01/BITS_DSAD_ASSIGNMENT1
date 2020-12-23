# An example to demonstrate the 2D Array in Python

edges=[]

edges.append(["F1","P1"])
edges.append(["F1","P2"])
edges.append(["F1","P3"])

print (edges[1][0])
print (edges)


# https://www.geeksforgeeks.org/multi-dimensional-lists-in-python/

# Python program to demonstrate that we 
# can access multidimensional list using 
# square brackets 
a = [ [2, 4, 6, 8 ],  
    [ 1, 3, 5, 7 ],  
    [ 8, 6, 4, 2 ],  
    [ 7, 5, 3, 1 ] ]  
          

a.append([5, 10, 15, 20, 25]) 

for i in range(len(a)) :  
    for j in range(len(a[i])) :  
        print(a[i][j], end=" ") 
    print()   