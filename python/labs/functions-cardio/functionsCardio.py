# print("hello there, is your triangle really a triangle?")
# num1 = int(raw_input("give me side 1 of the triangle: "))
# num2 = int(raw_input("give me side 2 of the triangle: "))
# num3 = int(raw_input("give me side 3 of the triangle: "))
#
# def is_triangle(s1, s2, s3):
#     sum1 = s1 + s2 #test if greater than s3
#     sum2 = s2 + s3 #test if greater than s1
#     sum3 = s3 + s1 #test if greater than s2
#     if sum1 > s3 and sum2 > s1 and sum3 > s2:
#         print("you have  triangle")
#         return True
#     else:
#         print("loser, you don't have a triangle")
#         return False
#
# is_triangle(num1, num2, num3)

# LETTER COUNTER
# print("welcome to my letter counter")
# word1 = raw_input("enter your first word here: ")
# word2 = raw_input("enter your second word here: ")
# word3 = raw_input("enter your third word here: ")
#
# def longest_word(length1, length2, length3):
#     if len(length1) > len(length3) and len(length2):
#         longest = length1
#         print(length1 + " is the longest word")
#     elif len(length3) > len(length1) and len(length2):
#         longest = length3
#         print(length2 + " is the longest word")
#     elif len(length2) > len(length3) and len(length1):
#         longest = length2
#         print(length3 + " is the longest word")
# longest_word(word1,word2,word3)

#REVERSE STRONG
word = raw_input("give me a words: ")
def reverse_string(x):
    return x[::-1]

print("this is your backwards word " + reverse_string(word))
