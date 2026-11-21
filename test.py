import copy
class MyClass:
    def __init__(self,value):
      self.value=value

o=MyClass([1,2,3])
s=copy.copy(o)
d=copy.deepcopy(o)
o.value.append(100)
print(o.value)
print(s.value)
print(d.value)    