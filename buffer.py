class Buffer:
    def __init__(self):
        self.lst = []
        # конструктор без аргументов

    def add(self, *a):
        # добавить следующую часть последовательности
        for el in a:
            self.lst.append(el)
        while len(self.lst) >= 5:
            sum = 0
            for i in range(5):
                el = self.lst[i]
                sum += el
            for i in range(5):
                self.lst.pop(0)
            print(sum)

    def get_current_part(self):
        return self.lst
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
