class Solution(object):
    def isValid(self, s):
        if len(s)% 2 != 0:
            return False
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if not stack:
                    return False
                if char != stack[-1]:
                    return False
                
                stack.pop()

        return len(stack) == 0
        