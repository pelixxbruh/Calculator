def add_one(x):
  return x + 1


def sub_one(x):
  return x - 1

def add(x, y):
    if y == 0:
        return x
    if y >= 0:
        y = sub_one(y)
        x = add_one(x)
        return add(x,y)
    else:
        y = add_one(y)
        x = sub_one(x)
        return add(x,y)


def sub(x,y):
    if y == 0:
        return x
    if y >= 0:
        y = sub_one(y)
        x = sub_one(x)
        return sub(x,y)
    else:
        y = add_one(y)
        x = add_one(x)
        return sub(x,y)


def mull(x, y):
    
    if x == 0 or y == 0:
        return 0
    if x < 0:
        x = sub(0,x)
        return sub(0,mull(x,y))
    if y < 0:
        y = sub(0,y)
        return sub(0,mull(x,y))
    if y == 1:
        return x
    return add(x, mull(x, sub(y, 1)))


def div(x,y):
    if x < 0:
        x = sub(0,x)
        return sub(0,div(x,y))
    if y < 0:
        y = sub(0,y)
        return sub(0,div(x,y))
    if x < y:
        return 0
    return add(1, div(sub(x,y),y))


def pow(x,y):
    if y == 0:
        return 1
    if y == 1:
        return x
    return mull(x, pow(x, sub(y,1)))


def factorial(x):
    if x == 0:
        return 1
    return mull(x, factorial(sub(x,1)))    

