def allen_prime(max:int):
    l=list(range(3,max))
    r=[2]
    for x in l:
        flag=False
        for y in r:
            if x%y==0:
                # l.pop(x)
                flag=True
                break
        if not flag:
            r.append(x)
    return r

print(allen_prime(100))


