def add_list_insert(subj_list:list, pos:int, val:int) -> list:
    '''Add list using list's insert'''
    subj_list.insert(pos, val)
    return subj_list

def add_list_extend(subj_list:list, arg_list:list) -> list:
    '''Add list using list's extend method'''
    subj_list.extend(arg_list)
    return subj_list

def add_list_append(subj_list:list, val:int) -> list:
    '''Add list using list's append method'''
    subj_list.append(val)
    return subj_list

def add_list_plusop(subj_list:list, arg_list:list) -> list:
    '''Add list using + op'''
    subj_list = subj_list + arg_list
    return subj_list