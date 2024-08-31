//결국 문제에서 주어진 배달 , 수거 집들은 모두 처리해야함
//문제 예시해서 가장 먼 지역부터 처리하는 것을 보고 일반화 할 수 있을 지 고민함
//모두 처리하기 해야하므로 앞에꺼 부터 처리하면 거리 최적화에 비효율적임
//가장 마지막꺼 부터 처리하자 -> 후입 선출 Stack을 생각함

import java.util.Stack;

public class Main {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        Stack<Integer> delivery_st = new Stack<>(); //배달 , 수거 해야 할 집 인덱스를 담은 스택
        Stack<Integer> pickup_st = new Stack<>();

        for (int i = 0; i < n; i++) {
            if (deliveries[i] != 0) {
                delivery_st.push(i);
            }
            if (pickups[i] != 0) {
                pickup_st.push(i);
            }
        }

        while (!delivery_st.isEmpty() || !pickup_st.isEmpty()) {
            int deliveryMaxDist = !delivery_st.isEmpty() ? delivery_st.peek() + 1 : 0;
            int pickupMaxDist = !pickup_st.isEmpty() ? pickup_st.peek() + 1 : 0;
            int remainingCap = cap;

            while (!delivery_st.isEmpty() && remainingCap > 0) {
                int idx = delivery_st.pop();
                if (remainingCap >= deliveries[idx]) {    //남은 용량이 현재 인덱스 배달 물량보다 크거나 같으면
                    remainingCap -= deliveries[idx];      // 용량 차감
                } else {
                    deliveries[idx] -= remainingCap;
                    delivery_st.push(idx);                //다시 스택에 추가함. 돌아가서 또 남은거 처리해야하기 떄문
                    break;
                }
            }

            remainingCap = cap;
            while (!pickup_st.isEmpty() && remainingCap > 0) {
                int idx = pickup_st.pop();
                if (remainingCap >= pickups[idx]) {
                    remainingCap -= pickups[idx];
                } else {
                    pickups[idx] -= remainingCap;
                    pickup_st.push(idx);
                    break;
                }
            }

            answer += 2 * Math.max(deliveryMaxDist, pickupMaxDist);   //배달과 픽업 중 더 먼 거리를 왕복 거리로 계산해 더함
        }

        return answer;
    }
}
