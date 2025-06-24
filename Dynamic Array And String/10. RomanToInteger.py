'''
I       =      1
V       =     5
X       =     10
L       =      50
C       =      100
D       =      500
M       =      1000

MD M+D = 1500
13 = XIIV
'''
from typing import List
print("input Roman Symbol:")
s = input()
class Solution:
    def romanToInteger(self, s: str) -> int:
        dictionary_roman = {'I': 1, 'V':5, 'X' :10, 'L': 50, 'C': 100, 'D':500, 'M': 1000 }
        total = 0
        for i in range(len(s)):
            value = dictionary_roman[s[i]]
            if i + 1 < len(s) and dictionary_roman[s[i]] < dictionary_roman[s[i+1]]:
                total -= value
            else:
                total += value
        return total
solution = Solution()
print(solution.romanToInteger(s))
