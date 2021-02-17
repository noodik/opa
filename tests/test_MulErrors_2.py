from opa.OOP.MulErrors import Matrix


def test_common_mull_1():
    m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    actual_result = 0.5 * m2
    expected_result = Matrix([[2.5, 1.0, 5.0], [-0.25, -0.125, 9.0], [-11.0, -1.25, -0.0625]])

    assert actual_result == expected_result, f'{actual_result} vs {expected_result}'


def test_common_mull_2():
    mid = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
    m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
    actual_result = m2 * (0.5 * mid * m1)
    expected_result = Matrix([[67.5, 30.0],
                              [126.5, 44.5],
                              [-21.375, -22.3125]])
    assert actual_result == expected_result
