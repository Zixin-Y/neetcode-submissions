from math import trunc
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if len(token) > 1 or token[0].isdigit():
                st.append(int(token))
                continue
            
            x = st.pop()
            if token =='+':
                st[-1] += x
            elif token == '-':
                st[-1] -= x
            elif token == '*':
                st[-1] *= x
            else:
                st[-1] = trunc(st[-1] / x)
        return st[0]