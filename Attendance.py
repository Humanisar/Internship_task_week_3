attendance = float(input("Enter your attendance percentage: "))
marks = float(input("Enter your final marks: "))

# Check if the student is promoted based on attendance and marks
if attendance >= 75 and marks >= 50:
    print("Promoted")
else:
    print("Not promoted")
