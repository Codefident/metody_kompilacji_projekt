a = 2
b = -3
c = a + b
d = 2 ** 8

print(d)

my_list = [1, 1, 1,
           1, 1, 1]

my_obj = {
    "a": 2, 
    "b": -10
}

nothing = None
true_val = True
false_val = False

if nothing is None:
    print("printing nothing")
    print(nothing)

for i in range(len(my_list)):
    my_list[i] = i + 1

print(my_list[a - 1])
print("dlugosc_listy")
print(len(my_list))
print("my_obj")
print(my_obj["b"])

my_list.append(70)
print(my_list)
