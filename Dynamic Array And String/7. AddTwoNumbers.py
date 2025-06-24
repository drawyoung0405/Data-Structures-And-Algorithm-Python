# Definition for singly-linked list
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
def to_linked_list(num_str):
    dummy = ListNode()
    current = dummy
    for ch in reversed(num_str):  # Reverse input like 243 → [3 → 4 → 2]
        current.next = ListNode(int(ch))
        current = current.next
    return dummy.next
def print_linked_list(node):
    while node:
        print(node.val, end= "")
        node = node.next
    print("None")
if __name__ == "__main__":
    num1 = input("Enter first number: ")  # Example: 243
    num2 = input("Enter second number: ")  # Example: 564

    l1 = to_linked_list(num1)
    l2 = to_linked_list(num2)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    print("Result Linked List:")
    print_linked_list(result)