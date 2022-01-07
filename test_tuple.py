def test_tuple_slice() -> None:
    tup = (1,2,3)
    tup2 = tup[0:2]
    assert tup2 == (1,2)
    tup3 = tup[:]
    assert tup == tup3
    assert tup3 == (1,2,3)
    val2 = tup[1]
    val3 = tup[-1]
    assert val2 == 2
    assert val3 == 3
