#You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order,
# and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to simplify the construction of the result
        dummy_head = ListNode(0)
        tail = dummy_head
        carry = 0

        # Iterate until we've processed all nodes in both lists and there's no carry left
        while l1 or l2 or carry:
            # Get the current digits from l1 and l2 (or 0 if the node is None)
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            # Calculate the sum and the new carry
            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            # Create a new node with the digit and add it to the result
            new_node = ListNode(digit)
            tail.next = new_node
            tail = tail.next

            # Move to the next nodes in l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result (skip the dummy node)
        return dummy_head.next