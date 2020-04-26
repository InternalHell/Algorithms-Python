class Heap:
    def __init__(self):
        self.volues = []
        self.size = 0

    def insert(self, x):
        self.volues.append(x)
        self.size += 1
        self.up(self.size-1)

    def up(self, i):
        while i != 0 and self.volues[i] < self.volues[(i-1)//2]:
            self.volues[i], self.volues[(i-1)//2] = self.volues[(i-1)//2], self.volues[i]
            i = (i - 1) // 2

    def min(self):
        tmp = self.volues[0]
        self.volues[0] = self.volues[-1]
        self.volues.pop()
        if not self.size:
            return None
        self.size -= 1
        self.down(0)
        return tmp

    def down(self, i):
        while i*2+1 < self.size:
            if self.volues[i*2+1] < self.volues[i]:
                j = i*2+1
            if i*2+2 < self.size and self.volues[i*2+2] < self.volues[i*2+1]:
                j = i*2+2
            if i == j:
                break
            self.volues[i],self.volues[j] = self.volues[j],self.volues[i]
            i = j
        
def heap_sort(list):
    arr = []
    heap = Heap()
    for i in list:
        heap.insert(i)
    while heap.size:
        arr.append(heap.min())
    return arr
if __name__ == '__main__':
    from random import *
    list = [randint(1,100) for i in range(10)]
    print('Start list:',list)
    print(heap_sort(list))
