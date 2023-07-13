def choose2(mylist):
    """
      >>> two = choose2([1, 2, 3, 4, 5, 6, 7])
      >>> len(two)
      2
    """
    return mylist[:2]


def run():
    stuff = ["George", "Ringo", "Paul", "John"]
    print(choose2(stuff))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    run()
