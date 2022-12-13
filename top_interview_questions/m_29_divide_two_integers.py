# https://leetcode.com/problems/divide-two-integers/description/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 1
        answer = 0

        negative_sign = ((dividend < 0) != (divisor < 0))

        dividend = remaining_dividend = abs(dividend)
        divisor = updated_divisor = abs(divisor)

        while remaining_dividend >= divisor:
            remaining_dividend -= updated_divisor

            answer += quotient
            quotient += quotient

            updated_divisor += updated_divisor

            if remaining_dividend < updated_divisor:
                updated_divisor = divisor
                quotient = 1

        if negative_sign:
            return max(-answer, -2**31)
        else:
            return min(answer, 2**31-1)
