101# Get input from the user
print("Enter target:")
x = int(input())
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Pseudocode:
        # 1. Handle special cases that are not palindromes.
        #    - If x is a negative number, it cannot be a palindrome (e.g., -121).
        #    - If x is not 0 and ends with 0, it cannot be a palindrome (e.g., 10, 120).
        #      The number 0 is still considered a palindrome.
        if x < 0 or (x!= 0 and x % 10 ==0):
            return False
        
        # 2. Reverse the second half of the number.
        half = 0
        #    Loop until the reversed number (half) is greater than or equal to the remaining part of the original number (x).
        while x > half:
            #    Get the last digit of x and add it to `half`.
            half = (half * 10) + (x % 10)
            #    Remove the last digit from x.
            x = x // 10
            
        # 3. Compare the two halves to check for symmetry.
        #    - If the original number has an even number of digits (e.g., 1221), the loop stops when x=12, half=12. We compare x == half.
        #    - If the original number has an odd number of digits (e.g., 12321), the loop stops when x=12, half=123.
        #      The middle digit (3) does not affect the palindrome property, so we compare x with half//10 (12 == 123//10).
        return x == half or x == half // 10

# Create an instance of the Solution class
solution = Solution()
# Call the isPalindrome method and print the result
if solution.isPalindrome(x):
    print('True')
else:
    print('False')
