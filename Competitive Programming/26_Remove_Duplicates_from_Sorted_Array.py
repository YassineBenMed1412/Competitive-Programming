class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  
        
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  
                nums[index] = nums[i]
                index += 1

        return index  

nums = [1, 1, 2]
sol = Solution()
length = sol.removeDuplicates(nums)


print("Length of array after deduplication:", length)