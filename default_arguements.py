from random import randint


def my_func(li=set()):
    li.add(randint(1, 10))
    print(li)
    

if __name__ == "__main__":
    my_func()
    my_func()
    my_func()
    my_func()