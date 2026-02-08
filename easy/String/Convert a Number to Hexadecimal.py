class Solution:
    def toHex(self, num: int) -> str:
        """
        Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

        All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

        for ref:
        # O(1) O(1)
        class Solution:
            def toHex(self, num: int) -> str:
                if num == 0:
                    return "0"
                if num < 0:
                    num += 2 ** 32
                h = "0123456789abcdef"
                res = ""
                while num:
                    res = h[num & 15] + res
                    num >>= 4
                return res

        # # O(log n) O(log n)
        # class Solution:
        #     def toHex(self, num: int) -> str:
        #         if num == 0:
        #             return "0"
        #         if num < 0:
        #             num = num + 2 ** 32
        #         h = "0123456789abcdef"
        #         res = ""
        #         while num:
        #             res = h[num % 16] + res
        #             num //= 16
        #         return res
        """
        hex_special_chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        if num < 0:
          num += 2 ** 32

        result = ""
        while num:
          result = hex_special_chars[num % 16] + result
          num //= 16

        if not result and not num:
          result = "0"
        
        return result
