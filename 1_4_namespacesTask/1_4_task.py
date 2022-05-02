n = int(input())
namespaces = {'global': 'None', }

variables = {'global': [], }


def get(namespace, var):
    global variables
    global namespaces
    if namespace == 'global':
        return 'global' if var in variables['global'] else 'None'
    if var in variables[namespace]:
        return namespace
    else:
        return get(namespaces[namespace], var)


for i in range(n):
    act, ns, vrb = map(str, input().split())
    # print('{} {} {}'.format(act, ns, vrb))
    if (act == 'create'):
        namespaces[ns] = vrb  # пространство имён:родитель
        if ns not in variables:
            variables[ns] = list()
    if (act == 'add'):
        if ns not in variables:
            variables[ns] = list()
        variables[ns].append(vrb)  # пространство имён: (переменная, переменная2 ...)
    if (act == 'get'):
        if ns not in variables:
            variables[ns] = list()
        print(get(ns, vrb))
        # if ns not in variables:
        #     variables[ns] = list()
        # if vrb not in variables[ns]:
        #     if vrb not in variables[namespaces[ns]]:
        #         print('None')
        #     else:
        #         print(namespaces[ns])
        # else:
        #     print(ns)

for key in variables.keys():
    print('key: {}, variables: {}'.format(key, variables[key]))
