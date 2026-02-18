#Python Warm-up challenges
#reverse a string
myString = "The quick drown fox jumps over the lazy dog"
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
sortedLetters.pop(' ')
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
