import math


# test.assert_equals(solution(89), 'LXXXIX', "solution(89),'LXXXIX'")
#    test.assert_equals(solution(91),'XCI', "solution(91),'XCI'")
# test.assert_equals(solution(14),'XIV', "solution(14),'XIV")
#   test.assert_equals(solution(21),'XXI', "solution(21),'XXI'")
#    test.assert_equals(solution(1000), 'M', 'solution(1000), M')
#    test.assert_equals(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
#     test.assert_equals(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
#     test.assert_equals(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")"""


def convert(roman_string):
    print(roman_string)
    # if count X>=5 : L
    if 'XXXXX' in roman_string:
        roman_string = roman_string.replace('XXXXX', 'L')
        if 'XXXX' in roman_string:
            roman_string = roman_string.replace('XXXX', 'C')
            roman_string = roman_string.replace('L', 'X')
    # if count X > 3 and < 5
    if 'XXXX' in roman_string:
        # print("HERE")
        roman_string = roman_string.replace('XXXX', 'XL')
    # if count C>= 5 : D
    if 'CCCCC' in roman_string:
        print("HERE")
        roman_string = roman_string.replace('CCCCC', 'D')
        if 'CCCC' in roman_string:
            roman_string = roman_string.replace('CCCC', 'M')
            roman_string = roman_string.replace('D', 'C')
    # if count C > 3 and < 5
    if 'CCCC' in roman_string:
        roman_string = roman_string.replace('CCCC', 'CD')

    return roman_string


def split_digits(num_string):
    digit_list = []
    for digit in num_string:
        digit_list.append(digit)
    return digit_list


def find_number_digits(num_string):
    number_of_digits = len(num_string)
    return number_of_digits


def find_number_digits_n(num):
    return int(math.log10(num)) + 1


def solution(n):
    """
    Modern Roman numerals are written by expressing each digit separately
    starting with the left most digit and skipping any digit with a value of zero.
    In Roman numerals 1990 is rendered:
    1000=M, 900=CM : "100 less than 1000", 90=XC : "10 less than 100"; resulting in MCMXC.
    2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in
    descending order: MDCLXVI.

    Remember that there can't be more than 3 identical symbols in a row.
    """
    numerals = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 50: 'L',
                100: 'C', 500: 'D', 1000: 'M'}
    n = str(n)
    number = ""
    digit_list = split_digits(n)

    count = len(digit_list) - 1
    for item in digit_list:
        if int(item) in numerals.keys():
            if count > 0:
                if count == 1:
                    number += 'X' * int(item)

                    count = count - 1
                elif count == 2:
                    number += 'C' * int(item)
                    count = count - 1

                    pass
                else:
                    number += 'M' * int(item)
                    count = count - 1

                    pass

            else:
                num = int(item)
                if num in numerals.keys():
                    number += numerals[num]
                    count = count - 1
                else:

                    count = count - 1
        else:
            count = count - 1

    number = convert(number)
    return number


if __name__ == "__main__":
    print(solution(1989))
