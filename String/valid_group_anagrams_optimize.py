from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for word in strs:

            temp_word = ''.join(sorted(word))

            if temp_word in anagram:
                anagram[temp_word].append(word)

            else:
                anagram[temp_word] = [word]  

        print(f"anagram = {anagram}")
        return list(anagram.values()) 

# Runtime:84ms and Memory:19.47MB
obj = Solution()
print(obj.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(obj.groupAnagrams(strs = [""]))
print(obj.groupAnagrams(strs = ["a"]))
      
