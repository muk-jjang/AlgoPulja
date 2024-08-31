'''접근방법
배달을 뒤에서부터 시작해야함 
-> 왜냐하면 배송을 다하고 다시 물류센터로 돌아가야하는데 앞에서 시작하는 경우는 점차 거리가 멀어지는 곳에서의 2곱의 거리 형태가 나옴
뒤에서부터 시작하면 점차 짧아지는 거리 2곱으로 나옴

1. 리스트를 뒤집어서 거리가 먼 곳부터 고려해준다
2. 총 배달해야하는 것과 수거해야하는 것을 저장해주고 해당 부분을 해결할 때까지 물류센터 왕복

 
'''

def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    delivery = 0
    pickup = 0

    for i in range(n):
        delivery += deliveries[i]
        pickup += pickups[i]

        #먼 곳부터 다 해결
        while delivery>0 or pickup> 0:
            delivery -= cap
            pickup -= cap
            answer += (n-i)*2 #뒤에서부터 시작하기 때문

    return answer


cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups = [0, 2, 0, 1, 0, 2, 0]

print(solution(cap, n, deliveries, pickups))