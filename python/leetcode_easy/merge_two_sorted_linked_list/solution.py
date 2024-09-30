from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.

        The function takes the heads of two sorted singly-linked lists (list1 and list2)
        and merges them into a single sorted linked list. It returns the head of the
        merged list. The new list is made by arranging nodes from both input lists.

        Parameters:
        list1 (Optional[ListNode]): The head of the first sorted linked list.
        list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
        Optional[ListNode]: The head of the merged sorted linked list.

        Time Complexity:
        O(n + m) where 'n' is the number of nodes in list1 and 'm' is the number of nodes in list2.
        This is because we traverse through both lists exactly once.

        Space Complexity:
        O(1) since we are not using any additional space proportional to the input size. 
        The space used is constant aside from the input lists, as we are just re-arranging the existing nodes.
        """
        # Create a dummy node to form the base of the merged linked list
        dummy = ListNode()
        current = dummy
        
        # While both lists have elements to compare
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If either of the lists is not empty, append the rest of it
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the merged list, which starts from dummy.next
        return dummy.next
