l=["allen", "frank", "andy", "jamison"]
print(l[0] + "," + l[-1])
l.append("eden")
print(l[-2])
l.insert(2, "adam")
print(l)

single_tuple=(1,)
print(single_tuple[0])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

s=input("year:")
year=int(s)
if year < 2000:
    print("your birth day is %s and it's a old one" % year)
else:
    print("your birth day is %s and it's a yougher one" % year)

match year:
    case x if x < 2000:
        print("[match] your birth day is %s and it's a old one" % year)
    case 2000:
        print("[match] your birth day is %s and it's just fine" % year)
    case _:
        print("[match] your birth day is %s and it's a yougher one" % year)

for x in l:
    print("hello, %s" % x)