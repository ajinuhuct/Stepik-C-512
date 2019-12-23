def list_sum(lst):
    result=0
    for elem in lst:
        result+=elem
    return result


def sum(a,b):
    return a+b


y = sum(2,3)
z = list_sum([1,2,3])
print(y)
print(z)

print("Дальше стек")

x = [1,2,3]
x.append(4)
x.append(5)

print(x)

top = x.pop()
print(top)
print(x)


print("Дальше задача")

def h():
  print(12)

def f():
  g(h)

def g(a):
  a()

g(f)

print("Дальше задача 1.3.9")

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        return x+(5-(x%5))
print(closest_mod_5(12))
