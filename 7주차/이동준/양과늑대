public class 양과늑대 {
    int[] animal;
    int[][] edge;
    int answer;

    public int solution(int[] info, int[][] edges) {
        answer = 0;
        boolean[] visited = new boolean[info.length];
        animal = info;
        edge = edges;
        dfs(visited, 0, 0, 0);

        return answer;
    }

    private void dfs(boolean[] visited, int idx, int sheep_cnt, int wolf_cnt) {
        visited[idx] = true;

        if (animal[idx] == 0) {
            sheep_cnt++;
            answer = Math.max(answer, sheep_cnt);
        } else {
            wolf_cnt++;
        }

        if (wolf_cnt >= sheep_cnt) {
            return;
        }

        for (int[] ed : edge) {
            if (visited[ed[0]] && !visited[ed[1]]) {
                boolean[] next = new boolean[visited.length];
                for (int i = 0; i < visited.length; i++) {
                    next[i] = visited[i];
                }

                dfs(next, ed[1], sheep_cnt, wolf_cnt);
            }
        }
    }
}
