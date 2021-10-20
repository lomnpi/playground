def merge_sort(myList):
    if len(myList) <= 1:
        return myList

    left_half, right_half = split(myList)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(myList):
    mid = len(myList)//2
    left = myList[:mid]
    right = myList[mid:]
    
    return left, right

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

def verify(myList):
    if len(myList) <= 1:
        return True
    f = myList[0]
    for i in range(1, len(myList)):
        if myList[i] < f:
            return False
        f = myList[i]
    return True
        


yulyList = [9, 19, 63, 88, 19, 65, 59, 8, 12, 11]
temp = merge_sort(yulyList)

print(verify(yulyList))
print(verify(temp))