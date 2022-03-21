n, = map(int, input("Enter size of arrays: ").split())
mas = list(map(int, input("Enter array elements: ").split()))
count = 0
for run in range(n-1):
    for i in range(n-1-run):    # check for every run
        if mas[i] > mas[i+1]:
            mas[i],mas[i+1] = mas[i+1],mas[i]
            count += 1
    print(*mas)

print(count)




