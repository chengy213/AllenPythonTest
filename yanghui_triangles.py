def yanghui_triangles(n):
    i=0
    r=[]
    while i<n:
        #第一行
        if i == 0:
            r.append([1])
        #第二行
        elif i == 1:
            r.append([1, 1])
        else:
            num=i+1
            tr=[1,1]
            index=1
            #生成的数量是偶素个
            gen=num-2
            half_gen=gen//2
            while(half_gen>0):
                tr.insert(index, r[i-1][index-1]+r[i-1][index])
                tr.insert(-1-index, r[i-1][index-1]+r[i-1][index])
                index+=1
                half_gen-=1
            last_one_gen=gen%2
            if last_one_gen>0:
                #奇数个时只增加一个，不做对称新增
                tr.insert(index, r[i-1][index-1]+r[i-1][index])
            r.append(tr)
        i+=1
    return r

triangles=yanghui_triangles(7)
print(f"yanghui_triangles, {triangles}")