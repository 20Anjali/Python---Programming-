r = int(input("Enter start number: "))

i = 1

# Upper part of the diamond
while i <= r:
    j = 1
    while j <= r - i:
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end=" ")
        j += 1
    print()
    i += 1

i = r - 1

# Lower part of the diamond
while i >= 1:
    j = 1
    while j <= r - i:
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end=" ")
        j += 1
    print()
    i -= 1
