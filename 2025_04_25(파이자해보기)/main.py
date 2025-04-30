price = []
input_line = input() # 가격을 입력?
price.append(input_line)
print(sum(price))




t = [1,2,3]
t_max = int(max(t))
print(t_max)
for k in t:
    t[3] = t_max/2
    print(t)

print(max(t))



b = int(input()) #703 
c= list(int(input()))
for i in range(len(c)): #1292 1274 1546
    max_price = int(max(c))

if max_price >= b:
    max_index = c.index(max_price)
    c[max_index] = max_price/2
else:
    pass
print(sum(c))



def coupon():
    num, coupon_price = map(int, input().split()) 
    whole_price = list(map(int, input().split())) 

    max_price = max(whole_price)
    if max_price >= coupon_price:
        max_index = whole_price.index(max_price)
        whole_price[max_index] = max_price / 2
    else:
        pass

    print(int(sum(whole_price)))
    return int(sum(whole_price))

coupon()

import math
num = int(input()) 
rain = list(map(int, input().split())) 

avg_sum = 0
for i in rain:
    avg_sum += i

print(math.ceil(avg_sum/num))


h,w,n = map(int, input().split()) 





# 넓이와 세로만큼만 ! 입력을 받아야한다

width, vert = map(int, input().split()) 
for i in range(width):
    for j in range(vert):
        k = map(int, input().split()*j) 
        l = map(int, input().split()*i) 
        print(k)
        print('-'*20)
        print(l)

        if len(k) == width and len(l) == vert:
            print(k[0:width])
            print(l[0:vert])
        else:
            print('잘못 입력')
            break
        
width, vert = map(int, input().split()) 
k = list(input().split()) 
l = list(input().split()) 
print(width)
print(len(k))
print(vert)
print(k)
print(l)
print(width==len(k))