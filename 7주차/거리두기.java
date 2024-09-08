import java.util.LinkedList;
import java.util.Queue;

class 거리두기_확인하기 {
    public static int[] solution(String[][] places) {
        int[] answer = new int[places.length];

        for (int i = 0; i < places.length; i++) {
            String[] p = places[i];
            if (checkPlace(p)) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        return answer;
    }

    private static boolean checkPlace(String[] p) {  //규칙 잘 지켰는지
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (p[i].charAt(j) == 'P') {
                    if (!isSafe(i, j, p)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    private static boolean isSafe(int a, int b, String[] p) {
        int[] dx = { -1, 1, 0, 0 };
        int[] dy = { 0, 0, -1, 1 };

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] { a, b });

        while (!queue.isEmpty()) {
            int[] position = queue.poll();
            int px = position[0];
            int py = position[1];

            for (int i = 0; i < 4; i++) {
                int x = px + dx[i];
                int y = py + dy[i];

                if (x < 0 || y < 0 || x >= 5 || y >= 5 || (x == a && y == b)) {
                    continue;
                }

                int distance = Math.abs(x - a) + Math.abs(y - b);

                if (p[x].charAt(y) == 'P' && distance <= 2) {
                    return false;
                } else if (p[x].charAt(y) == 'O' && distance < 2) {
                    queue.offer(new int[] { x, y });
                }
            }
        }
        return true;
    }
}
