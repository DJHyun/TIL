// baekjoon source = "https://www.acmicpc.net/problem/5397"
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

public class Å°·Î°Å_5397 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int t = Integer.parseInt(br.readLine());
		for (int T = 0; T < t; T++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			List<Character> list = new LinkedList<>();
			ListIterator<Character> iter = list.listIterator(list.size());
			char[] cmd = st.nextToken().toCharArray();
			for(int i = 0; i<cmd.length; i++) {
				
				switch(cmd[i]) {
				case '<':
					if(iter.hasPrevious()) iter.previous();
					break;
				case '>':
					if(iter.hasNext()) iter.next();
					break;
				case '-':
					if(iter.hasPrevious()) {
						iter.previous();
						iter.remove();
					}
					break;
				default:
					iter.add(cmd[i]);
				}
			}
			
			StringBuilder sb = new StringBuilder();
			for(char c : list) {
				sb.append(c);
			}
			bw.write(sb+"\n");
			bw.flush();
		}
	}
}
