class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            hour = (self.current // 3600) % 24
            minute = (self.current // 60) % 60
            second = self.current % 60
            
            self.current += 1
            return '%02d'%hour + ':' + '%02d'%minute + ':' + '%02d'%second
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < self.stop - self.start:
            index += self.start
            hour = (index // 3600) % 24
            minute = (index // 60) % 60
            second = index % 60
            
            return '%02d'%hour + ':' + '%02d'%minute + ':' + '%02d'%second
        else:
            raise IndexError 

start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
