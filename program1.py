# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         pass
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to hold the mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to hold the opening brackets
        stack = []

        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the expected opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # After processing all characters, the stack should be empty if the string is valid
        return not stack

# Example usage:
sol = Solution()
print(sol.isValid("()"))        # Output: True
print(sol.isValid("()[]{}"))    # Output: True
print(sol.isValid("(]"))        # Output: False
print(sol.isValid("{[]}"))      # Output: True







    



  

