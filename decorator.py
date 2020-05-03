# from future import print_function
# from logger_decor import myDecorator
def myDecorator(func):
    func_name = func.__name__
    def wraper(*args, **kwargs):
        print(f'Calling {func_name}({args,}, {kwargs})')
        result = func(*args, **kwargs)
        print(f'Finished {func_name}({result})')      
    return wraper

@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    print("argument a: ", a)
    print("argument b: ", b)
    print("argument args: ", args)
    print("argument kwargs: ", kwargs)
    return a + b

testFunc(2, 3, 4, 5, c=6, d=7)
testFunc(2, c=5, d=6)
testFunc(10)

# Calling testFunc((2, 3, 4, 5), {'c': 6, 'd': 7})
# argument a: 2
# argument b: 3
# argument args: 4,5
# argument kwargs: c: 6, d: 7
# Finished testFunc(5)

# Calling testFunc((2,), {'c': 5, 'd': 6})
# argument a: 2
# argument b: 1
# argument args: ()
# argument kwargs: c: 5, d: 6
# Finished testFunc(3)

# Calling testFunc((10,), {})
# argument a: 10
# argument b: 1
# argument args: ()
# argument kwargs: {}
# Finished f(11)