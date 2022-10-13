""" Доработать связный список из Lesson_4 возможностью итерации. """


class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())


class List:
    def __init__(self, start=None, finish=None, length=0, values=[]):  # values: list
        self._start_pointer = start
        self._finish_pointer = finish
        self._length = length
        if len(values) != 0:
            for value in values:
                self.append(value)

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False

        if i <= len(self) / 2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
            return curr_pointer.get_value()

        if i > len(self) / 2:
            curr_pointer = self._finish_pointer
            for j in range(len(self)-1, i, -1):
                curr_pointer = curr_pointer.get_prev()
            return curr_pointer.get_value()

    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def __add__(self, other):
        if isinstance(other, List):
            if len(self) != 0:
                if len(other) != 0:
                    c = List(start=self._start_pointer, finish=self._finish_pointer)
                    c._finish_pointer.set_next(other._start_pointer)
                    c._finish_pointer = other._finish_pointer
                    c._length = len(self) + len(other)
                    return c
                else:
                    return self
            else:
                return other
        else:
            return False

    def pop(self, i):
        if i < 0 or i >= len(self):
            return False
        else:
            b = self[i]
            if i == 0:
                self._start_pointer = self._start_pointer.get_next()
                self._start_pointer.set_prev(None)
                self._length -= 1
                return b
            if i == (len(self) - 1):
                self._finish_pointer = self._finish_pointer.get_prev()
                self._finish_pointer.set_next(None)
                self._length -= 1
                return b
            else:
                if i <= len(self) / 2:
                    curr_pointer = self._start_pointer
                    for j in range(i):
                        curr_pointer = curr_pointer.get_next()
                if i > len(self) / 2:
                    curr_pointer = self._finish_pointer
                    for j in range(len(self) - 1, i, -1):
                        curr_pointer = curr_pointer.get_prev()
                curr_pointer.get_prev().set_next(curr_pointer.get_next())
                curr_pointer.get_next().set_prev(curr_pointer.get_prev())
                self._length -= 1
            return b

    def __iter__(self):  # прямая итерация
        node = self._start_pointer
        while node:
            yield node
            node = node.get_next()

    def __reversed__(self):  # обратная итерация
        node = self._finish_pointer
        while node:
            yield node
            node = node.get_prev()



# class LinkedListIterator:
#     def __init__(self, l_list):
#         self.index = 0
#         self.max_index = len(l_list)
#
#     def __next__(self):
#         self.index += 1
#         if self.index >= self.max_index:
#             raise StopIteration
#         return




A = List()
for i in range(5):
    A.append(i)
print(A)
C = List()
B = List(values=[5, 6, 7, 9])
print(B)
print(A + B)
print(A)
print(B)
print(A + C)
print(C + A)
print((A + B)[3])
print(C)
print(A.pop(0), A.pop(1), A.pop(2), A)
for i in A:
    print(i)
for i in reversed(A):
    print(i)


