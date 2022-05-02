all_classes = {}
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
        all_classes[children].extend(str(parents).strip().split(' '))
    else:
        new_class = input_str
        all_classes[new_class] = []


k = int(input())
for i in range(k):
    input_str = str(input())
    parent, child = input_str.split(' ')
    depth(parent, child)
    if parent in mas or parent == child:
        print('Yes')
    else:
        print('No')
    mas = []
