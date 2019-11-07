fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)
print("-----------------------\n")

#Menambah data
fruits.add("Ceri")
for fruit in fruits:
    print(fruit)
print("-----------------------\n")

#Menghapus Data
fruits.remove("apple")
fruits.add("semangka")
for fruit in fruits:
    print(fruit)
print("-----------------------\n")