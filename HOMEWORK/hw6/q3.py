n = int(input("Enter the number to spell out: "))

digit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
digit_tenth = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def spell_number(n):
    if n < 10:
        print(digit[n - 1])
    elif n < 20:
        print(digit_teens[n - 11])
    elif n < 100:
        if n % 10 == 0:
            print(digit_tenth[n // 10 - 1])
        else:
            print(digit_tenth[n // 10 - 1] + '-' + digit[n % 10 - 1])
    elif n < 1000:
        if n % 100 == 0:
            print(digit[n // 100 - 1] + ' hundred')
        elif n % 100 < 10:
            print(digit[n // 100 - 1] + ' hundred and ' + digit[n % 100 - 1])
        elif n % 100 < 20:
            print(digit[n // 100 - 1] + ' hundred and ' + digit_teens[n % 100 - 11])
        else:
            print(digit[n // 100 - 1] + ' hundred and ' + digit_tenth[n % 100 // 10 - 1] + '-' + digit[n % 10 - 1])
    else:
        print("I don't know.")

spell_number(n)