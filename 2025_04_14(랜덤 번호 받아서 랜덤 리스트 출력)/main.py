
""" "토끼","강아지","고양이","양","소","쥐"가 인덱스인 리스트를 생성한다
input함수를 사용해서 입력값이 시작인 경우엔 반복문 탈출하는 함수를 생성한다 

1~6까지 랜덤한 숫자를 만드는 함수를 생성한다 

2번째 단계에서 생성된 랜덤 숫자를 매개변수로 받아 
리스트 슬라이싱을 통해 숫자에 맞는 동물을 출력하는 함수를 만든다
추가적으로 오늘 날짜/시간을 출력하는 문구를 집어넣는다.


"""





from data import random_generate
from data import animal
from data import check_input # 처음에 data라는 폴더에서 만든 함수들을 가져와야한다
                            # py파일 한곳에 함수 정리해서 불러와도 되는듯
import time
def main():
    check_input()
    x = random_generate()
    print(animal(x))
    print('오늘은',time.strftime('%Y년 %m월 %d일이고'),'시간은',time.strftime('%H시 %M분입니다'))
if __name__ == "__main__":
    main() # 40,41번 구문대신 단순히 main()만 써도 실행되지만 다른 py에서 불러올 경우도 있기에 무조건적으로 두 코드는 쓰자



ex = ['토끼','강아지','고양이','양','소','쥐']

import random 
import time

def check_input():
    x = input('텍스트를 입력하세요')
    return x

def generate_num():
    y = random.randint(1,6)
    return y

def define_animal(x):
    return ex[x-1]
    

while True:
    word =check_input()
    if word == '시작':
        break
y = generate_num()
print(define_animal(y))
print('오늘은',time.strftime('%Y년 %m월 %d일이고'),'시간은',time.strftime('%H시 %M분입니다'))


'''ssd
'''


import random
import time

class quiz:
    def __init__(self): # 처음 시작은 무조건 이 함수로 > 자동으로 실행되는 함수래
        self.animal_list = ['토끼','강아지','고양이','양','소','쥐'] # 변수앞에 self를 붙이는 이유는 여러번 사용할 수 있으니까 각각 다른 값을 정의하기 위해 self를 사용
                                                                    # > 다른 함수에서도 접근하려면 이걸 붙여야한대
        self.input = '' # 입력값이 여러개 들어오니까 일단 초기화? > 입력을 저장해두는 변수래
    def random_generate(self): # 함수에서는 빈 매개변수엿어도, 클래스에서는 무조건 self를 써야한다 만약 빈 매개변수가 아닌 다른 매개변수가 있다면 (self,매개변수)로 써야함
        self.num = random.randint(1,6)
        return self.num 
    def check_input(self):
        while True:
            self.input = input('텍스트를 입력하세요')
            if self.input =='시작':
                print('오늘은',time.strftime('%Y년 %m월 %d일이고'),'시간은',time.strftime('%H시 %M분입니다'))
                break
    def animal(self, var):  
        print(self.animal_list[var-1])
        """random_generate함수에서 가져온값을 사용하는데, 만약 매개변수에 text없이 사용하고 싶다면 
        self.animal_list[a-1]을 > self.animal_list[self.x-1]로 바꾸기만 하면 된다"""


if __name__ == "__main__": # 클래스 역시 함수와 마찬가지로 다른 py에서 사용될 수 있으니 이 문장은 꼭 쓰자
    game = quiz()             # 여기서 클래스를 정의한다 변수처럼 > 객체를 만드는거래 그리고 만든 객체는 변수처럼 쓸 수 있대
    game.check_input()        # 95번부터 97번까지는 내가 불러온 클래스에서 원하는 기능만 뽑아 쓸 수 있다(전부 다 안 써도 될듯?)
    zzz = game.random_generate() # 원하는 기능만 뽑아 쓸 수 있어 모듈화래
    game.animal(zzz)           






from data import random_generate
from data import animal
from data import check_input 
from data import random_genlist # 같은데서 임포트 헸으니 한줄로 불러와도 된다다

class quiz():
    def __init__(self):
        self.ran_list=[]
        self.data=[] 
        check_input()
        # self.num = random_generate() # 그냥 숫자 하나 받아서 할땐 이걸로
        self.ran_list=random_genlist(6)    
        for self.i,self.b in enumerate(self.ran_list): # self.data = [animal(b) for b in self.ran_list] gpt는 이거 추천해주네
            self.data.append(animal(self.b))
        #__init__함수는 리턴을 사용 못함

if __name__=='__main__':
    kkk=quiz()
    print(kkk.data)
    



### gpt가 추천해준 버전 ㅈㄴ 간결하네;;
from data import random_generate, animal, check_input, random_genlist

class Quiz:
    def __init__(self):
        check_input()
        self.data = [animal(n) for n in random_genlist(6)]

if __name__ == "__main__":
    game = Quiz()
    print("결과:", game.data)
