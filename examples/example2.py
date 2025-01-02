def hello(x):
    print(x)

hello("Hello everyone from a function!")

a = 0

print(a)
for i in range(10):
    if a % 2 == 0:
        print("a jest parzyste")
    else:
        print("a jest nieparzyste")
    a += 1
print(a)

while a > 0:
    a -= 1
    if a < 5:
        print("a jest mniejsze od 5")
    else: continue
print(a)