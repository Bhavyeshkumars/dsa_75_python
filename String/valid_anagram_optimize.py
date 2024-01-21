class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            count_s={}
            count_t={}
            for char in s:
                count_s[char] = count_s.get(char,0)+1
            for char in t:
                count_t[char] = count_t.get(char,0)+1

            print(f"count_s = {count_s}")
            print(f"count_s = {count_s}")

            if count_t == count_s:
                return True
        return False

obj = Solution()
print(obj.isAnagram(s = "anagram", t = "nagaram"))
print(obj.isAnagram(s = "rat", t = "car"))
print(obj.isAnagram(s = "cat", t = "tac"))