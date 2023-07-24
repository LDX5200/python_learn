#:指定类型 ->指定返回类型
def str_reverse(s:str) -> str:
    #反转字符串
    print(s[::-1])
    return s[::-1]

def substr(s:str,x,y) -> str:
    #字符串切片
    print(s[x:y:1])
    return s[x:y:1]