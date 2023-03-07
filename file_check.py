import sys

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except:
    print('请输入两个文本文件')
    sys.exit()

# with open(f"input.txt", "r+") as f:
with open(f"{input_file}", "r+") as f:
    line_changed = ''
    for i in range(0, 6):
        line = f.readline()
        for j in line:
            try:
                int(j)
                line_changed = line_changed + str(j)
            except ValueError:
                pass
    print(line_changed)
    count = 0
    new_file = ''
    for k in line_changed:
        count += 1
        new_file = new_file + str(k)
        if count % 9 == 0:
            new_file = new_file + '\n'
        elif count % 3 == 0:
            new_file = new_file + '-'
    print(new_file)

# with open("output.txt", "w+") as g:
with open(f"{output_file}", "w+") as g:
    g.write(new_file)
