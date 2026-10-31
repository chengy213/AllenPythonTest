import math


def quadratic(a,b,c):
    if not isinstance(a, (int,)):
        return 0,0
    s=math.sqrt(b*b-4*a*c)
    r1=(-b + s)/(2*a)
    r2=(-b-s)/(2*a)
    return r1, r2

print(quadratic(1,2,1))
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
print(quadratic("abc",3,-4))

def pow(x:int, n:int):
    if not isinstance(n, (int,)):
        return 0
    r=1
    while n > 0:
        r=r*x
        n = n-1
    return r

print(pow(2, 1))
print(pow(2, 2))
print(pow(3, 3))
print(pow(5, 3))

def append_end_wrong(L=[]):
    L.append("end_wrong")
    return L

al=[1,2,3]
# [1, 2, 3, "end_wrong"]
print(append_end_wrong(al))
# [1, 2, 3, "end_wrong"] al already changed
print(al)
print(append_end_wrong(al))

print("default:", append_end_wrong())
print("default2:", append_end_wrong())

al2=[1,2,3]
def append_end(L=None):
    if L is None: #must new again
        L = []
    L.append("end")
    return L

print(append_end(al2))
print(append_end(al2))

print("default3:", append_end())
print("default4:", append_end())

def mul_cal(*args):
    r=1
    for i in args:
        r = r * i
    return r

print(mul_cal(5))
print(mul_cal(5,6))
print(mul_cal(5,6,7))
print(mul_cal(5,6,7,9))

def cal_pingfang(*args):
    r=0
    for i in args:
        r = r + i * i
    return r

print(cal_pingfang(1,2))
print(cal_pingfang(1,2,3,4))

def digui_add(n:int):
    return digui_do_add(n,0)

def digui_do_add(num:int,r:int):
    if num<=0:
        return r
    return digui_do_add(num-1,num+r)

print(digui_add(3))
print(digui_add(4))

def move_hannuota(n,a,b,c):
    if n==1:
        print(f"{a}->{c}")
        return
    #将上面的n-1个盘子从a搬到b(借助c)
    move_hannuota(n-1, a, c, b)
    #将最大的盘子从a搬到c
    print(f"{a}->{c}")
    #再把n-1个盘子(视为一个整体)从b搬到c（借助a）
    move_hannuota(n-1, b, a, c)

move_hannuota(3, 'A', 'B', 'C')