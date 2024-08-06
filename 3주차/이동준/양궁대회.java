
//정확성 테스트 : 10초
//1 ≤ n ≤ 10
//info의 길이 = 11
//[10점,9점.....,1점,0점]
//어피치가 점수를 딴걸 기준으로 해야하나..
//그냥 높은 점수부터 조져야하나..
//기준으로 진행하기에는 일관된 규칙이 안보임
//아무리 생각해도 다 조져야할듯 => dfs
//원트~

class Solution {
    static int N, MAX;
    static int[] arr;
    static int[] answer = {-1}; // 문제 조건때문에.
    public int[] solution(int n, int[] info) {
        N = n;
        MAX = -1;
        arr = new int[11];
        DFS(info, 0, 0);

        return answer;
    }

    //idx는 점수 0~10까지 접근, cnt는 사용한 화살 수
    private static void DFS(int[] apeach, int idx, int cnt) {
        if(idx == 11) { //점수 접근을 다 했으면
            //화살 다 썼는지 확인하고 다 썼으면 점수 계산
            if(cnt == N) {
                int apeach_score = 0, lion_score = 0;
                for(int i = 0; i<11; i++) {
                    if(apeach[i] == 0 && arr[i] == 0) {
                        continue;
                    }
                    if(apeach[i]>=arr[i]) apeach_score += 10-i;
                    else lion_score += 10-i;
                }

                if(lion_score > apeach_score) {
                    //라이언이 가장 큰 차이로 이기는 경우
                    if(lion_score-apeach_score > MAX) {
                        MAX = lion_score-apeach_score;
                        answer = arr.clone();
                    }

                    //최대 치로 우승할 수 있는 방법이 2개 이상 일 경우
                    else if(lion_score-apeach_score == MAX) {
                        for(int i = 10; i>=0; i--) {
                            if(answer[i]<arr[i]) {
                                answer = arr.clone();
                                return;
                            }
                            else if(answer[i]>arr[i]) return;
                        }
                    }
                }
            }
            return;
        }

        //둘다 0으로 점수 받기 포기
        if(apeach[idx] == 0) {
            DFS(apeach, idx+1, cnt);
        }

        //어피치한테 이기기 -> 어피치보다 하나 더 많이 쏘는걸로 최적화.
        if(cnt+1+apeach[idx] <= N) { //그렇기 때문에 다음과 같이 짜면 됨.
            arr[idx] = apeach[idx]+1;
            DFS(apeach, idx+1, cnt+1+apeach[idx]);
            arr[idx] = 0;
        }

        //어피치한테 지기
        if(apeach[idx] != 0) {
            for(int i = 0; i<=apeach[idx]; i++) {
                arr[idx] = i;
                DFS(apeach, idx+1, cnt+i);
                arr[idx] = 0;
            }
        }

    }
}