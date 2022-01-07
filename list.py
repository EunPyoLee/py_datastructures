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

def list_count(subj_list:list, val:any) -> int:
    ''''Count # of occurence of `val`'''
    return subj_list.count(val)

def has_val(subj_list:list, val:any) -> bool:
    '''
    Return true if the `subj_list` has the val
    OW return false
    '''
    return val in subj_list

def get_idx(subj_list:list, val:any) -> int:
    '''
    Return the first occurence `val`'s idx position
    CAUTION: it raises ValueError if not exist
    '''
    return subj_list.index(val)

def remove_val(subj_list:list, val:any) -> None:
    '''
    Remove first occuring `val` from the `subj_list`
    CAUTION: removing non-existing `val` will raise ValueError
    '''
    subj_list.remove(val)