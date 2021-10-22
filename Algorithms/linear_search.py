"""
Linear Search Algorithm
- Worst complexity Linear time: O(n) 
- Average complexity: O(n)
- Space complexity: O(1)
"""

def linear_search(myList, target):
    # Returns the index position of the target if found, else returns None
    for i in range(len(myList)):
        if myList[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

sampleList = [3, 4, 7, 1, 78, 9, 6, 10]

result = linear_search(sampleList, 78)
verify(result)
