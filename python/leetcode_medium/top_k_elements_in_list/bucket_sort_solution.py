from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Return the k most frequent elements in the list `nums`.

        The solution uses a bucket sort approach where the index of the bucket represents 
        the frequency of elements. This allows us to efficiently collect the top k 
        frequent elements in linear time.

        Steps:
        1. Count the frequency of each element in `nums`.
        2. Place each element in the appropriate bucket based on its frequency.
        3. Collect elements from the highest frequency buckets until we have k elements.

        Time Complexity:
        - O(N), where N is the number of elements in `nums`. 
          - Counting frequencies takes O(N).
          - Placing elements in frequency buckets takes O(N).
          - Collecting the top k elements in the worst case takes O(N).

        Space Complexity:
        - O(N), where N is the number of elements in `nums`.
          - The frequency map (`count`) requires O(N) space.
          - The bucket list (`freq`) requires O(N) space.
          - The result list (`res`) may hold up to k elements, but this is bounded by O(N) as well.
        
        Args:
        nums (List[int]): A list of integers where some elements may repeat.
        k (int): The number of most frequent elements to return.

        Returns:
        List[int]: A list containing the k most frequent elements from `nums`.
        """
        
        # Step 1: Count the frequency of each element in nums
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]


        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Step 2: Place each element in the appropriate frequency bucket
        for n, c in count.items():
            freq[c].append(n)

        # Step 3: Collect the top k frequent elements starting from the highest frequency
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
