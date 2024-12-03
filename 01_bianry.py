# Day 01 : Binary Basics

def binary_operations():
    a = 0b1010  # 10 in binary
    b = 0b0101  # 5 in binary

    # Binary operations
    print("Bianry AND:"   ,   bin(a & b) )       #  AND
    print("Binary OR"     ,   bin(a | b) )       #  OR
    print("Binary XOR"    ,   bin(a ^ b) )       #  XOR
    print("Binary NOT (~a):", bin(~a)   )        #  NOT
    print("Left Shift (a << 1):", bin( a << 1))  # Left Shift
    print("Right Shift (a >> b)", bin (a >> 1 )) # Right Shift

binary_operations()
