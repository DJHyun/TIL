//sw expert source = "www.swexpertacademy.com/7465"
package D4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class 창용마을무리의개수_7465 {

	static int n, m;
	static List<ArrayList<Integer>> list;
	static int[] visited;

	static void bfs(int v) {
		Queue<Integer> q = new LinkedList<>();
		q.add(v);
		visited[v] = 1;
		while (!q.isEmpty()) {
			int t = q.poll();

			for (int i = 0; i < list.get(t).size(); i++) {
				if (visited[list.get(t).get(i)] == 0) {
					q.add(list.get(t).get(i));
					visited[list.get(t).get(i)] = 1;
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int t = 1; t <= T; t++) {
			String[] st = br.readLine().split(" ");
			n = Integer.parseInt(st[0]);
			m = Integer.parseInt(st[1]);
			list = new ArrayList<>();
			visited = new int[n + 1];

			for (int i = 0; i <= n; i++) {
				list.add(new ArrayList<>());
			}
			for (int i = 0; i < m; i++) {
				st = br.readLine().split(" ");
				if (st.length == 2) {
					list.get(Integer.parseInt(st[0])).add(Integer.parseInt(st[1]));
					list.get(Integer.parseInt(st[1])).add(Integer.parseInt(st[0]));
				} else {
					list.get(Integer.parseInt(st[0])).add(Integer.parseInt(st[0]));
				}
			}
			int result = 0;
			for (int i = 1; i <= n; i++) {
				if (visited[i] == 0) {
					bfs(i);
					result++;
				}
			}
			System.out.println("#" + t + " " + result);
		} // end of test_case
	}
}
