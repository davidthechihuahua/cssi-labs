print("welcome to my thing that makes things plural")
word = raw_input("in put your word here: ")
num = int(raw_input("input your number of objects here here: "))
if num == 0:
    print(str(num + " " +word + "s"))
elif num > 1:
    print(str(num + " " + word + "s"))
else: print(str(num + " " + word))
