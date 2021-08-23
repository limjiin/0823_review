import random

Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Speical_Character = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=']
Number = [1,2,3,4,5,6,7,8,9,0]

def pw_generator(length):
    password = ''
    for _ in range(length):
        rand_num = random.randint(0,2)
        if rand_num == 0:
            password = password + Alphabet[random.randint(0,len(Alphabet)-1)]
        elif rand_num == 1:
            password = password + str(Number[random.randint(0,len(Number)-1)])
        else:
            password = password + Speical_Character[random.randint(0,len(Speical_Character)-1)]
    
    return password

print(pw_generator(8))
