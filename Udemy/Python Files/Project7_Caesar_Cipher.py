# 
alpha = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

alpha = alpha + alpha

choice = input("Please choose between encode and decode by typing 'encode' and 'decode':\n")

text = input("Please type the message :\n")

text = text.lower()
shift = int(input("Please enter the shift number:\n"))





def encode(plain_text,shift_amount):
    result = ""
    for i in plain_text:
        new_index = alpha.index(i) + shift_amount
        result += alpha[new_index]
    print(f"THe encoded message is {result}")

def decode(plain_text,shift_amount):
    result = ""
    for i in plain_text:
        new_index = alpha.index(i) - shift_amount
        result += alpha[new_index]
    print(f"THe encoded message is {result}")

if choice == 'encode':
    encode(text,shift)
elif choice == 'decode':
    decode(text,shift)