import random


num_people = int(input("Enter number of people: "))


names = []
for i in range(num_people):
    name = input(f"Enter name {i+1}: ")
    names.append(name)


total_bill = float(input("Enter total bill: "))


payer_index = random.randint(0, len(names) - 1)
payer = names[payer_index]


split_amount = total_bill / len(names)


print(f"{payer} has to pay the full bill of Rs{total_bill:.2f}!")
print(f"Each person owes Rs{split_amount:.2f}.")
