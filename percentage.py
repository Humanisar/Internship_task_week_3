sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))

total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

# Grades on the basis of percentage
if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# results
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
