# Sample code on how recursion works
def one():
        two()
        print("1")

def two():
        three()
        print("2")

def three():
        four()
        print("3")

def four():
        print("4")

one()
