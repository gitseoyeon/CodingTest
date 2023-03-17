n = int(input()) # 입력받은 수를 정수형으로 바꿔준다

count = 0 # 출력할 거스름돈 변수 초기화

n = 1000 - n # 거스름돈 금액

for i in [500, 100, 50, 10, 5, 1]: # for문을 이용해 리스트에 있는 수를 차례로 사용
    count += n // i # 거스름돈 금액과 리스트 순으로 나열된 수를 차례로 나누어 몫을 구함 
    n %= i # 거스름돈 금액과 리스트에 있는 수들을 나누고 그 나머지 값을 구함

print(count) # 결과값 출력
