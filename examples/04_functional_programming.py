# Functions are objects

def example():
    ...


func = example

func()

funcs = [func, lambda: 1]


# Generator
def gen():
    yield 0
    yield 1
    yield 2


for n in gen():
    # print(n)
    pass

# Map
gen = map(print, [0, 1, 2])
list(gen)

# Filter
res = filter(lambda n: n < 10, [0, 5, 10, 15])  # filter object
print(list(res))
