import os

osPath = os.path.dirname(__file__)
filepath = "input.txt"
fullPath = os.path.join(osPath, filepath)

input = open(fullPath, "r")
listA = []
listB = []

for line in input:
    numbers = line.split(" ")
    listA.append(int(numbers[0].strip()))
    listB.append(int(numbers[3].strip()))

# Part 1
listA.sort()
listB.sort()
mergedList = zip(listA, listB)

totalDif = 0

for tuple in mergedList:
    diff = abs(tuple[0]-tuple[1])
    totalDif = totalDif + diff

print(totalDif)

# Part 2

def countOccurence(a:int, array:list):
    count = 0
    for item in array:
        if int(item) == a:
            count = count + 1
    return count
    
score = 0
for num in listA:
    occurences = countOccurence(num, listB)
    score = score + (num * occurences)

print(score)