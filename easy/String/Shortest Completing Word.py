class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        """
        Given a string licensePlate and an array of strings words, find the shortest completing word in words.

        A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

        For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

        Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

        for ref:
        class Solution {
            private static final int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103}; 
            
            public String shortestCompletingWord(String licensePlate, String[] words) {
                long charProduct = getCharProduct(licensePlate.toLowerCase());
                String shortest = "aaaaaaaaaaaaaaaaaaaa"; // 16 a's
                for(String word : words)
                    if (word.length() < shortest.length() && getCharProduct(word) % charProduct == 0)
                            shortest = word;
                return shortest;
            }
            
            private long getCharProduct(String plate) {
                long product = 1L;
                for(char c : plate.toCharArray()) {
                    int index = c - 'a';
                    if (0 <= index && index <= 25) 
                        product *= primes[index];
                }
                return product;
            }
        }

        class Solution:
            def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
                res_words = []
                letters = [char.lower() for char in licensePlate if char.isalpha()]

                for word in words:
                    word_letters = list(word)
                    is_valid = True

                    for letter in letters:
                        if letter in word_letters:
                            word_letters.remove(letter)
                        else:
                            is_valid = False
                            break

                    if is_valid:
                        res_words.append(word)

                res_words.sort(key=len)

                return res_words[0]

        class Solution:
            def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
                letters = [i.lower() for i in licensePlate if i.isalpha()]
                c = Counter(letters) # hash for counting all letters
                for i in sorted(words, key=lambda x: len(x)):
                    temp = Counter(i)
                    flag = True
                    for j in c:
                        if temp[j] < c[j]:
                          flag = False
                    if flag:
                        return i 
        """
        def to_lower(char: str) -> str:
            if 65 <= ord(char) <= 90:
              char = chr(ord(char) + 32)
            return char

        l_hash = {}
        for l in licensePlate:
          if 'A' <= l <= 'Z' or 'a' <= l <= 'z':
            l_hash[to_lower(l)] = 1 + l_hash.get(to_lower(l), 0)

        result = ' ' * 16
        for word in words:
          w_hash = {}
          for w in word:
            w_hash[w] = 1 + w_hash.get(w, 0)

          for char in l_hash:
            count = w_hash.get(char, 0)
            if not count or count < l_hash[char]:
              break
          else:
            if len(word) < len(result):
              result = word

        return result