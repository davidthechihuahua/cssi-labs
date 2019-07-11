print("hello there")
myString = raw_input("give me a string to loop")
letterNum = 1


for character in myString:
    print("this is the first letter %s: " %(letterNum))
    letterNum = letterNum + 1
    print(character)
