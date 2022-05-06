f = open('test.txt', 'r') # r - read

x = f.read()
x = x.splitlines()

f2 = open('newfile.txt', 'w+')
n = len(x)
for i in range(n):
    f2.write(x[n-i-1]+'\n')

# for line in f:
#     line = line.rstrip()
#     print(repr(line))

# x = f.read()
# print(repr(x))
f2.close()
f.close()