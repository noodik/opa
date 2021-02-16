import opa.OOP.MulErrors


def test_common_mull_1():
    mid = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
    actual_result = mid * m1
    expected_result = int('3\t2\n-10\t0\n14\t5')
    assert actual_result == expected_result, 'Чет, не робит'


def test_common_mull_2():
    mid = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    actual_result = mid * m2
    expected_result = int('5.0\t2.0\t10.0\n-0.5\t-0.25\t18.0\n-22.0\t-2.5\t-0.125')
    assert actual_result == expected_result, 'Чет, не робит'


def test_common_mull_3():
    m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
    m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    actual_result = m2 * m1
    expected_result = int('135\t60\n253.0\t89.0\n-42.75\t-44.625')
    assert actual_result == expected_result, 'Чет, не робит'


def test_error():
    mid = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
    m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    try:
        m = m1 * m2
        print("WA It should be error")
    except MatrixError as e:
        print(e.matrix1)
        print(e.matrix2)
