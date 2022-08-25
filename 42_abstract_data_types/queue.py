class queue(object):
    pass

# -----------------------------------------

s = queue() # queue of object working in FIFO basis

print(s.put(10))
print(s.put(20))
print(s.put(30))
print(s.put('10'))
print(s.put('10'))


print(s.get()) # 10
print(s.get()) # 20
print(s.get()) # 30
print(s.get()) # '10'