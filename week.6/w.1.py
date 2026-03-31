# Creating list using list()
a = list([3, 1, 2, 2])

print("Original list:", a)

print("Length:", len(a))                 # len()
print("Count of 2:", a.count(2))        # count()
print("Index of 1:", a.index(1))        # index()

a.append(5)                              # append()
a.insert(1, 10)                          # insert()
a.extend([7, 8])                         # extend()
a.remove(2)                              # remove()
a.pop()                                  # pop()
a.reverse()                              # reverse()
a.sort()                                 # sort()

b = a.copy()                             # copy()
a.clear()                                # clear()

print("Modified copy list:", b)
print("Cleared original list:", a)






















# Creating a tuple
t = (5, 2, 8, 2, 1)

print("Original Tuple:", t)

print("Length:", len(t))                # len()
print("Count of 2:", t.count(2))        # count()
print("Index of 8:", t.index(8))        # index()
print("Sorted Tuple:", sorted(t))       # sorted()
print("Minimum value:", min(t))         # min()
print("Maximum value:", max(t))         # max()
print("Reversed Tuple:", tuple(reversed(t)))  # reversed()
