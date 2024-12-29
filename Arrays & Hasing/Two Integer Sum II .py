from collections import defaultdict
from typing import List
class Solution():
    def twoSum(self,nums:List[int], target : int)->List[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i+1, j+1]
    
        
    def twoSum2(self,nums:List[int], target : int)->List[int]:
        mp = defaultdict(int)
        for i in range(len(nums)):
            temp = target - nums[i]
            if mp[temp]:
                return [mp[temp], i+1]
            mp[numbers[i]] = i + 1
        return []
  
if __name__ == "__main__":
    obj = Solution()
    numbers = [1,2,3,4]
    target = 3
    output = obj.twoSum2(numbers, target)
    print('Result --> ', output)