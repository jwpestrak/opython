def addarg(i):
    def mdeco(f):
        def wrapper(*args, **kwargs):
            return f(i, *args, **kwargs)
        return wrapper
    return mdeco
