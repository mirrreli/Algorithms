
s = input()
stack = []  # use LIFO
is_good = True
for i in s:
    if i in'[{(':
        stack.append(i)
    elif i in ']})':
        if not stack:       # if stack is empty
            is_good = False
            break
        open_bracket = stack.pop()

        if open_bracket == '(' and i == ')':
            continue
        if open_bracket == '[' and i == ']':
            continue
        if open_bracket == '{' and i == '}':
            continue
        is_good = False
        break

if is_good and len(stack) == 0:
    print('YES')
else:
    print('NO')
