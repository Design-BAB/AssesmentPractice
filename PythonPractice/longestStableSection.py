nums = [1, 3, 6, 7]
k = 3

#my Solution
if len(nums) < 2:
    print("Your list is too short!")
elif len(nums) < 1 :
    print("Your list is actually empty!")
else:
    myNums = [nums[0], nums[1]]
    stableNumsList = []
    i = 1
    
    for i in range(len(nums) - 2):
        myNums.append(nums[i + 2])
        kChecker = max(myNums) - min(myNums)
        if kChecker <= k :
            stableNumsList.append(myNums.copy())
    for num in myNums:
        removeFirstOne = myNums.pop(0)
        kChecker = max(myNums) - min(myNums)
        if kChecker <= k :
            stableNumsList.append(myNums.copy())
    
    if len(stableNumsList) == 0:
        print("There is no stable list of numbers")
    else:
        winner = []
        for list in stableNumsList:
            if len(list) > len(winner):
                winner = list
    print("The winning list is... ")
    print(winner)
