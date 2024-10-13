# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less, more, prev, curr = None, None, None, head
        while curr:
            if curr.val < x:
                if prev and prev.val >= x: prev.next = curr.next
                if not less:
                    less = curr
                    head = less
                else:
                    less.next = curr
                    less = less.next
            else:
                if not more: more = curr
                prev = curr
            curr = curr.next
        if prev and prev.next and prev.val >= x: prev.next = None
        if less and more: less.next = more
        return head