#Tree Practice

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _createMinTree(arr, start, end):
    # Base case: if the range is invalid, there is no subtree to build
    if end < start:
        return None
    # Pick the middle element — this keeps the tree balanced
    #mid is not the value of the middle of the list but the position itself
    mid = (start + end) // 2

    # Create a node using the middle value
    newNode = Node(arr[mid])

    # Recursively build the left subtree from the left half of the array
    newNode.left = _createMinTree(arr, start, mid - 1)
    # Recursively build the right subtree from the right half of the array
    newNode.right = _createMinTree(arr, mid + 1, end)

    # Return the constructed subtree root
    return newNode


def createMinTree(arr):
    #start is 0 while end is length of the list
    return _createMinTree(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    root = createMinTree([1, 2, 3])
