__all__ = ['test1']
#__all__变量是一个列表，里面的函数为from import * 时候可以使用的
def test1(a,b):
    print("test1")
    print(a + b)
    return a + b

def test2(a,b):
    print("test2")
    print(a - b)
    return a - b

