# rotate list
# no time/space requirements
# return "rotated" version of input list

def oldRotate(my_list, num_rotations):
    newList = my_list.copy()
    for i in range(num_rotations):
        removedLastOne = newList.pop(len(newList) - 1)
        listOfOne = [removedLastOne]
        newList = listOfOne + newList
    print("The new list is...")
    print(newList)
    return newList

def rotate(my_list, num_rotations):
    n = len(my_list)
    if n == 0:
        return my_list
    newList = my_list.copy()
    for i in range(num_rotations):
        removedLastOne = newList.pop(len(newList) - 1)
        listOfOne = [removedLastOne]
        newList = listOfOne + newList
    print("The new list is...")
    print(newList)
    return newList

    num_rotations %= n  # handle rotations >= length

    # Left rotation by k:
    # 1) reverse first k
    # 2) reverse last n-k
    # 3) reverse whole list

    rev(my_list, 0, num_rotations - 1)
    rev(my_list, num_rotations, n - 1)
    rev(my_list, 0, n - 1)

    return my_list


def rev(lst, low, high):
    while low < high:
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1
    return lst

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['f', 'a', 'b', 'c', 'd', 'e']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['e', 'f', 'a', 'b', 'c', 'd'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['e', 'f', 'a', 'b', 'c', 'd']))

#Rotation point: Binary Search
# find rotation point 
# O(logN) time requirement
# return index of "rotation point" element

def rotation_point(rotated_list):
    midPoint = len(rotated_list) // 2
    endPoint = len(rotated_list) - 1
    for piece in rotated_list:
        location = binary_search(midPoint, endPoint, rotated_list)
        if location == "Right":
            midPoint = midPoint * 1.5
            midPoint = midPoint // 1
        elif location == "Left":
            endPoint = midPoint
            midPoint = endPoint // 2
        else:
            return location
    return None

def binary_search(midPoint, endPoint, rotated_list):
    if endPoint == midPoint + 1:
        if midPoint < endPoint:
            return midPoint
        else:
            return endPoint
    if rotated_list[midPoint] > rotated_list[endPoint]:
        return "Right"
    elif rotated_list[midPoint] < rotated_list[endPoint]:
        return "Left"




#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

