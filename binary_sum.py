import sys
# put_in = input()
# num_list = put_in.split(' ')
num_list = sys.argv[1:]
dec_sum = 0
for i in num_list:
    try:
        dec_sum = dec_sum + int(i, 2)
    except ValueError:
        print('请检查输入格式是否为二进制，个数字间用空格分隔')
        break
bin_sum = bin(dec_sum)
print(str(bin_sum)[2:])
