import list
def test_add_list() -> None:
    subj_list:list = []
    subj_list = list.add_list_append(subj_list, 1)
    assert subj_list == [1]
    subj_list = list.add_list_extend(subj_list, [2,3])
    assert subj_list == [1,2,3]
    subj_list = list.add_list_insert(subj_list, 1, -1)
    assert subj_list == [1,-1,2,3]
    subj_list = list.add_list_plusop(subj_list, arg_list=[4,'5'])
    assert subj_list == [1,-1,2,3,4,'5']


def test_count_list() -> None:
    subj_list:list = [1, 2, 3, '3', 4, 'hi', 2]
    assert list.list_count(subj_list, 2) == 2
    assert list.list_count(subj_list, 5) == 0
    assert list.get_idx(subj_list, 4) == 4
    try:
        res = list.get_idx(subj_list, 0)
    except ValueError as e:
        assert True, e
    else:
        assert False
    assert list.has_val(subj_list, 'hi') == True

def test_remove_list() -> None:
    subj_list:list = [1,2,3,1]
    list.remove_val(subj_list, 1)
    assert subj_list == [2,3,1]
    try:
        list.remove_val(subj_list, 4)
    except ValueError:
        assert True
    else:
        assert False

def test_pop_list() -> None:
    subj_list:list = [1,2,3]
    assert subj_list.pop() == 3
    assert subj_list.pop(0) == 1
    assert subj_list.pop(0) == 2
    try:
        subj_list.pop()
    except IndexError:
        assert True
    else:
        assert False