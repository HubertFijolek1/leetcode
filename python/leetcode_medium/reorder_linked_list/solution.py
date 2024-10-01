from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the given linked list in a specific order where the nodes follow the pattern:
        [first, last, second, second-last, third, third-last, ...]

        The reordering is done in-place without modifying the values of the nodes, but by rearranging
        the node pointers.

        Steps:
        1. Find the middle of the linked list using the slow and fast pointer technique.
        2. Reverse the second half of the linked list starting from the middle.
        3. Merge the first half with the reversed second half, alternating between nodes.

        Args:
        head (ListNode): The head node of the linked list to reorder.

        Time Complexity:
        O(n) - where n is the number of nodes in the linked list.
               - Finding the middle takes O(n/2), reversing the second half takes O(n/2),
                 and merging the two halves takes O(n).
        
        Space Complexity:
        O(1) - We only use a few extra pointers, so the space complexity is constant.

        Example:
        Input: [1, 2, 3, 4, 5]
        After reordering: [1, 5, 2, 4, 3]

        Input: [1, 2, 3, 4, 5, 6]
        After reordering: [1, 6, 2, 5, 3, 4]
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # After this loop, 'slow' is at the middle node
        
        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next  # Store the next node temporarily
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move prev to current
            curr = next_temp       # Move to the next node
        
        # At the end of this loop, 'prev' is the new head of the reversed second half
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next  # Save the next nodes temporarily
            first.next = second  # Link first node to second node
            second.next = temp1  # Link second node to the next node in first half
            first, second = temp1, temp2  # Move to the next nodes in both halves
