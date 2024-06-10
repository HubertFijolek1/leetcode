#time complexity  O(n2)
def brute_force(nums):
    nums2 = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums2)):
            if i == j :
                continue
            else:
                nums2[j] *= nums[i]
    return nums2

nums = [1,4,6,7,2]
print(brute_force(nums))