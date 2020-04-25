class Heap:
    def __init__(self):
        self.volues = []
        self.size = 0

    def insert(self, x):
        self.volues.append(i)
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
        while 2*i+1 < self.size:
            if self.volues[2*i+1] < self.volues[i]:
                j = 2*i+1
            if 2*i+2 < self.size and self.volues[2*i+2] < self.volues[j]:
                j = 2*i+2
            if i == j:
                break
            self.volues[i], self.volues[j] = self.volues[j], self.volues[i]
            j = i
def heapfy(arr):
    heap = Heap()
    for i in arr:
        heap.insert(i)
    return heap_sort(heap)
def heap_sort(heap):
    arr = []
    while heap.size:
        arr.append(heap.min())
    return arr
x = Heap()
list = [23,17,19,12,9,18,7,10,20]
print(heapfy(list))