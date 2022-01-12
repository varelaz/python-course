class FlexibleModel:
    a = None
    b = None
    _other = None

    def __init__(self):
        self._other = {}

    def __setattr__(self, name, value):
        if hasattr(self, name):
            super().__setattr__(name, value)
        else:
            self._other[name] = value

    def __getattr__(self, name):
        try:
            return self._other[name]
        except KeyError:
            raise AttributeError(f'Attribute {name} doesn\'t exist')

    def save(self):
        pass
        


f = FlexibleModel()
f.a = 4
f.b = 3
f.c = 3

print('a,', f.a)
print('b,', f.b)
print('c,', f.c)

print('all data,', f.__dict__)

print('d', f.d)