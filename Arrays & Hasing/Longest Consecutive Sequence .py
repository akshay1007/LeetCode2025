from typing import List
class Solution():
    def longestConsecutive(self,nums:List[int])->int:
        store = set(nums)
        res = 0
        for num in store:
            if (num-1) not in store:
                length = 1 
                while(num+length) in store:
                    length +=1 
                res = max(res,length)
        
        return res
        

  
if __name__ == "__main__":
    obj = Solution()
    input = [2,20,4,10,3,4,5]
    output = obj.longestConsecutive(input)
    print('Result --> ', output)