max_L = 0
for i in range(int(input())):
    for j in range(int(input())):
        school, L = input().split()
        if int(L) > max_L:
            max_L = int(L)
            max_school = school
    print(max_school)