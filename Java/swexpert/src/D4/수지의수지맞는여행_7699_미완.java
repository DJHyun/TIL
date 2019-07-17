//sw expert source = "www.swexpertacademy.com/7829"
package D4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;

public class 수지의수지맞는여행_7699_미완 implements Cloneable {
	static int R, C, cnt;
	static String[][] arr;
	static Map<String, List<Integer>> map;
	static int[] dx = { 0, 0, 1, -1 };
	static int[] dy = { 1, -1, 0, 0 };
	static String[][] visited;

	static boolean check(int x, int y) {
		if (x < 0 || x > R - 1)
			return false;
		if (y < 0 || y > C - 1)
			return false;
		if (map.containsKey(arr[x][y])) {
			for (int i = 0; i < map.get(arr[x][y]).size(); i++) {
				if (map.get(arr[x][y]).get(i) < cnt) {
					return false;
				}
			}
		}
		return true;
	}

	static void bfs(int a, int b) {
		
		Queue<int[]> tq = new LinkedList<>();
		Queue<int[]> q = new LinkedList<>();
		Iterator<int[]> it = tq.iterator();
		
		tq.add(new int[] { a, b });
		cnt = 1;
		map.put(arr[a][b], new ArrayList());
		map.get(arr[a][b]).add(cnt);

		while (!tq.isEmpty()) {
			
			System.out.println(q + " " + tq);
			while (!q.isEmpty()) {

				for (int[] i : q) {
					System.out.print(Arrays.toString(i) + " ");
				}
				System.out.println(q.size());

				System.out.println(map);
				int[] t = q.poll();
				for (int i = 0; i < 4; i++) {
					int tx = t[0] + dx[i];
					int ty = t[1] + dy[i];
					if (check(tx, ty)) {
						tq.add(new int[] { tx, ty });
						if (map.containsKey(arr[tx][ty])) {
							map.get(arr[tx][ty]).add(cnt);
						} else {
							map.put(arr[tx][ty], new ArrayList());
							map.get(arr[tx][ty]).add(cnt);
						}
					}
				}
			}
			cnt++;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {
			R = sc.nextInt();
			C = sc.nextInt();
			arr = new String[R][C];
			map = new HashMap<>();
			visited = new String[50][50];
			for (int i = 0; i < R; i++) {
				arr[i] = sc.next().split("");
			}

			bfs(0, 0);
			System.out.println(map);
		}
	}
}
