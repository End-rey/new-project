import numpy


def reverse_arr():
    arr = input().strip().split(' ')
    a = numpy.array(arr, float)
    result = numpy.flip(a)
    print(result)


def concatenate_arr():
    n, m, p = map(int, input().strip().split())
    arr1 = numpy.array([input().split() for y in range(n)], int)
    arr2 = numpy.array([input().split() for y in range(m)], int)
    print(numpy.concatenate((arr1, arr2), axis=0))


def zeros_ones():
    a = tuple(map(int, input().split()))
    print(numpy.zeros(a, dtype=numpy.int64))
    print(numpy.ones(a, dtype=numpy.int64))


def main():
    zeros_ones()


if __name__ == "__main__":
    main()
