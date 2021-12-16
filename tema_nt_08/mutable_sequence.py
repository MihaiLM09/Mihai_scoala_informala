from collections.abc import MutableSequence
from utils import print_header

class CrayonsBox(MutableSequence):
    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        print('Getting the len of the crayon box: {}'.format(len(self._crayons)))
        return len(self._crayons)


    def __getitem__(self, index):
        print('{}: {}'.format(index, self._crayons[index]))
        return self._crayons[index]

    def __setitem__(self, index, value):
        print('Decided that index {} has to be changed'.format(index, self._crayons[index]))
        self._crayons[index] = value

    def __delitem__(self, index):
        print('User wanted index {} to be deleted'.format(index, self._crayons[index]))
        del self._crayons[index]

    def insert(self, index, value):
        self._crayons.insert(index, value)



crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

print_header('__len__')
print(len(crayons_box))

print_header('__getitem__')
print(crayons_box[2])

print_header('__contains__')
if 'Green' in crayons_box:
    print('Green crayon is in the crayon box')

print_header('__iter__')
for crayons in crayons_box:
    print(crayons)

print_header('__setitem__')
crayons_box[3] = 'Ferrari Red'
for crayons in crayons_box:
    print(crayons)

print_header('__delitem__')
del crayons_box[2]
for crayons in crayons_box:
    print(crayons)

print_header('insert')
crayons_box.insert(4, 'CocaCola Red')
for crayons in crayons_box:
    print(crayons)