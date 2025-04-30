
from .function1 import random_generate 
''' 함수 안에서 다른 함수 불러와도 상관없 
함수내에 클래스 불러와도 상관없
내가 만든것처럼 하위 디렉토리에 함수를 넣은 경우엔 .function1이런식으로 
사용하는게 좋지만, 걍 .없이 실행해도 가능
'''

def animal(a):
    a = ["토끼",'강아지','고양이','양','소','쥐']
    y = random_generate()  
    z = y-1
    return a[z]



