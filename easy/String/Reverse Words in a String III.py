class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

        for ref:
        class Solution:
          def reverseWords(self, s: str) -> str:
            s=list(s)
            start=0
            n=len(s)

            while start<n:
              end=start
              while end<n and s[end]!=' ':
                end+=1
              i,j=start,end-1
              while(i<j):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
              
              start=end+1
            return ''.join(s)      
        """
        indecies = []
        in_word = False
        for i in range(len(s)):
          if s[i] != " " and not in_word:
            indecies.append(i)
            in_word = True
          elif s[i] == " " and in_word:
            indecies.append(i)
            in_word = False
        else:
          if in_word:
            indecies.append(i + 1)

        def reverse(s: str) -> str:
          l = len(s)
          for i in range(l // 2):
            tmp = s[i]
            s = s[:i] + s[l - 1 - i] + s[i+1:]
            s = s[:l - 1 - i] + tmp + s[l - i:]
          return s
        
        length = len(indecies)
        for i in range(0, length, 2):
          s = s[:indecies[i]] + reverse(s[indecies[i]:indecies[i+1]]) + s[indecies[i+1]:]
        return s
