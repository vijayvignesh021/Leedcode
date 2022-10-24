# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        heard = ListNode(0)
        tail = heard
        rem = 0
        while(l1 != None and l2 != None):
            tail.next = ListNode((l1.val + l2.val + rem)%10)
            rem = (l1.val + l2.val+rem)//10
            l1=l1.next
            l2=l2.next
            tail = tail.next
        while(l1 != None and l2 == None):
            tail.next = ListNode((l1.val + rem)%10)
            rem = (l1.val+rem )//10
            l1=l1.next
            tail = tail.next
        while(l1 == None and l2 != None):
            tail.next = ListNode((l2.val + rem)%10)
            rem = (l2.val+rem )//10
            print(rem)
            l2=l2.next
            tail = tail.next
        if rem != 0:
            tail.next =  ListNode(rem)
        return heard.next
