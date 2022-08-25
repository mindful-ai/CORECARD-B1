class stack(object):

    maxsize = 10

    def __init__(self, type=int, size=10):
        self._stack = []
        self._type = type
        self._size = size

    def push(self, dataunit):
        if len(self._stack) <= stack.maxsize:
            if type(dataunit) == self._type:
                self._stack.insert(0, dataunit)
                return 1
            else:
                return 0
        else:
            return 0

    def pop(self):
        if len(self._stack) == 0:
            return None
        else:
            return self._stack.pop(0)

    def empty(self):
        self._stack = []


# --------------------------------------------------

s = stack(type=int, size=20) # Stack of object in LIFO basis

print(s.push(10))
print(s.push(20))
print(s.push(30))
print(s.push('10'))
print(s.push('10'))


print(s.pop()) # 30
print(s.pop()) # 20
print(s.pop()) # 10
print(s.pop()) # None