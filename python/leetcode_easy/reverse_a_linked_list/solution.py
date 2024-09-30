from typing import Optional, ListNode
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list.
        
        Given the head of a singly linked list, reverse the list and return the new head.
        
        Approach:
        1. Initialize two pointers, 'prev' and 'curr'. 'prev' starts as None, and 'curr' starts as the head of the list.
        2. Iterate through the linked list:
           - Store the next node using 'next_node = curr.next' before reversing the current node's pointer.
           - Set 'curr.next' to 'prev' to reverse the pointer direction.
           - Move 'prev' to 'curr' and 'curr' to 'next_node' to continue the reversal process.
        3. Once 'curr' becomes None (end of the list), 'prev' will point to the new head of the reversed list.
        
        Time Complexity: O(n), where n is the number of nodes in the linked list.
            - We traverse each node of the list exactly once.
        
        Space Complexity: O(1).
            - We only use a constant amount of extra space (for the pointers 'prev', 'curr', and 'next_node').
        
        Parameters:
        - head: Optional[ListNode], the head node of the linked list to be reversed.
        
        Returns:
        - Optional[ListNode]: The new head of the reversed linked list.
        
        Example:
        Input: head = [1, 2, 3, 4]
        Output: [4, 3, 2, 1]
        """
        
        prev = None   # Previous node starts as None
        curr = head   # Current node starts as the head of the list
        
        # Loop through the list
        while curr:
            next_node = curr.next  # Store the next node
            curr.next = prev       # Reverse the current node's next pointer
            prev = curr            # Move prev to the current node
            curr = next_node       # Move to the next node
        
        return prev  # prev will be the new head of the reversed list
