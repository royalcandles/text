import sys


def binary_addition(num1, num2):
    # 补全二进制数长度
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        bit_sum = int(num1[i]) + int(num2[i]) + carry
        carry = bit_sum // 2
        result = str(bit_sum % 2) + result

    if carry:
        result = '1' + result

    return result


if __name__ == '__main__':
    nums = sys.argv[1:]
    result = '0'

    for num in nums:
        result = binary_addition(result, num)

    print(result)
