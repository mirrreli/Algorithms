# two pointer method

n,m = map(int, input("Enter two sizes of arrays: ").split())
a=list(map(int, input("Enter first array elements: ").split()))
b=list(map(int, input("Enter second array elements: ").split()))


i = j = 0
c = []

while i<n and j<m:
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1

while i<n:
    c.append(a[i])      # if we have other elements in array a
    i += 1
while j<m:
    c.append(b[j])      # if we have other elements in array b
    j += 1

print(*c)

