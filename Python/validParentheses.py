# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {}
        dic['('] = ')'
        dic['['] = ']'
        dic['{'] = '}'
        curr_open = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                curr_open.append(char)
            else:
                if len(curr_open) == 0:
                    return False
                if dic[curr_open[-1]] != char:
                    return False
                else:
                    curr_open.pop(-1)
        if len(curr_open) == 0:
            return True
        return False