"""
Binary Search Algorithm

- Sorted List
- Best Case Constant Time Operation: O(1)
- Worst case Logarithmic Runtime: O(log n)

"""

def binary_search(myList, target):
    first = 0
    last = len(myList) - 1

    while first <= last:
        mid = (first + last)//2

        if myList[mid] == target:
            return mid
        elif myList[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None

tempList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(tempList, 5))