myDict = {
    's5301': 'Fred',
    's5302': 'Harry',
    's5303': 'John',
    's5304': 'Fred',
    's5305': 'Harry',

}

def find_duplicates(dict):
    dupes = {}
    temp = {}
    for key, value in dict.items():
        if value not in temp:
            temp[value] = [key]
        else:
            temp[value].append(key)
    
    for k,v in temp.items():
        if len(v) > 1:
            for i in v:
                dupes[i] = k
    
    return dupes
    

print(find_duplicates(myDict))