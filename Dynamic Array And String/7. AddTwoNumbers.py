# Definition for singly-linked list
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Pseudocode:
        # 1. Initialize a dummy node to act as a placeholder for the head of the result list.
        dummy = ListNode()
        # 2. Set a 'current' pointer to the dummy node to build the new list.
        cur = dummy
        # 3. Initialize 'carry' to 0 to store any overflow from digit addition.
        carry = 0

        # 4. Loop until both input lists are exhausted and there is no carry left.
        while l1 or l2 or carry:
            # 5. Get the value from the current node of l1, or 0 if l1 is empty.
            v1 = l1.val if l1 else 0
            # 6. Get the value from the current node of l2, or 0 if l2 is empty.
            v2 = l2.val if l2 else 0

            # 7. Calculate the sum of the two digits and the carry.
            val = v1 + v2 + carry
            # 8. Determine the new carry for the next position (e.g., 15 // 10 = 1).
            carry = val // 10
            # 9. Determine the digit for the current position (e.g., 15 % 10 = 5).
            val = val % 10
            # 10. Create a new node with the calculated digit and link it to the current node.
            cur.next = ListNode(val)

            # 11. Move the 'current' pointer forward to the new node.
            cur = cur.next
            # 12. Advance l1 to its next node if it exists, otherwise set to None.
            l1 = l1.next if l1 else None
            # 13. Advance l2 to its next node if it exists, otherwise set to None.
            l2 = l2.next if l2 else None

        # 14. The result list starts after the dummy node, so return dummy.next.
        return dummy.next
