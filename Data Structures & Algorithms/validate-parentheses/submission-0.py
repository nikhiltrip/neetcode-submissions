class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ['{', '(', '[']:
                stack.append(char)
            if not stack and char in ['}', ')', ']']:
                return False
            if char == '}' and stack[-1] != '{':
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            if char == '}' and stack[-1] == '{':
                stack.pop()
            if char == ')' and stack[-1] == '(':
                stack.pop()
            if char == ']' and stack[-1] == '[':
                stack.pop()
            
            
        return len(stack) == 0