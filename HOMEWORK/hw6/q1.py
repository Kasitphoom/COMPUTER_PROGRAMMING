def time24hourto12hour(time):
    time = time.split(':')
    hr = time[0]
    min = time[1]
    
    hr12 = int(hr) % 12
    
    if int(hr) > 12:
        ampm = 'PM'
    else:
        ampm = 'AM'
        
    return str(hr12) + ':' + min + ' ' + ampm
    
t = input("Enter time in 24 hour format: ")
print(time24hourto12hour(t))