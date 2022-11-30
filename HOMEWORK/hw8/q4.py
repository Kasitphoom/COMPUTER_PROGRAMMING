def checksumisbn(isbn):
    if len(isbn) != 9:
        return "Error: Input is not 9 digits"
    else:
        sum = 0
        for i in range(len(isbn)):
            sum += int(isbn[i])*(i+1)
        return sum % 11
    
isbn = input("Enter a 9-digit ISBN: ")
lastdigit = checksumisbn(isbn)
print("Your ISBN-10 number is ", end="")
if lastdigit == 10:
    print(isbn, "X", sep="")
else:
    print(isbn, lastdigit, sep="")
