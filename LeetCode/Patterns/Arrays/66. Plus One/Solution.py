from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = 0
        digits = digits[::-1]

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
                i += 1          # Move to the next digit
            else:
                digits.append(carry)
                carry = 0

        return digits[::-1]