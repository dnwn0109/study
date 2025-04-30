# def check_input():
#     while True:    
#         x = input('텍스트를 입력하세요 > ')
#         if x=='시작':
#             break


# my_dict = {}
# def check_input():
#     i = 0
#     while True:
#         x = input('입력해주세요')
#         if x =='exit'or x=='stop':
#             if i > 0:
#                 break
#             else:
#                 print('아무것도 입력안한 상태에서 종료할 수 없습니다')
#         else:
#             my_dict[i]=x
#             i+=1
#     return my_dict


def check_input():
    x = input("텍스트를 입력하세요 > ")
    return x