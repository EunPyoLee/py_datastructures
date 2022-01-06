import datastructure
def test_add_list() -> None:
    subj_list:list = []
    subj_list = datastructure.add_list_append(subj_list, 1)
    assert subj_list == [1]
    subj_list = datastructure.add_list_extend(subj_list, [2,3])
    assert subj_list == [1,2,3]
    subj_list = datastructure.add_list_insert(subj_list, 1, -1)
    assert subj_list == [1,-1,2,3]
    subj_list = datastructure.add_list_plusop(subj_list, arg_list=[4,'5'])
    assert subj_list == [1,-1,2,3,4,'5']