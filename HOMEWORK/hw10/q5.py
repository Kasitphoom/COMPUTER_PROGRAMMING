def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    for i in range(len(s1)):
        if s1[i] not in s2:
            return False
        else:
            s2 = s2.replace(s1[i], '', 1)
    return True

print(isAnagram("silent", "listen"))
print(isAnagram("silent", "annda1"))