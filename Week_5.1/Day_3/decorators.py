from decorator_interface import ShippingDecorator

class LogginDecorator(ShippingDecorator):
    def __init__(self , dec : ShippingDecorator):
        self.dec = dec

    def status_log(self , status_log):
        print(f"Wrapping up the object : {status_log}")

def logging(func):
    def wrapper(*args):
        print(f"Start of the function {func.__name__!r}")
        result = func(*args)
        print(f"Completion of the function {func.__name__!r}")
        return result
    return wrapper