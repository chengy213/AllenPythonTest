from functools import reduce


def to_format_name(x:str):
   y=str.lower(x)
   if len(y) > 0:
       return y[0].upper()+y[1:]
   return y

print(list(map(to_format_name, ["allen", "FRANK", "anDY"])))

def allen_sum(l:list):
    return reduce(lambda x,y:x+y, l)

print(f"allen_sum, {allen_sum([1,2,3,4,5])}")

def is_palindrome(n):
    i=0
    s=str(n)
    time=len(s)//2
    flag=True
    while i<time:
        if s[i]!=s[-1-i]:
            flag=False
            break
        i+=1
    return flag

huiwen_test_list=[12345,123421,123321,4567654,"allen","abccba","abcDcba"]

print(list(filter(is_palindrome, huiwen_test_list)))
print(list(filter(is_palindrome, range(1000))))

def sort_with_name(l):
    m={}
    for i,v in enumerate(l):
        name=v[0]
        m[name]=i
    new_l=sorted(m.keys())
    r=[]
    for x in new_l:
        source=l[m.get(x)]
        r.append(source)
    return r

print(sort_with_name([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]))

def sort_with_score(l):
    m={}
    for i,v in enumerate(l):
        score=v[1]
        m[score]=i
    new_l=sorted(m.keys(), reverse=True)
    r=[]
    for x in new_l:
        source=l[m.get(x)]
        r.append(source)
    return r

print(sort_with_score([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]))

def sorted_inner_tuple(lst, key_function=None, reverse=False):
    if key_function is None:
        key_function=lambda x:x[0]

    sorted(lst, key=key_function, reverse=reverse)

da=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(f"sorted_with_name={sorted(da,key=lambda x:x[0])}")
print(f"sorted_with_score={sorted(da,key=lambda x:x[1],reverse=True)}")