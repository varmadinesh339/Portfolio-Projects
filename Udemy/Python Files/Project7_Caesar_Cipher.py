# 
alpha = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

alpha = alpha + alpha

choice = input("Please choose between encode and decode by typing 'encode' and 'decode':\n")

text = input("Please type the message :\n")

text = text.lower()
shift = int(input("Please enter the shift number:\n"))

def code(input_text,shift_amount,ciper_direction):
    result = ""
    if ciper_direction  == 'decode':
        shift_amount *= -1
    for i in input_text :
       result += alpha[alpha.index(i)+ shift_amount]

    print(f'The {ciper_direction}d code is {result}') 

code(input_text=text,shift_amount=shift,ciper_direction=choice)
