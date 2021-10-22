""" 
Merge Sort Algorithm

Steps:
Divide: Find the midpoint of list and floor divide into two sublists
Conquer: Recursively sort the sublists created in previous step
Combine: Merge the sorted sublists created in previous step
"""
def merge_sort(myList):
    if len(myList) <= 1:
        return myList

    left_half, right_half = split(myList)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

# Divides list into two
def split(myList):
    mid = len(myList)//2
    left = myList[:mid]
    right = myList[mid:]
    
    return left, right

# Merging left and right portions and comparing elements
def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

# Verify sorting using iteration
def verify(myList):
    if len(myList) <= 1:
        return True
    f = myList[0]
    for i in range(1, len(myList)):
        if myList[i] < f:
            return False
        f = myList[i]
    return True
        
def recur_verify(myList):
    if len(myList) <= 1:
        return True
    return myList[0] <= myList[1] and recur_verify(myList[1:])

yulyList = [9, 19, 63, 88, 19, 65, 59, 8, 12, 11]
temp = merge_sort(yulyList)

print(verify(yulyList))
print(verify(temp))
print(recur_verify(temp))
print(temp)