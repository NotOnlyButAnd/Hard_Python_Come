# --------- TASK 1 --------

print("Input list\n")
l = list(map(int, input().split()))
prev = l[0]
count = 0
f = 0
f_prev = 0
start = True
l = l[1::]
for i in l:
    if prev-i < 0 and f == 1:
        f = 1
    elif prev - i > 0 and f == -1:
        f = -1
    elif prev - i > 0 and (f == 0 or f == 1):
        f = -1
    elif prev - i < 0 and (f == 0 or f == -1):
        f = 1
    else:
        f = 0
    if f_prev != f or start:
        count += 1
    f_prev = f
    prev = i
    start = False
print(count)
