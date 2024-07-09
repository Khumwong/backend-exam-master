"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0 or number > 10000000:
            return "number can not less than 0"
    
    # Thai number words
        #thai_digits = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
        thai_teens = ['', 'เอ็ด', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
        thai_tens = ['', 'สิบ', 'ยี่สิบ', 'สามสิบ', 'สี่สิบ', 'ห้าสิบ', 'หกสิบ', 'เจ็ดสิบ', 'แปดสิบ', 'เก้าสิบ']
        thai_hundreds = ['', 'หนึ่งร้อย', 'สองร้อย', 'สามร้อย', 'สี่ร้อย', 'ห้าร้อย', 'หกร้อย', 'เจ็ดร้อย', 'แปดร้อย', 'เก้าร้อย']
        thai_thousands = ['', 'หนึ่งพัน', 'สองพัน', 'สามพัน', 'สี่พัน', 'ห้าพัน', 'หกพัน', 'เจ็ดพัน', 'แปดพัน', 'เก้าพัน']
        thai_ten_thousands = ['', 'หนึ่งหมื่น', 'สองหมื่น', 'สามหมื่น', 'สี่หมื่น', 'ห้าหมื่น', 'หกหมื่น', 'เจ็ดหมื่น', 'แปดหมื่น', 'เก้าหมื่น']
        thai_ten_hundreds_thousands = ['', 'หนึ่งแสน', 'สองแสน', 'สามแสน', 'สี่แสน', 'ห้าแสน', 'หกแสน', 'เจ็ดแสน', 'แปดแสน', 'เก้าแสน']
        thai_millions = ['', 'หนึ่งล้าน', 'สองล้าน', 'สามล้าน', 'สี่ล้าน', 'ห้าล้าน', 'หกล้าน', 'เจ็ดล้าน', 'แปดล้าน', 'เก้าล้าน']
        thai_ten_millions = ['', 'สิบล้าน']

        if number == 0:
            return 'ศูนย์'
        if number == 1:
            return 'หนึ่ง'

        result = []
        # Process ten millions
        if number >= 10000000:
            ten_millions = number // 10000000
            result.append(thai_ten_millions[ten_millions])
            number %= 10000000

        # Process millions
        if number >= 1000000:
            millions = number // 1000000
            result.append(thai_millions[millions])
            number %= 1000000

        # Process ten hundreds thousands
        if number >= 100000:
            ten_hundreds_thousands = number // 100000
            result.append(thai_ten_hundreds_thousands[ten_hundreds_thousands])
            number %= 100000

        # Process ten thousands
        if number >= 10000:
            ten_thousands = number // 10000
            result.append(thai_ten_thousands[ten_thousands])
            number %= 10000
                
        # Process thousands
        if number >= 1000:
            thousands = number // 1000
            result.append(thai_thousands[thousands])
            number %= 1000

        # Process hundreds
        if number >= 100:
            hundreds = number // 100
            result.append(thai_hundreds[hundreds])
            number %= 100

        # Process tens and ones
        if number >= 10:
            tens = number // 10
            result.append(thai_tens[tens])
            number %= 10

        if number > 0:
            result.append(thai_teens[number])

        return ''.join(result)

solution = Solution()
input1 = 101
input2 = -1  

print(f'input = {input1}, output = {solution.number_to_thai(input1)}')
print(f'input = {input2}, output = {solution.number_to_thai(input2)}')

