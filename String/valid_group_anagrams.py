from typing import List
from collections import Counter, defaultdict

class Solution:
    # Solution 1
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        final_strs = []
        for st in strs:
            s = sorted(st, reverse=True)
            s = "".join(s)
            sorted_strs.append(s)

        unique_sorted_strs = list(set(sorted_strs))
             
        for st in unique_sorted_strs:
            temp_word = []
            for index, st1 in enumerate(sorted_strs):
                if st == st1:
                    temp_word.append(strs[index])

            final_strs.append(temp_word)       

        return final_strs

    # Solution 2
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        """
        - obtain frequencies of all characters using 'Counter';
        - these frequencies are used as a key for dict;
        - to uniquely identify groups, we use 'frozenset'
        - (note that 'set' is mutable, thus, can't be used as key)
        
        """
        for s in strs:
            groups[frozenset(Counter(s).items())].append(s)
        
        return list(groups.values())

# Solution 1 : Runtime:2607ms and Memory:19.73MB
# Solution 2 : Runtime:114ms and Memory:29.75MB
obj = Solution()
print(obj.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(obj.groupAnagrams(strs = [""]))
print(obj.groupAnagrams(strs = ["a"]))
      
