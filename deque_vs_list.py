
def test():
    """Stupid test function"""
    lst.insert(4, 19)
    d.app
    print("hi")


if __name__ == '__main__':
    import timeit
    from collections import deque
    lst = [_ for _ in range(10)]
    d = deque([_ for _ in range(10)])
    # For Python>=3.5 one can also write:
    print(timeit.timeit("test()", globals=locals()))
