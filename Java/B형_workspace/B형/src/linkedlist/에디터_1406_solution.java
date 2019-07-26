// baekjoon source = "https://www.acmicpc.net/problem/1406"
package linkedlist;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class ¿¡µðÅÍ_1406_solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		char[] arr = br.readLine().toCharArray();
		List<Character> list = new LinkedList<>();
		ListIterator<Character> iter = list.listIterator(list.size());
		int n = Integer.parseInt(br.readLine());

		for (int i = 0; i < arr.length; i++) {
			iter.add(arr[i]);
		}

		for (int i = 0; i < n; i++) {
	
			StringTokenizer st = new StringTokenizer(br.readLine());
			switch (st.nextToken()) {
			case "P":
				iter.add(st.nextToken().charAt(0));
				break;
			case "L":
				if(iter.hasPrevious()) iter.previous();
				break;
			case "D":
				if(iter.hasNext()) iter.next();
				break;
			case "B":
				if(iter.hasPrevious()) {
					iter.previous();
					iter.remove();
				}
			}

		}
		
		StringBuilder sb = new StringBuilder();
		for(char c : list) {
			sb.append(c);
		}

		bw.write(sb+"");
		bw.flush();

	}
}
