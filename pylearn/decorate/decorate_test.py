def outer(fun):
    def wrapper(*args,**kw):
        print("start")
        fun()
        print("end")
    return wrapper

def outer1(fun):
    def wrapper(*args,**kw):
        print("start1")
        fun()
        print("end1")
    return wrapper

@outer
@outer1
def hello():
    print("hello")

if __name__ == "__main__":
    hello()