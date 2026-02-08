class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
        
        :param s: the string input parentheses.
        :type s: str
        :return: if the input string is valid or not.
        :rtype: bool

        for ref:
        class Solution:
          def isValid(self, s: str) -> bool:
              stack = []
              for c in s:
                  if c in "([{":
                      stack.append(c)
                  elif c in ")]}":
                      if stack:
                          openb = stack.pop()
                          if (openb == "(" and c == ")") or (openb == "{" and c == "}") or (openb == "[" and c == "]") :
                              continue
                          else:
                              return False
                      else:
                          return False
              
              return len(stack) == 0
        """""
        opening_count = 0
        prev_bracket = ""
        idx = 0

        while idx < len(s):
          if s[idx] == '[':
            opening_count += 1
          elif s[idx] == '(':
            opening_count += 1
          elif s[idx] == '{':
            opening_count += 1
          elif s[idx] == ']':
            if prev_bracket == '[':
              opening_count -= 1
              s = s[0: idx - 1] + (s[idx + 1:] if idx + 1 < len(s) else "")
              idx -= 2
            else:
              opening_count += 1
          elif s[idx] == ')':
            if prev_bracket == '(':
              opening_count -= 1
              s = s[0: idx - 1] + (s[idx + 1:] if idx + 1 < len(s) else "")
              idx -= 2
            else:
              opening_count += 1
          elif s[idx] == '}':
            if prev_bracket == '{':
              opening_count -= 1
              s = s[0: idx - 1] + (s[idx + 1:] if idx + 1 < len(s) else "")
              idx -= 2
            else:
              opening_count += 1
          
          prev_bracket = s[idx] if idx >= 0 else ""
          idx += 1
        
        return False if opening_count else True
