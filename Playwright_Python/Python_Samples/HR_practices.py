def formula(x, y, z, n):
    x_ls = [x for x in range(x+1)]
    y_ls = [y for y in range(y+1)]
    z_ls = [z for z in range(z+1)]
    list_all = [[x, y, z] for x in x_ls for y in y_ls for z in z_ls]
    list_only = [x for x in list_all if sum(x) != n]
    print(list_only)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    formula(x, y, z, n)
