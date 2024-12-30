from typing import List
class Solution():
    def groupAnagrams(self,strs:List[str]) -> List[List[str]]:
        my_dict = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in my_dict:
                my_dict[sortedS].append(s)   
            else:
                my_dict[sortedS] =  [s]
        my_res = list(my_dict.values())
        return my_res


if __name__ == "__main__":
    obj = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    res = obj.groupAnagrams(strs)
    print(res)
   