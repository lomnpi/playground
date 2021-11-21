# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        tempSum = 0
        dummy = ListNode()
        curNode = dummy
        
        # val1 = l1.val
        # val2 = l2.val
        
        while l1 or l2 or carry:
            tempSum = carry
            if l1:
                tempSum += l1.val
                l1 = l1.next
            if l2:
                tempSum += l2.val
                l2 = l2.next
            carry = int(tempSum / 10) # or tempSum // 10
            # if tempSum >= 10:
            #     cur = tempSum % 10
            #     carry = 1
            curNode.next = ListNode(tempSum%10)
            curNode = curNode.next
        return dummy.next