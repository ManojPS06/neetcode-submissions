# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
                    val=[]
                    cur=head
                    while cur:
                        val.append(cur.val)
                        cur=cur.next
                    val.reverse()

                    cur=head
                    for v in val:
                        cur.val=v
                        cur=cur.next
                    return head
#o(n)->val 
            