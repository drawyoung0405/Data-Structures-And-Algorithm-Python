class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Initialize left and right pointers.
        l,r = 0, len(s)-1
        
        # 2. Loop until the pointers meet or cross.
        while l < r:
            # 3. Move the left pointer forward if it's not an alphanumeric character.
            while l < r and not self.alphaNumeric(s[l]):
                l += 1
            # 4. Move the right pointer backward if it's not an alphanumeric character.
            while r > l and not self.alphaNumeric(s[r]):
                r -= 1
            
            # 5. Compare the characters (case-insensitive). If they don't match, it's not a palindrome.
            if s[l].lower() != s[r].lower():
                return False
            
            # 6. Move pointers inward for the next comparison.
            l, r = l + 1, r - 1
        # 7. If the loop finishes, the string is a palindrome.
        return True
                        
    def alphaNumeric(self, c):
        # Helper function to determine if a character is alphanumeric.
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
