//생성된 정점 -> 나가는건 2개이상이고 들어오는건 없다
//막대-> 들어오는 간선이 없는 정점이랑, 나가는 간선이 없는 정점 하나씩 존재. 나머지는 모두 들어오는, 나가는 간선 하나씩 가짐.
//도넛-> 나가는 간선, 들어오는 간선 한개씩 존재
//8자-> 1개 정점은 각각 2개씩 들어오는거 나가는거 간선 존재
//      나머지 정점들은 각각 1개씩 들어오는, 나가는 간선 존재
/**
 * 각 특징으로 찾으려다 보니 막대와 8자는 찾기 쉬웟는데 막상 도넛은 루프 사용해서 풀어보니 계속 무한루프 걸려서 실패
 * 문제에서 왜 생성된 정점? 이걸 굳이 구하지? 라는 생각하고 또 계속 이 점이 문제에서 언급되는걸 생각해보니
 * 중심 정점으로 파생되오는 간선이 곧 그래프 총 갯수인것을 깨달음
 * 도넛 처리 완료
 */
//생성 정점 찾고난 후에 정점과 연결된 간선들을 모두 지우면 우리가 찾으려는 그래프의 총개수이다.
//나가는 간선 없는거 정점 개수 == 막대 개수
// 2개 들어오고 2개 나가는 간선이 존재하는 정점 찾기-> 8자
//전체에서 두개 뺴면 나옴.

//edges[2,3] : 2->3

class Solution {
    public int[] solution(int[][] edges) {

        int[] answer = new int[4];
        Map<Integer, Integer> in = new HashMap<>();
        Map<Integer, Integer> out = new HashMap<>();


        for (int[] edge : edges) {   // 각각 문제 예시들 대입
            if (out.containsKey(edge[0])) {
                int currentCount = out.get(edge[0]);
                out.put(edge[0], currentCount + 1);
            } else {
                out.put(edge[0], 1);
            }

            if (in.containsKey(edge[1])) {
                int currentCount = in.get(edge[1]);
                in.put(edge[1], currentCount + 1);
            } else {
                in.put(edge[1], 1);
            }

        }

       for (int i : out.keySet()) {
            if (out.get(i) >= 2) { // 2개 이상나가고
                if (!in.containsKey(i)) {  // 들어오는 간선이 없으면
                    answer[0] = i;     // 생성 정점!!
                } else {              //들어오는 간선 존재하면
                    answer[3] += 1;  // 8자
                }
            }
        }

        for (int i : in.keySet()) {    //들어오는 정점 중에
            if (!out.containsKey(i)) {  //나가는 정점에 포함되어 있지 않으면
                answer[2] += 1;    // 막대
            }
        }
        answer[1] = out.get(answer[0]) - answer[2] - answer[3];
        return answer;
    }


}
