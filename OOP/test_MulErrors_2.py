import opa.OOP.MulErrors


def test_common_mull_1():
    m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    actual_result = 0.5 * m2
    expected_result = int('2.5\t1.0\t5.0\n-0.25\t-0.125\t9.0\n-11.0\t-1.25\t-0.0625')
    assert actual_result == expected_result, 'Чет, не робит'


def test_common_mull_2():
    mid = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
    m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    actual_result = m2 * (0.5 * mid * m1)
    expected_result = int('67.5\t30.0\n126.5\t44.5\n-21.375\t-22.3125')
    assert actual_result == expected_result, 'Чет, не робит'
