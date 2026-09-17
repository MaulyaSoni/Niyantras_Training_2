def logging(func):
    def wrapper(*args):
        print(f"Start of the function {func.__name__!r}")
        result = func(*args)
        print(f"Completion of the function {func.__name__!r}")
        return result
    return wrapper