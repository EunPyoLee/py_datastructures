import list

def ds_main() -> None:
    '''datastructure main driver'''
    main_list = []
    main_list = list.add_list_append(main_list, 1)
    print(main_list)
    main_list = list.add_list_plusop(main_list, [2])
    print(main_list)
    main_list = list.add_list_extend(main_list, [3,'4'])
    print(main_list)
    main_list = list.add_list_insert(main_list, 2, -3)
    print(main_list)
    print("end of the ds_main")


if __name__ == '__main__':
    ds_main()