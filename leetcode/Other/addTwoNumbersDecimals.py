
# Overall TC: O(n) + O(n) = O(n); where n is a bigger number between the two
# Overall SC: O(n) + O(n) = O(n); where n is a bigger number between the two

def add_zeroes(num_1: str, num_2: str, is_decimal: bool):

    # TC: O(n-m+m) -> O(n); where n is a bigger number
    # SC: O(n); where n is a bigger number

    zeroes_amount = abs(len(num_1) - len(num_2))

    if is_decimal and len(num_1) > len(num_2):
        num_2 += "0" * zeroes_amount
    elif is_decimal and len(num_2) > len(num_1):
        num_1 += "0" * zeroes_amount
    elif len(num_1) > len(num_2):
        num_2 = "0" * zeroes_amount + num_2
    elif len(num_2) > len(num_1):
        num_1 = "0" * zeroes_amount + num_1

    return num_1, num_2


def perform_addition(num_1: str, num_2: str, overload: int = 0):
    result_num = ""
    for i in range(len(num_1)-1, -1, -1):

        digit_1 = int(num_1[i])
        digit_2 = int(num_2[i])
        digit_sum = digit_1 + digit_2 + overload

        result_num = str(digit_sum % 10) + result_num
        overload = digit_sum // 10

    return result_num, overload

def add_two_numbers(num_1: str, num_2: str):

    num1_split = num_1.split(".")
    num2_split = num_2.split(".")

    num_1_right, num_2_right = add_zeroes(num1_split[1], num2_split[1], True)
    num_1_left, num_2_left = add_zeroes(num1_split[0], num2_split[0], False)

    decimal_sum, dec_overload = perform_addition(num_1_right, num_2_right)
    digit_sum, digit_overload = perform_addition(num_1_left, num_2_left, dec_overload)

    overload_str = str(digit_overload) if digit_overload > 0 else ""
    return overload_str + digit_sum + "." + decimal_sum


if __name__ == "__main__":


    tests = [
        ["231.6","124.6"],
        ["123456789.987", "987654321.123"],
        ["999999999.999", "0.001"],
        ["1.0", "999.999"],
        ["0.0001", "1000.0"],
        ["1.23", "4.5"],
        ["10.5", "2.345"],
        ["0.001", "0.009"]
    ]


    def is_correct(n1, n2):
        print("==================")
        print(add_two_numbers(n1, n2))
        print(float(n1) + float(n2))
        print("==================")
        print(float(add_two_numbers(n1, n2)) == float(n1) + float(n2))

    for test in tests:
        is_correct(*test)
