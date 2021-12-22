import numpy


def reverse_arr():
    # записываем массив в обратном порядке
    arr = input().strip().split(' ')
    a = numpy.array(arr, float)
    result = numpy.flip(a)
    print(result)


def concatenate_arr():
    # соединение 2 массивов по оси 0
    n, m, p = map(int, input().strip().split())
    arr1 = numpy.array([input().split() for y in range(n)], int)
    arr2 = numpy.array([input().split() for y in range(m)], int)
    print(numpy.concatenate((arr1, arr2), axis=0))


def zeros_ones():
    # создаем матрицы заполненными 0 и 1, с заданной размерностью
    a = tuple(map(int, input().split()))
    print(numpy.zeros(a, dtype=numpy.int64))
    print(numpy.ones(a, dtype=numpy.int64))


def sum_prod():
    # находим сумму по оси 0 потом произведение всех элементов суммы
    n, m = map(int, input().split())
    a = numpy.array([input().split() for i in range(n)], int)
    summ = numpy.sum(a, axis=0)
    print(numpy.prod(summ))


def min_max():
    # находим минимум по оси 1, потом максимальный элемент
    n, m = map(int, input().split())
    a = numpy.array([input().split() for i in range(n)], int)
    minn = numpy.min(a, axis=1)
    print(numpy.max(minn))


def mean_var_std():
    # среднее арифметическое, дисперсия и стандартное отклонение
    n, m = map(int, input().split())
    a = numpy.array([input().split() for i in range(n)], int)
    print(numpy.mean(a, axis=1))
    print(numpy.var(a, axis=0))
    print(round(numpy.std(a), 11))


def matrix_product():
    # произведение матриц
    n = int(input())
    a = numpy.array([input().split() for i in range(n)], int)
    b = numpy.array([input().split() for i in range(n)], int)
    print(numpy.dot(a, b))


def inner_outer():
    # скалярное и outer произведения матриц
    a = numpy.array(input().split(), int)
    b = numpy.array(input().split(), int)
    print(numpy.inner(a, b))
    print(numpy.outer(a, b))


def value_of_p_at_point_x():
    # находит значение полинома в заданной точке
    p = numpy.array(input().split(), float)
    x = float(input())
    print(numpy.polyval(p, x))


def determinant():
    # определитель матрицы
    n = int(input())
    a = numpy.array([input().split() for i in range(n)], float)
    print(round(numpy.linalg.det(a), 2))


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


def main():
    strip_test()


if __name__ == "__main__":
    main()
