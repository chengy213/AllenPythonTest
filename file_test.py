def allen_read_file(path:str):
    with open(path,'r') as f:
        print(f.readline(10))

allen_read_file("/Users/allen/.zshrc")