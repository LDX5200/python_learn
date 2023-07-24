def print_file_info(file_name:str):
    f = None
    try:
        f = open(file_name,"r",encoding="UTF-8")
        # print(f.read())
    except FileNotFoundError as e:
        print("file not existed")
    else:
        print(f.read())
    finally:
        if f:
            f.close()

def append_to_file(file_name:str,data):
    f =None
    try:
        f = open(file_name,"a",encoding="UTF-8")
    except FileExistsError as e:
        print("file not existed")
    else:
        f.write(data)
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    # 在windows系统当中读取文件路径可以使用\，
    # 但是在python字符串中\有转义的含义，如\t可代表TAB，\n代表换行，
    # 所以我们需要采取一些方式使得\不被解读为转义字符。
    # 在路径字符串前面加r，即保持字符原始值的意思。
    print_file_info(r'C:\Users\13581\Desktop\learn\pythonlearn\2023\day9\my_utils\test.txt')
    