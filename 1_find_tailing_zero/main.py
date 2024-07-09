"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

class Solution:

    def find_tailing_zeroes(self, number: int) -> int:
        if number < 0:
            return 'number cannot be negative'
        elif number < 5:
            return 0

        count = 0
        i = 5
        while number // i > 0:
            count += number // i
            i *= 5
        return count


solution = Solution()
input1 = 7
input2 = -10  

print(f'input = {input1}, output = {solution.find_tailing_zeroes(input1)}')
print(f'input = {input2}, output = {solution.find_tailing_zeroes(input2)}')





