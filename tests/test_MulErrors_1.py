import opa.OOP.MulErrors


def test_common_mull_1():
    mid = opa.OOP.MulErrors.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1 = opa.OOP.MulErrors.Matrix([[3, 2], [-10, 0], [14, 5]])
    actual_result = mid * m1
    expected_result = opa.OOP.MulErrors.Matrix(
        [[3, 2],
         [-10, 0],
         [14, 5]]
    )
    assert actual_result == expected_result, 'Чет, не робит'


def test_common_mull_2():
    mid = opa.OOP.MulErrors.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m2 = opa.OOP.MulErrors.Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    actual_result = mid * m2
    expected_result = opa.OOP.MulErrors.Matrix([[5.0, 2.0, 10.0],
                                                [-0.5, -0.25, 18.0],
                                                [-22.0, -2.5, -0.125]])
    assert actual_result == expected_result, 'Чет, не робит'


def test_common_mull_3():
    m1 = opa.OOP.MulErrors.Matrix([[3, 2], [-10, 0], [14, 5]])
    m2 = opa.OOP.MulErrors.Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    actual_result = m2 * m1
    expected_result = opa.OOP.MulErrors.Matrix([[135, 60],
                                                [253.0, 89.0],
                                                [-42.75, -44.625]])
    assert actual_result == expected_result, 'Чет, не робит'


def test_error():
    m1 = opa.OOP.MulErrors.Matrix([[3, 2], [-10, 0], [14, 5]])
    m2 = opa.OOP.MulErrors.Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    try:
        m1 * m2
    except opa.OOP.MulErrors.MatrixError as e:
        print('Handled an exception, everything is OK')
        print(e.matrix1)
        print(e.matrix2)
