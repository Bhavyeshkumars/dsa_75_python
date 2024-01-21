class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        print(s)
        print(t)

        return True if s == t else False


obj = Solution()
print(obj.isAnagram(s = "anagram", t = "nagaram"))
print(obj.isAnagram(s = "rat", t = "car"))
print(obj.isAnagram(s = "cat", t = "tac"))
      
