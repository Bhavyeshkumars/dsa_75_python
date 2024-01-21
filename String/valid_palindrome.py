class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_str = ""
        for ch in s:
            if ch.isalnum():
                formatted_str += ch.lower()
        print(formatted_str)

        if formatted_str == formatted_str[::-1]:
            return True
        else:
            return False
        

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
print(obj.isPalindrome("race a car"))
print(obj.isPalindrome("tat"))
print(obj.isPalindrome(""))





