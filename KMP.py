# Knuth-Morris-Pratt algorithm
# pattern searching

t = "kimmil"  # pattern

p = [0]*len(t)             # dictionary of repetitions
j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        p[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

print(p)

a = "kimilil kimmilal"   # string
m = len(t)
n = len(a)

i = 0
j = 0
while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("Found")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1

if i == n:
    print('Not found')