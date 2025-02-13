bill=int(input("Enter bill : "))
person=int(input("No.of persons : "))
tip=int(input("percent of tip : "))
tip_amount=bill*(tip/100)
total_amount=bill+tip_amount
contribution=total_amount/person
print(f"contribution : {contribution}")
