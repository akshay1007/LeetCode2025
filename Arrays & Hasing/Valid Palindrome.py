from typing import List
class Solution():
    def isPalindrome(self,strs:List[str]) -> bool:
        newStr = ''
        for c in strs:
            if c.isalnum():
                newStr += c.lower()
        temp = newStr[::-1]
        if newStr == temp:
            return True
        return False
        


if __name__ == "__main__":
    obj = Solution()
    strs = "Was it a car or a cat I saw?"
    res = obj.isPalindrome(strs)
    print(res)
   