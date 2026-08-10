class Solution:
    def multiply(self, num1: str, num2: str) -> str:


        if len(num1) >= len(num2):
            to_multiply = num1[::-1]
            multiplier = num2[::-1]
        else:
            to_multiply = num2[::-1]
            multiplier = num1[::-1]

        nums_to_add = []
        num_to_add = ""

        # Multiplication
        for i in range(len(multiplier)):

            remainder = 0
            num_to_add += "0" * i

            for dig in to_multiply:
                mult_res = int(dig) * int(multiplier[i]) + remainder
                num_to_add += str(mult_res % 10)
                remainder = mult_res // 10

            if remainder != 0:
                num_to_add += str(remainder)

            nums_to_add.append(num_to_add)
            num_to_add = ""


        # Addition
        for i in range(1, len(nums_to_add)):

            curr = nums_to_add[i]
            prev = nums_to_add[i-1]

            curr_p = 0
            prev_p = 0

            remainder = 0
            summed_num = ""

            while curr_p < len(curr) or prev_p < len(prev):

                prev_digit = 0
                curr_digit = 0

                if curr_p < len(curr): curr_digit = int(curr[curr_p])
                if prev_p < len(prev): prev_digit = int(prev[prev_p])

                sm = curr_digit + prev_digit + remainder
                summed_num += str(sm % 10)
                remainder = sm // 10
                curr_p += 1
                prev_p += 1

            if remainder != 0: summed_num += str(remainder)

            nums_to_add[i] = summed_num

        res = nums_to_add[-1][::-1]
        if res[0] == "0": return "0"
        return res

if __name__ == "__main__":
    sln = Solution()
    print(sln.multiply("408","987654321"))
