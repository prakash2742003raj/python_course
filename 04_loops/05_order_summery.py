names = ["Nishant", "Ankit", "Prakash", "Rachana", "Karina"]
bills = [50, 70, 80, 43, 28]

# for item in zip(names,bills):
#     print(f"{item[0]}: {item[1]}")
#              OR

for name, amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")

