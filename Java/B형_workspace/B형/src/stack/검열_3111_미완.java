// baekjoon source = "https://www.acmicpc.net/problem/3111"
package stack;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

//List<Character> list = new ArrayList<>();
//for (int i = 0; i < b.length(); i++) {
//	list.add(b.charAt(i));
//}
//while (true) {
//	boolean flag = false;
//	int index = -1;
//	for (int i = 0; i < list.size() - a.length()+1; i++) {
//		if (list.get(i).equals(' '))
//			continue;
//		String check = "";
//		if (flag) {
//			for (int j = i; j < i + a.length(); j++) {
//				check += list.get(j);
//			}
//			if (a.equals(check)) {
//				index = i;
//			}
//
//		} else {
//			for (int j = i; j < i + a.length(); j++) {
//				check += list.get(j);
//			}
//			if (a.equals(check)) {
//				flag = true;
//				for (int j = i; j < i + a.length(); j++) {
//					list.set(j, ' ');
//				}
//			}
//		}
//	}
//	if (index != -1) {
//		for (int j = index; j < index + a.length(); j++) {
//			list.set(j, ' ');
//		}
//	}
//	if (!flag)
//		break;
//	int id = 0;
//	while (id < list.size()) {
//		if (list.get(id).equals(' ')) {
//			list.remove(id);
//		}else {
//			id++;
//		}
//	}
//}

public class 검열_3111_미완 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String a = br.readLine();
		String b = br.readLine();

		Stack<String> oneStack = new Stack<>();
		Stack<String> twoStack = new Stack<>();

	}
}
