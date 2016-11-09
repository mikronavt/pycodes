class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            list.append(self, x)


class NonPositiveError(Exception):
    pass

p = PositiveList()
p.append(1)