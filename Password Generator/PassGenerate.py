import random
import array
 
print("GIVEN LENGTH SHOULD BE FIVE OR MORE")
print("GIVEN LENGTH SHOULD BE FIVE OR MORE")
print("||||||||||||||||||||||||||||||||||")
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

# Length of PASSWORD
len = int(input('\nEnter the length of password: '))
 
# declare all characters, symbols, numbers,
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
# combine all
combine = digits + uppercase + lowercase + symbols
 
# randomly select at least one character from each
random_digit = random.choice(digits)
random_upper = random.choice(uppercase)
random_lower = random.choice(lowercase)
random_symbol = random.choice(symbols)
 
# combine the character randomly
# we want a 12-character password and this will give only 4
tpass = random_digit + random_upper + random_lower + random_symbol
 

for x in range(len - 4):
    tpass = tpass + random.choice(combine)
 
    
    tpass_list = array.array('u', tpass)
    random.shuffle(tpass_list)

password = ""
for p in tpass_list:
        password = password + p
         
print(password)