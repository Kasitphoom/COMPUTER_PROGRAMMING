def print_table(list_table):
    for i in list_table:
        for j in i:
            print(j, end="\t")
        print()
        
table2 = [["ID", "Name", "Surname"], ["001", "Guido", "van Rossum"], ["002", "Donald", "Knuth"], ["003", "Gordon", "Moore"]]
print_table([["x", "y"], [0,0], [10,10], [200, 200]])
print()
print_table(table2)