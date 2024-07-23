# 그냥 완전 탐색으로 끝나는 문제였심, 최대 개수가 4의 7승개라 완전탐색해도 문제 없었음. 다음부터 조건 꼼꼼히 읽자
def solution(users, emoticons):
    # 1. 이모플 많이 팔기
        # 최대 판매 개수 구하기
        # 모든 조합 다 구해서 실행하기
    num_emo = len(emoticons)
    discount=[0.1 for _ in range(num_emo)]
    
    high_subscribe=0
    high_sell=0
    while True:
        if discount == [0.4 for _ in range(num_emo)]:
            break
        discount[-1]+=0.1
        for i in range(1,num_emo):
            if discount[-i]==0.5:
                discount[-i]=0.1
                discount[-i-1]+=0.1
        emoticons_price = [emoticons[k]*(1-discount[k]) for k in range(num_emo)]
        # 각 유저별 구매력 확인
        count=0
        total_sell=0
        for min_dis,max_price in users:
            total_price=0
            
            for j in range(num_emo):
                if discount[j]>=(min_dis/100):
                    total_price+=emoticons_price[j]
            # 기준 가격보다 높으면 이모플 count+=1
            if total_price>=max_price:
                count+=1
            # 아닐 경우 판매액에 +
            else:
                total_sell+=total_price
        if count>high_subscribe:
            high_subscribe=count
            high_sell=total_sell
        elif count==high_subscribe and total_sell>high_sell:
            high_sell=total_sell
            
    answer = [high_subscribe,high_sell]

    return answer
