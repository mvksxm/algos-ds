
# TC -> O(7) -> O(1)
# SC -> O(7) -> O(1)

class Solution:

    # Not Standard Approach
    def intToRoman(self, num: int) -> str:
        mp = {
            1000:  "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I"
        }

        roman_num = []

        next_num = num
        curr_power_ten = 1000
        for divisor, symbol in mp.items():

            amount = next_num // divisor
            power_ten_amount = next_num // curr_power_ten

            if power_ten_amount == 4:
                roman_num.append(mp[curr_power_ten])
                roman_num.append(mp[curr_power_ten * 5])
                next_num = next_num - (4 * curr_power_ten)
            elif power_ten_amount == 9:
                roman_num.append(mp[curr_power_ten])
                roman_num.append(mp[curr_power_ten * 10])
                next_num = next_num - (9 * curr_power_ten)
            elif amount != 0:
                roman_num.append(mp[divisor] * amount)
                next_num = next_num - (amount * divisor)

            if next_num == 0: break

            if next_num // curr_power_ten == 0:
                curr_power_ten //= 10

        return "".join(roman_num)