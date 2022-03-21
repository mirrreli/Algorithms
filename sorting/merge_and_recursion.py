def merge_two_lists(a,b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1  # take next
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c+=a[i:]    # if we have other elements in array a
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s)//2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_lists(left,right)


mas = list(map(int, input("Enter array elements: ").split()))

print(*merge_sort(mas))