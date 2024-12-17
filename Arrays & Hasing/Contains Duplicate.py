#Given an integer array nums, return true if any value appears more than once in the array, 
# otherwise return false.
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         d ={}
         for e in nums:
            if e in d:
                return True
            d[e] = 1
         return False
    
if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 3]
    output  = True
    result = obj.hasDuplicate(nums)
    print(result)

