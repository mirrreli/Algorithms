# Boyer-Moore-Horspool algorithm
# pattern search

t = "bases"

S = set()  # unique symbols in pattern
M = len(t) # number of symbols
d = {}     # dictionary of bias

for i in range(M-2, -1,-1):
    if t[i] not in S:
        d[t[i]] = M-i-1
        S.add(t[i])

if t[M-1] not in S:
    d[t[M-1]] = M

d['*'] = M

print(d)


a = "amount of basespace "
N = len(a)

if N >= M:
    i = M-1

    while i < N:
        k = 0
        for j in range(M-1, -1, -1):
            if a[i-k] != t[j]:
                if j == M-1:
                    off = d[a[i]] if d.get(a[i], False) else d['*']     # if last simbol of pattern is not equal
                else:
                    off = d[t[j]]   # if is not equal any other symbol

                i += off
                break

            k += 1

        if j == 0:
            print(f"pattern found at  {i-k+1}")
            break
else:
    print("not found")