def test(a,b):
    print("this is a add mod")
    return a + b

#main 变量
#当运行的时候 __name__就会变为main，也就是说会为True
if __name__ == '__main__':
    test(1,2)