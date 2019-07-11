def count_spaces(s):
    return s.count(" ")

def count_vowels(s):
    numA = s.count("a")
    numE = s.count("e")
    numI = s.count("i")
    numO = s.count("o")
    numU = s.count("u")
    sumVowles = numA + numE + numO + numI + numU
    return sumVowles
def count_totals(s):
    return count_spaces(s) + count_vowels(s)

print(count_vowels("hello there my child"))

countNum = count_vowels("hello there my child")
print(countNum)
