class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        print(x)
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError()

temp = PositiveList()
temp.extend([1, 2, 3, 4])
temp.append(-5)
print(temp)