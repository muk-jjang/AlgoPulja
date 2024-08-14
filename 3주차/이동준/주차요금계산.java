import java.util.*;

class Solution {
    public static int[] solution(int[] fees, String[] records) {
        Map<String, Integer> park = new HashMap<>();  // 차번호 ,시간8
        // 차번호, 요금 / 차번호 기준 오름차순 정렬
        Map<String, Integer> cost = new TreeMap<>();

        for (String r : records) {
            String[] record = r.split(" ");
            String[] t = record[0].split(":");
            int time = Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
            String num = record[1];
            String in_out = record[2];

            if (in_out.equals("IN")) {
                park.put(num, time);
            } else if (in_out.equals("OUT")) {
                if (!cost.containsKey(num)) { // 처음 들어온 경우
                    cost.put(num, time - park.get(num));
                } else {
                    cost.put(num, cost.get(num) + time - park.get(num));
                }
                park.remove(num);
            }
        }

        // 아직 나가지 않은 차량
        if (!park.isEmpty()) {
            for (String carNum : park.keySet()) {
                int accumulatedTime = cost.getOrDefault(carNum, 0);
                cost.put(carNum, accumulatedTime + (23 * 60 + 59) - park.get(carNum));
            }
        }

        List<Integer> answer = new ArrayList<>(cost.size());
        for (Integer c : cost.values()) {
            int baseTime = fees[0];
            int baseFee = fees[1];
            int unitTime = fees[2];
            int unitFee = fees[3];

            // 요금 = 기본 요금 + ((총 주차 시간 - 기본 시간) / 단위 시간) * 단위 요금
            if (c <= baseTime) {
                answer.add(baseFee);
            } else {
                answer.add(baseFee + (int)Math.ceil((double)(c - baseTime) / unitTime) * unitFee);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
