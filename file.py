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
    strip_test()


def strip_test():
    strinput = "  $$$$$  No. 1 Welcome to JAVATPOINT!! No. 1 $$$ "
    # use strip() function to remove the set of characters
    res = strinput.strip(' $No. 10 !')  # store result into res variable
    print(" Given string is: ", strinput)
    print(" After removing the set of characters: ", res)

    str3 = ' 1 11 111 111 1111 Learn Python Programming Tutorial 1111 111 11 1 '
    str4 = str3. strip(' 1')
    print(" n  Given string is ", str3)
    print(" Stripping 1 from both ends of the string using strip ('1') function ", str4)

    # define new string
    str5 = '++++++Python Programming Tutorial****** $$$$$'
    print("n Given string is = ", str5)
    # use strip function to remove the symbols from both ends
    str6 = str5. strip(' $*+')
    print(" Stripping the '+', '*' and '$' symbols on both sides of the string is = ", str6)


if __name__ == "__main__":
    main()
