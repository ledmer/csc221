def foo():
    print("Hello, I'm foo!")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    foo()
