#综合案例 ATM
money = int(5000000)
name = str(input())

def check():
    print(f'您当前的余额是{money}')

def save():
    global money
    print("请输入你要存多少钱")
    inmoney = int(input())
    money = money + inmoney
    print("存款成功")
    print(f"您的余额{money}元")

def withdraw():
    global money
    print("请输入你取存多少钱")
    outmoney = int(input())
    money = money - outmoney
    print("取款成功")
    print(f"您的余额{money}元")

def menu():
    print('请输入您的名字')
    name = input()
    while(1):
        print("请输入您需要的功能")
        print("1 --- 查询余额")
        print("2 --- 存款")
        print("3 --- 取款")
        print("其他 --- 退出")
        num = int(input())
        if num == 1:
            check()
            continue
        elif num == 2:
            save()
            continue
        elif num == 3:
            withdraw()
            continue
        else:
            break

menu()