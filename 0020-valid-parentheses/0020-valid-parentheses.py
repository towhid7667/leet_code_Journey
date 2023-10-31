class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_ones = {')' : '(', '}' : '{' , ']' : '['}
        for i in s:
            if i in closed_ones:
                if stack and stack[-1] == closed_ones[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)   
        return True if not stack else False      
        