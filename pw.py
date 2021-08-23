# Create: Password Generate

import random

Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Speical_Character = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=']
Number = [1,2,3,4,5,6,7,8,9,0]

def pw_generator(length): #길이가 length인 암호를 생성한다
    password = ''
    for _ in range(length): #첫글자부터 랜덤하게 생성하도록 forloop을 돌림
        rand_num = random.randint(0,2) # 0~2중에 랜덤하게 선택해서 0이면 알파벳, 1이면 숫자 ,2면 특수 문자를 생성한다
        if rand_num == 0:
            password = password + Alphabet[random.randint(0,len(Alphabet)-1)]
        elif rand_num == 1:
            password = password + str(Number[random.randint(0,len(Number)-1)])
        else:
            password = password + Speical_Character[random.randint(0,len(Speical_Character)-1)]
    
    return password

print(pw_generator(8)) #최종적으로 만들어진 패스워드

