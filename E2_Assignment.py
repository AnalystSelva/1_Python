print("Print Range 0 t0 20")
for i in range(0, 20):
    print(i)

print("Print Range 10 to 20")
for i in range(10, 20):
    print(i)

list_data = [10, 20, 14, 55, 43, 87, 76]
print("Number of item in the List:", len(list_data))

for i in "Artificial Intelligence":
    print(i)

Name = input("Your Name-")
Age = int(input("Your Age-"))
profession = input("Your Profession-")
tuples = (Name, Age, profession)
print(tuples)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'HOPE')
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

list_val = [20, 10, 16, 19, 25, 1, 276, 188]
for i in list_val:
    if i % 2 == 1:
        print(i, "is odd")

list_val = [20, 10, 16, 19, 25, 1, 276, 188]
for i in list_val:
    if i % 2 == 0:
        print(i, "is even")
