income=int(input("Enter your income: "))
expenses=int(input("Enter your expenses: "))

savings=income-expenses

if savings > 10000:
    print("saving well")
elif 5000 <= savings <= 9999:
    print("Average")
else:
    print("Try to Save")

print("Your monthly savings:", savings)