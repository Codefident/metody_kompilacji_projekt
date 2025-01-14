for i in range(3):
    print(i)

print()
for i in range(3, 60):
    if i < 6:
        print(i)
    else: break

print()
for i in range(1, -2, -1):
    print(i)

def get_range(a, b):
    return b - a

print("\nget_range")
for i in range(get_range(5, 8)):
    print(i)
