class Coat:  # Class - это тип объектов
    leg = 4  # Классовый атрибут, используются, как const

    def __init__(self, weight, height):  # Классовые методы
        self.height = height
        self.weight = weight

    def __str__(self):
        s = 'weight = {}, height = {}'.format(self.weight, self.height)
        return s


mw = Coat(60, 40)
no = Coat(65, 30)
mw.weight += 1
for x in mw, no:
    print(x)
x = mw  # Ссылка на объект mw
x.weight += 1  # Измениться объект mw
mw.leg += 1  # Новый объект у mw
'''a = [1]
a.append([2])
a[1].append([3,a])
p = a
while p is not None:
    print(p[0])
    p = p[1]
    '''
