class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            elif not stack or stack.pop() != ch:
                return False
        return not stack


# Runtime:26ms and Memory:16.60MB
obj = Solution()
print(obj.isValid(s = "()"))
print(obj.isValid(s = "()[]{}"))
print(obj.isValid(s = "(]"))
print(obj.isValid(s = "("))
print(obj.isValid(s = "]"))