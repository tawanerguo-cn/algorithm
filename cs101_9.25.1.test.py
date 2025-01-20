def process_input(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        while True:
            try:
                line = infile.readline().strip()
                if not line:
                    break  # 文件结束
                o = list(map(int, line.split()))
                if o.count(0) != len(o):
                    n = o[5] + o[4]
                    o[0] = max(0, o[0] - 11 * o[4])
                    n += o[3]
                    if 5 * o[3] >= o[1]:
                        o[1] = 0
                        o[0] = max(0, o[0] - 20 * o[3] + 4 * o[1])
                    else:
                        o[1] -= 5 * o[3]
                    n += o[2] // 4 + o[1] // 9 + o[0] // 36
                    o[2] = o[2] % 4
                    o[1] = o[1] % 9
                    o[0] = o[0] % 36
                    if o[2] == 0:
                        n += -(-((4 * o[1] + o[0]) // 36) // 1)
                    else:
                        n += 1
                        o[1] = max(0, o[1] - 7 - 2 * o[2])
                        o[0] = max(0, o[1] - 8 - o[2])
                        n += -(-((4 * o[1] + o[0]) // 36) // 1)
                    outfile.write(f"{int(n)}\n")
                else:
                    outfile.write("0\n")
            except Exception as e:
                print(f"An error occurred: {e}")
                break
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    differences = []
    for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
        if int(line1.strip()) != int(line2.strip()):
            differences.append(f"Line {i}: '{line1.strip()}' != '{line2.strip()}'")

    return differences
# 调用函数
input_file = '1017.in'  # 输入文件名
output_file = '1017_output.txt'  # 输出文件名
process_input(input_file, output_file)
# 使用文件名调用函数
file1 = '1017_output.txt'  # 你的输出文件
file2 = '1017.out'  # 你需要比对的文件
differences = compare_files(file1, file2)

if differences:
    for diff in differences:
        print(diff)
else:
    print("No differences found.")
