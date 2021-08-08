max_L = 0
for i in range(int(input())):
    for j in range(int(input())):
        school, L = input().split()
        if int(L) > max_L:
            print('max L',max_L)
            print('L',L)
            max_L = int(L)
            max_school = school
            print('max L', max_L)
            print('L', L)
    print(max_school)