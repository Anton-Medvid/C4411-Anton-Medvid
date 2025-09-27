class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i
count1 = Counter(5)
#for i in count1:
#    print(i)
count2 = Counter(10)
#for j in count2:
#    print(j)
print('Counter1:', next(count1))
print('Counter2:', next(count2))
print('Counter2:', next(count2))
print('Counter1:', next(count1))
print('Counter2;', next(count2))
print('Counter1:', next(count1))
print('Counter1:', next(count1))
print('Counter2:', next(count2))


