def compose_functions(f, g):
    """Возвращает новую функцию h(x), которая является композицией функций f и g"""
    def h(x):
        """Композиция функций f и g"""
        return f(g(x))
    return h

def f(x):
    """Возвращает квадрат числа x"""
    return x**2

def g(x):
    """Возвращает число x плюс 1"""
    return x + 1

h = compose_functions(f, g)
print(h(2)) 

print('Nurkhan')
print('Aidynbek')
print('Damir')
<<<<<<< HEAD
print('ASD')
=======
print('llll')
print('hsdcgkyu')
>>>>>>> d8cd053b8674779973df32fbad5a1f9086d00399
