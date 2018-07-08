class Kumanda():
    def __init__(self,kanal):
        self.kanal = kanal
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.kanal):
            return self.kanal[self.index]

        else:
            self.index = -1
            raise StopIteration

kumanda = Kumanda(['ATV','Star','Fox'])

iterator = iter(kumanda)

print(next(iterator))

print(next(iterator))

print(next(iterator))


print("---------------------------")

"""
for i in kumanda:
    print(i)

bu işlemin aynısı bu şekilde de yapılır.............

"""
