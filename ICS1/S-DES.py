# Abhishek Bhalerao
### BE. Comp. METIOE, Nashik


#initialization

IP = [2, 6, 3, 1, 4, 8, 5, 7]
IPi = [4, 1, 3, 5, 7, 2, 8, 6]
E = [4, 1, 2, 3, 2, 3, 4, 1]
S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
     ]
S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
     ]
P4 = [2, 4, 3, 1]
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]

#Function Definitions

def permutation(pattern, key):
    permuted = ""
    for i in pattern:
        permuted += key[i-1] 
    return permuted

def generate_first(left, right):
    left = left[1:] + left[:1]
    right = right[1:] + right[:1]
    key = left + right
    return permutation(P8, key)

def generate_second(left, right):
    left = left[3:] + left[:3]
    right = right[3:] + right[:3]
    key = left + right
    return permutation(P8, key)

def transform(right, key):
    extended = permutation(E, right)
    print("Extended Permutation: ", extended)
    xor_cipher = bin(int(extended, 2) ^ int(key, 2))[2:].zfill(8)
    print("After applying xor with round key ", xor_cipher)
    xor_left = xor_cipher[:4]
    xor_right = xor_cipher[4:]
    new_left = Sbox(xor_left, S0)
    new_right = Sbox(xor_right, S1)
    print("After applying S-box ")
    print("Left: S0= ", new_left)
    print("Right: S1= ", new_right)
    p4permute = permutation(P4, new_left + new_right)
    print("After applying P4 permutation ", p4permute)
    return p4permute 

def Sbox(data, box):
    row = int(data[0] + data[3], 2)
    column = int(data[1] + data[2], 2)
    return bin(box[row][column])[2:].zfill(2)   

def encrypt(left, right, key):
    cipher = int(left, 2) ^ int(transform(right, key), 2)
    print("After applying final xor= ", bin(cipher)[2:].zfill(4))
    return right, bin(cipher)[2:].zfill(4)

def decrypt(left, right, key):
    plain = int(left, 2) ^ int(transform(right, key), 2)
    print("After applying final xor= ", bin(plain)[2:].zfill(4))
    return right, bin(plain)[2:].zfill(4)


#User Input

key = "1010000010"
plaintext = "01110010"


userInput = False


if userInput == True:
    print("Start the S-DES algorithim.")
    key = input("Enter a 10-bit key: ")
    if len(key) != 10:
        raise Exception("Check the input")


    plaintext = input("Enter 8-bit plaintext: ")
    if len(plaintext) != 8:
        raise Exception("Check the input")


#Encryption Block

print("Input KEY: ", key)
print("Input PLAINTEXT: ", plaintext)

p10key = permutation(P10, key)
print("\nAfter applying permutation P10 on KEY: ",p10key)


print("\nAfter split")
left_key = p10key[:len(p10key)//2]
right_key = p10key[len(p10key)//2:]
print("Left key =: ",left_key,"   Right key =: ",right_key)



first_key = generate_first(left_key, right_key)
second_key = generate_second(left_key, right_key)
print("\nFirst key K1 =: ",first_key)
print("Second key K2=: ",second_key)


print("Encrypt the message")
initial_permutation = permutation(IP, plaintext)
print("Initial Permutation =: ",initial_permutation)

print("\nEncryption Function 1 ")
print("IP Split ")

left_data = initial_permutation[:len(initial_permutation)//2]
right_data = initial_permutation[len(initial_permutation)//2:]
print("Left data =: ",left_data)
print("Right data =: ",right_data)

left, right = encrypt(left_data, right_data, first_key)
print("\nEncrypted data =: ",left+right)


print("\nEncryption Function 2 ")
right, left  = encrypt(left, right, second_key)
print("Encrypted data =: ",left+right)

cipheredText= permutation(IPi, left + right)
print("\nCiphertext =: ",  cipheredText )


#Decryption Block

print("Input KEY: ", key)
print("Above CipherText: ", cipheredText)

p10key = permutation(P10, key)
print("\nAfter applying permutation P10 on KEY: ",p10key)


print("\nAfter split")
left_key = p10key[:len(p10key)//2]
right_key = p10key[len(p10key)//2:]
print("Left key =: ",left_key,"   Right key =: ",right_key)



first_key = generate_first(left_key, right_key)
second_key = generate_second(left_key, right_key)
print("\nFirst key K1 =: ",first_key)
print("Second key K2=: ",second_key)


print("\nDecrypt the message")
initial_permutation = permutation(IP, cipheredText)
print("Initial Permutation =: ",initial_permutation)

print("\nDecryption Function 1 ")
print("IP Split ")
left_data = initial_permutation[:len(initial_permutation)//2]
right_data = initial_permutation[len(initial_permutation)//2:]
print("Left data =: ",left_data)
print("Right data =: ",right_data)

left, right = decrypt(left_data, right_data, second_key)
print("Decrypted data =: ",left+right)

print("\nDecryption Function 2 ")
right,left,    = decrypt(left, right, first_key)
print("Decrypted data =: ",left+right)

print("\nPlain text =: ", permutation(IPi, left + right))





