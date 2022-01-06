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

def ds_main() -> None:
    '''datastructure main driver'''
    main_list = []
    main_list = add_list_append(main_list, 1)
    print(main_list)
    main_list = add_list_plusop(main_list, [2])
    print(main_list)
    main_list = add_list_extend(main_list, [3,'4'])
    print(main_list)
    main_list = add_list_insert(main_list, 2, -3)
    print(main_list)
    print("end of the ds_main")


if __name__ == '__main__':
    ds_main()