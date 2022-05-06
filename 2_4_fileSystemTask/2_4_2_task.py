import os
import os.path

result = []

with open('test.txt', "w") as f:
    for current_dir, dirs, files in os.walk("main"):
        for file in files:
            if file[-3:] == '.py' and current_dir[5:] not in result:
                result.append(current_dir[5:])
                f.write(current_dir[5:]+'\n')

result.sort()

with open('test.txt', "w") as f:
    for line in result:
        f.write(line.replace('//', '/') + '\n')