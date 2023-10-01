# didn't pass all the test case
def isValid(s):
    for i in s: 
        if i == '(' and ')' in s or i == '[' and ']' in s or i == '{' and '}' in s:
            return True
    return False 
print(isValid("()[]{}"))

# didn't pass all the test case
def isValid(s):
    for i in range(len(s)):
            for j in range(i + 1, len(s)): 
                if s[i] == '(' and s[j] == ')' or s[i] == '[' and  s[j] == ']' or s[i] == '{' and  s[j] == '}':
                    return True
    return False           
    
print(isValid("([)]"))


def isValid(s):
    stack = []
    closed_ones = {')' : '(', '}' : '{', ']' : '['}       
    
    for i in s:
        if i in closed_ones:
            if stack and stack[-1] == closed_ones[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False                   
    
print(isValid("([)]"))