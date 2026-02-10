class Solution:
    def countSegments(self, s: str) -> int:
        """
        Given a string s, return the number of segments in the string.

        A segment is defined to be a contiguous sequence of non-space characters.
        
        for ref:
        class Solution:
            def countSegments(self, s: str) -> int:
                # Initialize a variable to keep track of the count of segments.
                count = 0
                # Initialize a flag to check if we are inside a segment.
                inside_segment = False
                
                # Iterate through each character in the string.
                for char in s:
                    # If the current character is not a space and we are not inside a segment, start a new segment.
                    if char != ' ' and not inside_segment:
                        count += 1
                        inside_segment = True
                    # If the current character is a space and we are inside a segment, mark the end of the segment.
                    elif char == ' ' and inside_segment:
                        inside_segment = False
                
                return count
        """
        if not s:
          return 0
        
        r = 1 if s[0] != " " else 0
        for i in range(r, len(s) - 1):
          if s[i] == " " and s[i + 1] != " ":
            r += 1

        return r
