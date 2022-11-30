s = input("Enter some text: ")

def countfreq(s):
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    return freq

freq = countfreq(s)
print("\n-- Character Frequency Table --")
print("Chara\tPercentage")

for i in freq:
    print(i, "\t", format(freq[i]/len(s)*100, "5.2f"), "%", sep="")