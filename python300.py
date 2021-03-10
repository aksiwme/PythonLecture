# 사용자로부터 값을 입력 받은 후 해당 값에 20을 더한 값을 출력하라.
# 단 사용자가 입력한 값과 20을 더한 값이 255를 초과하는 경우 255를 출력해야 한다.
num = int(input())
if num + 20 > 255:
    num = 255
else:
    num = num + 20
print(num)

# 사용자로부터 값을 입력 받은 후 해당 값에 20을 뺀 값을 출력하라.
# 단, 출력 값의 범위는 0 ~ 255이다.
# (결과값이 0보다 작을 경우 0, 255 보다 클 경우 255를 출력해야 한다.)
num = int(input())
if num - 20 < 0:
    num = 0
elif num - 20 > 255:
    num = 255
else:
    num = num - 20
print(num)

# 년도를 입력하면 윤년인지 아닌지를 출력하는 프로그램을 작성하라.
year = int(input())

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("{0}년은 윤년입니다.".format(year))
else:
    print("{0}년은 윤년이 아닙니다.".format(year))

# 리스트에 4개의 정수 [3, -20, -3, 44] 가 저장되어 있다.
# For 문을 사용하여 리스트의 음수만을 출력하는 프로그램을 작성하라.
givenList = [3, -20, -3, 44]

for i in givenList:
    if i < 0:
        print(i)

# 리스트에 4개의 정수 [3, 100, 23, 44] 가 저장되어 있다.
# For 문을 사용하여 3의 배수만을 출력하는 프로그램을 작성하라.
givenList = [3, 100, 23, 44]

for i in givenList:
    if i % 3 == 0:
        print(i)

# 다음 리스트 [13, 21, 12, 14, 30, 18]에서
# 20보다 작은 3의 배수를 출력하는 프로그램을 for문을 사용하여 작성하라.
givenList = [13, 21, 12, 14, 30, 18]

for i in givenList:
    if (i < 20) and (i % 3 == 0):
        print(i)

# while 문을 사용하여 ‘hello world’를  10번 출력하는 프로그램을 작성하라.
# 단, 반복 횟수도 같이 출력되어야 함.
i = 1

while i <= 10:
    print("hello world - {0}".format(i))
    i = i + 1

# 위 프로그램에서 반복 횟수가 10부터 거꾸로 출력되도록 변경하라
i = 10

while i >= 1:
    print("hello world - {0}".format(i))
    i = i - 1

# while 문을 사용하여 1 부터 10까지의 숫자 중 홀수만을 출력하는 프로그램을 작성하라
i = 1
while i <= 10:
    if i % 2 == 1:
        print(i)
    i = i+1

# 초항 A1 = 1 이고, 공차 d = 4인 등차수열 An 에 대하여
# 100을 넘지 않는 최대 An의 값과 그 때의 n 을 구하라.
d = 4
n = 1
An = d * n - 3  # A1

while An < 100:
    n = n + 1
    An = An + d

# 100 이상일 때 루프를 빠져나오기 때문에 이전 항이 정답
n = n - 1
An = An - d
print("100을 넘지않는 최대 An은 {0}항이고, 값은 {1}이다.".format(n, An))

# 커피 자판기
quantity = 10
coffeePrice = 300

while quantity > 0:
    # 돈 입력을 기다림
    money = int(input("금액을 입력해 주세요: "))

    if money >= coffeePrice:
        print("커피를 판매 합니다.")
        print("거스름 돈은 {0}원 입니다.".format(money - coffeePrice))
        quantity = quantity - 1     # 팔았으니까 한 잔 뺌

    else:
        print("{0}원 이상의 금액을 입력해주세요.".format(coffeePrice))
        print("남은 수량은 {0}잔 입니다.".format(quantity))

print("남은 커피가 없습니다. 판매를 종료합니다.")
