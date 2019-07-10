package D4;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class 반장선출_7792 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();
		Map<Character, Integer> map = new HashMap<>();

		for (int t = 1; t <= testCase; t++) {
			String result = "";
			int check = Integer.MIN_VALUE;
			int n = sc.nextInt();
			sc.nextLine();
			for (int i = 0; i < n; i++) {
				map.clear();
				String name = sc.nextLine();
				for (int s = 0; s < name.length(); s++) {
					if (name.charAt(s) == ' ') {
						continue;
					}
					if (!map.containsKey(name.charAt(s))) {
						map.put(name.charAt(s), 1);
					}
				}
				System.out.println(map);
				if (check < map.size()) {
					check = map.size();
					result = name;
				} else if (check == map.size()) {
					int c = result.compareTo(name);
					if (c >= 0) {
						result = name;
					}
				}
			}
			System.out.printf("#%d %s%n", t, result);
		}
	}
}
