class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or(head.val == None):
            return False
        s = head
        f = head
        while(f.next and f.next.next):
            s=s.next
            f=f.next.next
            print(s.val,f.val)
            if (s==f):
                return True

        return False
