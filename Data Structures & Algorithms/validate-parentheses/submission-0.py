class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        stack = []
        map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for c in s:
            if c not in map:
                stack.append(c)
            elif not stack or stack.pop() != map[c]:
                return False
        return not stack