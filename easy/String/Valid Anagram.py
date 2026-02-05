class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      """
      Given two strings s and t, return true if t is an anagram of s, and false otherwise.
      
      for ref:
        class Solution:
          def isAnagram(self, s: str, t: str) -> bool:  
              if len(s) != len(t):
                  return False

              counter = {}

              for char in s:
                  counter[char] = counter.get(char, 0) + 1

              for char in t:
                  if char not in counter or counter[char] == 0:
                      return False
                  counter[char] -= 1

              return True
      """
      if len(s) != len(t):
        return False
        
      def sort(s: str) -> str:
        if len(s) == 1:
          return s
        
        middle = len(s) // 2
        left = sort(s[:middle])
        right = sort(s[middle:])

        result = ""
        i = 0
        j = 0
        while True:
          if left[i] < right[j]:
            result += left[i]
            i += 1
          elif left[i] > right[j]:
            result += right[j]
            j += 1
          else:
            result += right[j] + left[i]
            j += 1
            i += 1
          if i == len(left):
            result += right[j:]
            break
          if j == len(right):
            result += left[i:]
            break
            
        return result
      
      return sort(s) == sort(t)
