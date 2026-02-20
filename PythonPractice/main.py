#Python Warm-up challenges

import csv
import sqlite3
from icecream import ic

#reverse a string
myString = "abcab"
newString = ""
lengthOfString = len(myString)
for x in myString :
    lengthOfString = lengthOfString - 1
    newString = newString + myString[lengthOfString]
print(newString)

#Check if a string is a pangram (contains every letter of the alphabet)
if len(myString) < 25 :
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
print(lastThreeItems)

#Fubanacci Sequence
allFubNums = [1, 1]
nMinusOne = allFubNums[1]
nMinusTwo = allFubNums[0]
newN = 0
x = 0
while x < 25 :
    newN = nMinusOne + nMinusTwo
    allFubNums.append(newN)
    nMinusOne = allFubNums[len(allFubNums) - 1]
    nMinusTwo = allFubNums[len(allFubNums) - 2]
    x = x + 1
print(allFubNums)

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
print(newString)

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

#CSV reading
#creating a new list for dicitonaries to write
newCSVtoWrite = []
#open file then read as Dictionaries
with open("cases.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        #to search for overdue stuff
        amountNum = float(row["amount_owed"])
        if amountNum > 1000:
            newCSVtoAdd = row
            newCSVtoWrite.append(newCSVtoAdd)

    print(newCSVtoWrite)

with open("bigCases.csv", mode="w", newline="") as csvfile:
    fieldNames = newCSVtoWrite[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
    for row in newCSVtoWrite:
        writer.writerow(row)
