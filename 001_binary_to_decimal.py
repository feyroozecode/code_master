
def decimal_to_binary():
    d = int(input("Entrez un decimal :"))
    d_to_bin = bin(d)
    return [d_to_bin]

print("Convert Decimal to Binary")
rs = decimal_to_binary()[0]

print(" in binary is ", rs)
