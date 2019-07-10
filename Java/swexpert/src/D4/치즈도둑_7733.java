package D4;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Ä¡ÁîµµµÏ_7733 {

	static int T, N, result, idx, cnt;
	static int[][] arr;
	static int[] dx = { 0, 0, 1, -1 };
	static int[] dy = { 1, -1, 0, 0 };
	static int[][] visited;

	static boolean check(int x, int y) {
		if (x < 0 || x > N - 1)
			return false;
		if (y < 0 || y > N - 1)
			return false;
		if (visited[x][y] == 1)
			return false;
		if (arr[x][y] <= idx)
			return false;
		return true;
	}

	static void bfs(int x, int y) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] { x, y });
		visited[x][y] = 1;
		while (!q.isEmpty()) {
			int tmp[] = q.poll();
			for (int i = 0; i < 4; i++) {
				int tmp_x = tmp[0] + dx[i];
				int tmp_y = tmp[1] + dy[i];
				if (check(tmp_x, tmp_y)) {
					q.add(new int[] { tmp_x, tmp_y });
					visited[tmp_x][tmp_y] = 1;
				}
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		T = sc.nextInt();
		cnt = Integer.MIN_VALUE;
		for (int t = 1; t <= T; t++) {
			N = sc.nextInt();
			arr = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					arr[i][j] = sc.nextInt();
					cnt = Math.max(cnt, arr[i][j]);
				}
			}
			result = 1;
			idx = 1;
			while (idx <= cnt) {
				int chee = 0;
				visited = new int[N][N];
				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						if (arr[i][j] > idx && visited[i][j] == 0) {
							bfs(i, j);
							chee++;
						}
					}
				}
				result = Math.max(result, chee);
				idx++;
			}
			System.out.printf("#%d %d%n", t, result);
		}
	}
}
