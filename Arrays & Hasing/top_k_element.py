""" Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
"""

from typing import List, Set


class Solution():
    
    def topKFrequent(self , nums:List[int],k:int)->List[int] :
        count = {}
        arr = []
        for ele in nums:
            count[ele] = count.get(ele,0)+1

        for key, value in count.items():
            arr.append([value,key])
        
        arr.sort()
        
        res = []
        while(len(res)<k):
            res.append(arr.pop()[1])

        return res
    
    def topKFrequent2(self , nums:List[int],k:int)->List[int] :
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for ele in nums:
            count[ele] = 1 + count.get(ele,0)
        
        for key , value in count.items():
            freq[value].append(key)
            print(freq)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            print('freq -- ',freq[i])
            for num in freq[i]:
                res.append(num)
                print('res ---> ', res)
                if len(res)==k:
                    return res


if  __name__ == "__main__":
    obj = Solution()
    nums = [1,2,2,3,3,3]
    k = 2
    output = obj.topKFrequent2(nums,k)
    print('output --->', output)




