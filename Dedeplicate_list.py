l = [1,2,3,4,4,5,5,6,1]
print([x for x in l if l.count(x) == 1])
print([x for x in l if l.count(x) > 1])


result = list()
map(lambda x: not x in result and result.append(x), l)
print(result)

uniqueList = []

for letter in l:
    if letter not in uniqueList:
        uniqueList.append(letter)
        
print(uniqueList) 