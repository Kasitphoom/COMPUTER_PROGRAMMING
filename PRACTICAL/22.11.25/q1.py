def list_member(x, a_list):
    if a_list == []:
        return False
    elif x == a_list[0]:
        return True
    else:
        return list_member(x, a_list[1:])
    
print(list_member(2, []))