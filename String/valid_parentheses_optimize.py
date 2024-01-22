class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch in parentheses:
                if stack and stack[-1] == parentheses[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False

# Runtime:19ms and Memory:16.58MB
obj = Solution()
print(obj.isValid(s = "()"))
print(obj.isValid(s = "()[]{}"))
print(obj.isValid(s = "(]"))
print(obj.isValid(s = "("))
print(obj.isValid(s = "]"))