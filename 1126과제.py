# 몇단을 입력할까요? 를 물어봐서 해당 숫자의 구구단을 출력해주는 함수 
num = int(input("몇단을 입력할까요?: "))

def print_gugu(num):
      for i in range(1, 10):
            print(num, "x", i, "=", num*i)

print_gugu(num)




#터틀로 내가 그릴 수 있는 '가장 멋있는 도형' 그리기
import turtle
import time
turtle.speed(0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for x in range(150):
    turtle.pencolor(colors[x % 6])
    turtle.width(x // 100 + 1)
    turtle.forward(x)
    turtle.left(59)
time.sleep(0)
