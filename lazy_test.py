def lazy_sum(*args):
    def sum():
        r = 0
        for x in args:
            r+=x
        return r
    return sum

print(lazy_sum(1,2,3,4)())

def counter():
    def do_counter(max):
        n=1
        while n<=max:
            yield n
            n+=1
    return do_counter(100)

my_count=counter()
print(my_count)
print(next(my_count))
print(next(my_count))

odd_list=list(filter(lambda x: x%2>0, range(1,20)))
print(odd_list)