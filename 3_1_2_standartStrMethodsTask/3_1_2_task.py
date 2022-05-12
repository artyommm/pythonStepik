s = str(input().strip())
t = str(input().strip())

count = 0
start = 0
while s.find(t, start) != -1:
    count += 1
    start = s.find(t, start) + 1

print(count)