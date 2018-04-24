    def isValid(s):
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif not stack:
                return False
            else:
                if c == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif c == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                else:
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
        return stack == []


#solution2: use dictionary
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_table = { ')': '(',
                              ']': '[',
                              '}': '{'
                            }
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif not stack:
                return False
            else:
                if parentheses_table[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return stack == []

    
