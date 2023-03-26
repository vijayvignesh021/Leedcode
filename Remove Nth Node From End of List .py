class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            front = head
            back = head
            
            while n > 0:
                front = front.next
                n -= 1
                
            if not front :
                return head .next

            while front.next :
                back = back.next
                front = front.next

            back.next = back.next.next
            return head
