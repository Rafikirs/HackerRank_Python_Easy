def print_mat(n, m):
    for i in range(1, n, 2):
        pattern = (".|." * i).center(m, "-")
        print(pattern)
    
    print("WELCOME".center(m, "-"))
    
    for i in range(n-2, -1, -2):
        pattern = (".|." * i).center(m, "-")
        print(pattern)

n, m = map(int, input().split())
print_mat(n, m)







