# import random

# my_dict = {}
# def save_dict():
#     i = 0
#     while True:
#         x = input('입력해주세요')
#         if x =='exit'or x=='stop':
#             break
#         else:
#             my_dict[i]=x
#             i+=1
#     print(f'현재까지 딕셔너리에 들어있는 값들은 : {my_dict.items()} 입니다')
#     dust = []
#     for value in my_dict.values():
#         dust.append(value)
#         k = random.randint(0,len(dust)-1)
    
#     try:
#         print(f'내 딕셔너리의 마지막 값은 : {dust[-1]}입니다')
#     except:
#         print(f'내 딕셔너리의 마지막 값은 : {dust[0]}입니다')
#     print(f'내 딕셔너리 중 랜덤한 값은 : {dust[k]}입니다')

# save_dict()



import random

my_dict = {}
def save_dict():
    i = 0
    while True:
        x = input('입력해주세요')
        if x =='exit'or x=='stop':
            if i > 0:  
                break
            else:
                print('아무것도 입력안한 상태에서 종료할 수 없습니다')
        else:
            my_dict[i]=x
            i+=1
    print(f'현재까지 딕셔너리에 들어있는 값들은 : {my_dict.items()} 입니다')
    dust = []
    for value in my_dict.values():
        dust.append(value)
        k = random.randint(0,len(dust)-1)
    
    try:
        print(f'내 딕셔너리의 마지막 값은 : {dust[-1]}입니다')
    except:
        print(f'내 딕셔너리의 마지막 값은 : {dust[0]}입니다')
    print(f'내 딕셔너리 중 랜덤한 값은 : {dust[k]}입니다')

save_dict()








## 전에 만든 함수 가져와서 입력값 받는데에 사용

import sys
import random

sys.path.append(r"C:\coding\2025_04_14\data") 
from function2 import check_input

my_dict = {}
def save_dict():
    i = 0
    while True:
        x = check_input()
        if x =='exit'or x=='stop':
            if i > 0:
                break
            else:
                print('아무것도 입력하지 않은 상태에선 종료할 수 없습니다.')
        else:
            my_dict[i]=x
            i+=1
    print(f'현재까지 딕셔너리에 들어있는 값들은 : {my_dict.items()} 입니다')
    dust = []
    for value in my_dict.values():
        dust.append(value)
        k = random.randint(0,len(dust)-1)
    
    # try:
    #     print(f'내 딕셔너리의 마지막 값은 : {dust[-1]}입니다')
    # except:
    print(f'내 딕셔너리의 마지막 값은 : {dust[-1]}입니다')
    print(f'내 딕셔너리 중 랜덤한 값은 : {dust[k]}입니다')

save_dict()


## gpt가 짠 코드드
import sys
import random

sys.path.append(r"C:\coding\2025_04_14\data")
from function2 import check_input

def save_inputs():
    user_inputs = []
    
    while True:
        user_input = check_input()
        
        if user_input.lower() in ['exit', 'stop']:
            if user_inputs:
                break
            else:
                print('입력된 값이 없습니다. 최소 한 개 이상의 값을 입력하세요.')
                continue

        user_inputs.append(user_input)

    # 딕셔너리로 변환 (인덱스를 키로 사용)
    input_dict = {i: val for i, val in enumerate(user_inputs)}   ## 획기전인 방법이지만 만약 키값을 0,1,2,3,,, 이 아닌 다른걸 쓰고 싶다면 이 코드를 못쓰겟네

    print(f'\n딕셔너리에 들어있는 값들: {input_dict.items()}')
    print(f'딕셔너리의 마지막 값은: {user_inputs[-1]}')
    print(f'딕셔너리에서 랜덤한 값은: {random.choice(user_inputs)}')

save_inputs()





import sys
import random
from collections import Counter


sys.path.append(r"C:\coding\2025_04_14\data") 
from function2 import check_input

my_dict = {}
def save_dict():
    i = 0
    while True:
        x = check_input()
        if x =='exit'or x=='stop':
            if i > 0:
                break
            else:
                print('아무것도 입력하지 않은 상태에선 종료할 수 없습니다.')
        else:
            my_dict[i]=x
            i+=1
    print(f'현재까지 딕셔너리에 들어있는 값들은 : {my_dict.items()} 입니다')
    dust = []

    for value in my_dict.values():
        dust.append(value)
        unique = Counter(dust)
        k = random.randint(0,len(dust)-1)
    
    # try:
    #     print(f'내 딕셔너리의 마지막 값은 : {dust[-1]}입니다')
    # except:
    print(f'내 딕셔너리의 마지막 값은 : {dust[-1]}입니다')
    print(f'내 딕셔너리 중 랜덤한 값은 : {dust[k]}입니다')
    print(f'내 딕셔너리 중 입력된 빈도는 {unique}이고 가장 많이 나온 항목은 {unique.most_common(1)}입니다다')

save_dict()



# 다음 번엔 기능은 죄다 함수로 빼보자 연습연습








