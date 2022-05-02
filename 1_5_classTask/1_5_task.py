class Buffer:
    def __init__(self): # конструктор без аргументов
        self.seq = []
        self.counter = 0
        self.sum = 0
    def add(self, *a): # добавить следующую часть последовательности
        for item in a:
            self.seq.append(item)
            self.counter += 1
            self.sum += item
            if self.counter == 5:
                print(self.sum)
                self.counter = 0
                self.sum = 0
                self.seq = []

    def get_current_part(self):# вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.seq
buf = Buffer()
buf.add(1, 2, 3)
buf.add(4, 5, 6)
print(buf.seq)