#Python Warm-up challenges

import csv

#To make the results more readable
def newLine() :
    print("")
#reverse a string
myString = "abcab"
newString = ""
lengthOfString = len(myString)
for x in myString :
    lengthOfString = lengthOfString - 1
    newString = newString + myString[lengthOfString]
print('I took the string "' + myString + '"and I reversed it into "' + newString + '"')

#Check if a string is a pangram (contains every letter of the alphabet)
if len(myString) < 24:
    print("The string is not a pangram.")
else :
    is_pangram = set(myString.upper()) >= set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if is_pangram :
        print("The string is a pangram")
    else :
        print("The string is not a pangram")

#Count the frequency of each character and return the top 3 most common
letters = {"A": False}
for x in myString :
    y = x.upper()
    z = myString.upper()
    letters.update({y: z.count(y)})
sortedLetters = dict(sorted(letters.items(), key=lambda item: item[1]))
lastThreeItems = list(sortedLetters.items())[-3:]
print("I counted the frequency of each character and the top 3 are " + str(lastThreeItems))

#Given a sentence, capitalize the first letter of each word without using .title()
newString = ""
CapUpNext = True
for x in myString :
    if CapUpNext :
        newString = newString + x.upper()
        CapUpNext = False
    elif x == " ":
        newString = newString + x
        CapUpNext = True
    else:
        newString = newString + x
print("Without using .title()... I capitalize each word... " + newString)

#Find the longest substring without repeating characters
newString = ""
bestString = ""

for x in myString:
    if x in newString:
        index = newString.index(x)
        newString = newString[newString.index(x) + 1:] + x
    else:
        newString += x
    if len(newString) > len(bestString):
        bestString = newString
print("The longest substring without repeating characters is " + bestString)
newLine()

#Fubanacci Sequence
allFubNums = [1, 1]
nMinusOne = allFubNums[1]
nMinusTwo = allFubNums[0]
newN = 0
for i in range(25) :
    newN = nMinusOne + nMinusTwo
    allFubNums.append(newN)
    nMinusOne = allFubNums[len(allFubNums) - 1]
    nMinusTwo = allFubNums[len(allFubNums) - 2]
print("The first 25 of the Fubanacci numbers are " + ", ".join(str(num) for num in allFubNums))
newLine()

#CSV reading
#creating a new list for dicitonaries to write
newCSVtoWrite = []
#open file then read as Dictionaries
print("I'm opening cases.csv and taking the ones who own over $1,000 and")
print("compiling them into an new file.")
newLine()
with open("cases.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        #to search for overdue stuff
        amountNum = float(row["amount_owed"])
        if amountNum > 1000:
            newCSVtoWrite.append(row)
    #keeping track on how many times loop goes through (i)
    #so that it doesn't do a line break on the last one
    for i, row in enumerate(newCSVtoWrite):
        #Each row is an individual dictionary
        for key in row:
            print(key, row[key])
        if i != len(newCSVtoWrite) - 1: 
            print("-----")

with open("bigCases.csv", mode="w", newline="") as csvfile:
    fieldNames = newCSVtoWrite[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
    for row in newCSVtoWrite:
        writer.writerow(row)
newLine()

#Move all zeros to the end of the list/array
myList = [5, 7, 2, 0, 8, 0, 3]
print("Moving zero to the end of this list: " + str(myList))
for num in myList:
    if num == 0:
        myList.append(num)
        myList.remove(num)
print("Result: " + str(myList))
newLine()

#from 1 to n except for one, return the missing int.
originalList = [1, 2, 6, 7, 9, 3, 4, 10, 8]
newList = sorted(originalList)
for i, num in enumerate(newList):
    if i != 0:
        if newList[i] - newList[i-1] != 1:
            print("The missing number is " + str(newList[i] - 1))
            print("from the list " + str(originalList))
#a better way of doing things with the sum method
n = len(originalList) + 1
expectedSum = n * (n + 1) // 2
actual_sum = sum(originalList)
missing = expectedSum - actual_sum
print("The sum method got the missing number of ", missing)
