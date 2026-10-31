def self_trim(str):
    #找第一个非空格的字母
    l=list(str)
    i=0
    while i< len(l):
        if l[i] != ' ':
            break
        i +=1
    j=len(l)-1
    while j > 0:
        if l[j] != ' ':
            break
        j -= 1
    return ''.join(l[i:j+1])

print(self_trim("allen1"))
print(self_trim(" allen2"))
print(self_trim(" allen3"))
print(self_trim(" allen4"))
print(self_trim(" allen5  "))

def find_min_max(l:list):
    min = l[0]
    max = min
    for x in l:
        if x < min:
            min = x
        if x > max:
            max = x
    return (min, max)

print(find_min_max([7, 1, 3, 9, 5]))

for i,x in enumerate([7, 1, 3, 9, 5]):
    print(i,x)

def self_to_lowcase(l:list):
    return [s.lower() for s in l if isinstance(s, str)]

print(self_to_lowcase(["AllEn", "HEllo", 18, None]))

def fushu(l:list):
    return [-x+1 for x in l if x%2 ==0]

print(fushu(list(range(0,10))))

a1,a2,a3=1,2,3
a1,a2=a2,a1+a2
# 2,3
#这说明用的是之前的值参与计算，不是用a1=a2新赋值的value
print(f"{a1},{a2}")

def fib(max):
    n,a,b=0,0,1
    r=[]
    while n<max:
        print(f"{b},")
        r.append(b)
        t=a+b
        a=b
        b=t
        n+=1
    return r
print(fib(6))

def fib_gen(max):
    n,a,b=0,0,1
    r=[]
    while n<max:
        yield b
        r.append(b)
        t=a+b
        a=b
        b=t
        n+=1
    return "done"

fg=fib_gen(10)
print(next(fg))
print(next(fg))
print(next(fg))
print(next(fg))



