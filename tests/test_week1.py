from opa.week1.assignments import divide_apples

def test_common_case():
    n = 3
    k = 14
    expected_result = 4
    actual_resulst = divide_apples(n, k)
    assert actual_resulst == expected_result

def test_common_case2():
    n = 1
    k = 14
    expected_result = k
    actual_resulst = divide_apples(n, k)
    assert actual_resulst == expected_result

def test_common_case3():
    n = 6
    k = 3
    expected_result = 0
    actual_resulst = divide_apples(n, k)
    assert actual_resulst == expected_result