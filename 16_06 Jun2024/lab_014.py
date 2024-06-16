
# Write a program that calculates the grade of students
# Input score ---89
# output --B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59


#step1
# Figureout the input

scale = int(input("Enter the number you got"))

# step2
# Logic

if scale >=90 and scale <= 100:
    print("A")
elif scale >=80 and scale <=89:
    print("B")
elif scale >=70 and scale <=79:
    print("C")
elif scale >=60 and scale <=69:
    print("D")
elif scale >=0 and scale <=59:
    print("E")
else:
    print("Invalid input")








