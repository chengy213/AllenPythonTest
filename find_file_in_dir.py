import os
def search_file(path,key):
    x_path=path
    print(f"search path:{x_path}")
    if not os.path.exists(x_path):
        print("error: not exist!!")
        return
    if os.path.isfile(x_path):
        if x_path.find(key) != -1:
            print(f"match path:{x_path}")
        return
    if os.path.isdir(x_path):
        dir_list=os.listdir(x_path)
        for x in dir_list:
            full_path = os.path.join(x_path, x)
            if x.find(key)!=-1:
                print(f"match path2:{full_path}")
            if os.path.isdir(full_path):
                search_file(full_path,key)

search_file("/Users/allen/zoom", "jpg")