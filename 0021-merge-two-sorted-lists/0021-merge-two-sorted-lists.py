# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        arr = []
        temp = list1
        while temp:
            arr.append(temp.val)
            temp = temp.next
        temp = list2
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        
     
        dummy = ListNode(0)
        curr = dummy
        
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next