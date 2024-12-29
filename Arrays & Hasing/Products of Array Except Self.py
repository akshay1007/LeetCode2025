from typing import List
class Solution():
    def productExceptSelf(self,nums:List[int])->List[int]:
        res = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            res.append(prod)
        print(res)

    def productExceptSelf2(self,nums:List[int])->List[int]:
        n = len(nums)
        print(n)
        for i in range(1,len(nums)):
            print(i)

if __name__ == "__main__":
    obj = Solution()
    input = [1,2,3,4]
    output = obj.productExceptSelf(input)
    print('Result --> ', output)