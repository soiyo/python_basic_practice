#1_변수
#컴퓨터 입장에서의 변수 : 값이 있는 곳을 가리킴, 메모리에 올려둔다. 변수는 메모리에 올려져 있는 값들을 지적하고 있는 거임(값을 가리키고 있다)
from tkinter import E

#출력
print('터미널창에 보이는 글자')

#변수 설정
a=3 #3이라는 값이 a라는 박스에 들어갔다.
b=2
c=1.3 #변수는 소수 및 문자열도 가능
d='hyeon'
f=True #참, 거짓도 가능 (조건문쓸때 참이면~하고 거짓이면 ~해라 할때 많이 쓰임)

#여러가지 방법으로 출력해보기
print("어디에 쓰임?","제곱:"+str(a**b), "동등하게 3가지로 나뉘어야 할때(나머지0,1,2) or 짝홀판단(나머지1,2):"+str(a%b),"소수:"+str(c),"문자열"+d)
e=3>2 #True False 판단 가능
g=3==2
print(e,g)

