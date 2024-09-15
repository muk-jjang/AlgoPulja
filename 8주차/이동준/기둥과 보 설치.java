import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[][] solution(int n, int[][] build_frame) {
        int[][] answer = {};
        boolean[][] piliars = new boolean[n+5][n+5];
        boolean[][] bo = new boolean[n+5][n+5];
        
        for (int[] bf : build_frame) {
            int x = bf[0];
            int y = bf[1];
            int material = bf[2];
            int delete_make = bf[3];

            if (delete_make == 0) { // 삭제 작업
                if (material == 0) { // 기둥 삭제
                    if (piliars[x][y+1]) {
                        if (!((x > 0 && bo[x-1][y+1]) || bo[x][y+1]))
                            continue;
                    }
                    if (bo[x][y+1]) {
                        if (!(piliars[x+1][y] || ((x > 0 && bo[x-1][y+1]) && bo[x+1][y+1])))
                            continue;
                    }
                    if (x > 0 && bo[x-1][y+1]) {
                        if (!(piliars[x-1][y] || ((x > 1 && bo[x-2][y+1]) && bo[x][y+1])))
                            continue;
                    }
                    piliars[x][y] = false;

                } else { // 보 삭제
                    if (piliars[x][y]) {
                        if (!(piliars[x][y-1] || (x > 0 && bo[x-1][y])))
                            continue;
                    }
                    if (piliars[x+1][y]) {
                        if (!(piliars[x+1][y-1] || bo[x+1][y]))
                            continue;
                    }
                    if (bo[x+1][y]) {
                        if (!(piliars[x+1][y-1] || piliars[x+2][y-1]))
                            continue;
                    }
                    if (x > 0 && bo[x-1][y]) {
                        if (!(piliars[x-1][y-1] || piliars[x][y-1]))
                            continue;
                    }
                    bo[x][y] = false;
                }

            } else { // 설치 작업
                if (material == 0) { // 기둥 설치
                    if (y == 0)
                        piliars[x][y] = true;
                    else {
                        if (x > 0 && bo[x-1][y])
                            piliars[x][y] = true;
                        if (bo[x][y])
                            piliars[x][y] = true;
                        if (piliars[x][y-1])
                            piliars[x][y] = true;
                    }
                } else { // 보 설치
                    if (piliars[x+1][y-1] || piliars[x][y-1])
                        bo[x][y] = true;
                    if ((x > 0 && bo[x-1][y]) && bo[x+1][y])
                        bo[x][y] = true;
                }

            }
        }
        
        List<int[]> ansList = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (piliars[i][j]) {
                    ansList.add(new int[]{i, j, 0});
                }
                if (bo[i][j]) {
                    ansList.add(new int[]{i, j, 1});
                }
            }
        }
        
        int[][] answer = new int[ansList.size()][3];
        for (int i = 0; i < ansList.size(); i++) {
            answer[i] = ansList.get(i);
        }

        return answer; 

    }
}
