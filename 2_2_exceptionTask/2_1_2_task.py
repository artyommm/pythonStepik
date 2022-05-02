# Алгоритм depth взят из задачи 1_6_1

all_classes = {}
exceptions = []
mas = []


def depth(parent, child):
    global mas
    mas.extend(all_classes[child])
    for element_of_child in all_classes[child]:
        depth(parent, element_of_child)


n = int(input())

for i in range(n):
    input_str = str(input()).strip()
    if ':' in input_str:
        children, parents = input_str.split(':')
        children = children.strip()
        parents = parents.strip()
        if children not in all_classes.keys():
            all_classes[children] = []
        if ' ' in parents:
            all_classes[children].extend(str(parents).strip().split(' '))
        else:
            all_classes[children].append(parents)
    else:
        new_class = input_str
        all_classes[new_class] = []

k = int(input())
for i in range(k):
    input_str = str(input())
    exceptions.append(input_str)

print_exceptions = []

for i in range(k):
    for j in range(len(exceptions)):
        depth(exceptions[j], exceptions[i])
        #if exceptions[j] in all_classes[exceptions[i]]:
        if exceptions[j] in mas:
            if exceptions[i] not in print_exceptions and i > j:
                print_exceptions.append(exceptions[i])
        mas = []

for i in range(len(print_exceptions)):
    print(print_exceptions[i])

print(all_classes)