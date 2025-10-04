class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # Remove leading/trailing spaces
        num_seen = dot_seen = e_seen = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                num_seen = True
            elif char in ['+', '-']:
                # Sign can only appear at the start or just after 'e'/'E'
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif char == '.':
                # Dot can't appear after e or appear twice
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif char in ['e', 'E']:
                # Exponent must appear only once and only after a number
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False  # Must have a number after 'e'
            else:
                return False
        
        return num_seen
