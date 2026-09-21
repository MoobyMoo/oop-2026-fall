def add(a, b):
    return a + b

def devide(a, b):
    if b == 0:
        raise ValueError('Error: divide by 0')
    return a / b