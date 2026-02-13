class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        """
        Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

        Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

        In the American keyboard:

        the first row consists of the characters "qwertyuiop",
        the second row consists of the characters "asdfghjkl", and
        the third row consists of the characters "zxcvbnm".

        for ref:
        class Solution:
            def findWords(self, words: List[str]) -> List[str]:
                l1=set("qwertyuiop")
                l2=set("asdfghjkl")
                l3=set("zxcvbnm")
                op=[]
                for word in words:
                    r=l1 if word[0].lower() in l1 else l2 if word[0].lower() in l2 else l3
                    for i in word.lower():
                        if i not in r:
                            break
                    else:
                        op.append(word)
            
                return op
        class Solution:
            def findWords(self, words: List[str]) -> List[str]:
                r1={'q','w','e','r','t','y','u','i','o','p'}
                r2={'a','s','d','f','g','h','k','j','l'}
                r3={'z','x','c','v','b','n','m'}
                
                s=[]
                for i in range(len(words)):
                    c=words[i].lower()
                    s1=s2=s3=0
                    for j in range(len(c)):
                        if c[j] in r1:
                            s1+=1
                        if c[j] in r2:
                            s2+=1
                        if c[j] in r3:
                            s3+=1
                    if(s1==len(c) or s2==len(c) or s3==len(c)):
                        s.append(words[i])
                return s
        """
        keyboard_list = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
        result = []
        for word in words:
          base_row = keyboard_list[0] if word[0] in keyboard_list[0] else (keyboard_list[1] if word[0] in keyboard_list[1] else keyboard_list[2])
          for i in range(len(word)):
            if word[i] not in base_row:
              break
            elif i == len(word) - 1:
              result.append(word)

        return result
