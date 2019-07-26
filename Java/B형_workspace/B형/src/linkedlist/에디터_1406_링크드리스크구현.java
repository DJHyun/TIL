// baekjoon source = "https://www.acmicpc.net/problem/1406"
package linkedlist;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class 에디터_1406_링크드리스크구현 {

//	private Node header;
//	private int size;
//	static String[] arr;
//
//	public Main() {
//		header = new Node(null);
//		size = 0;
//	}
//
//	private class Node {
//		private Object data;
//		private Node previous;
//		private Node next;
//
//		Node(Object data) {
//			this.data = data;
//			this.previous = null;
//			this.next = null;
//		}
//	}
//
//	public void addFirst() {
//		for (int i = arr.length - 1; i > -1; i--) {
//			Node newNode = new Node(arr[i]);
//			newNode.next = header.next;
//			if (header.next != null) {
//				header.next.previous = newNode;
//			} else {
//				header.previous = newNode;
//			}
//			header.next = newNode;
//			size++;
//			System.out.println(arr[i]);
//		}
//	}
//
//	public void add(int index, Object data) {
//
//		Node newNode = new Node(data);
//		Node previousNode = null;
//		Node nextNode = null;
//
//		if (index != -1) {
//			previousNode = get(index);
//			nextNode = previousNode.next;
//		} else {
//			nextNode = get(0);
//		}
//		
//		if(previousNode != null) {
//			previousNode.next = newNode;
//			newNode.previous = previousNode;
//		}else {
//			header.next = newNode;
//		}
//		if (nextNode != null) {
//			nextNode.previous = newNode;
//			newNode.next = nextNode;
//		} else {
//			header.previous = newNode;
//		}
//		size++;
//	}
//
//	public void remove(int index) {
//		Node node = get(index);
//		Node previousNode = node.previous;
//		Node nextNode = node.next;
//
//		if (previousNode == null) {
//			header.next = nextNode;
//			nextNode = null;
//		} else if (nextNode == null) {
//			header.previous = previousNode;
//			previousNode.next = null;
//		} else {
//			previousNode.next = nextNode;
//			nextNode.previous = previousNode;
//		}
//		size--;
//	}
//
//	public Node get(int index) {
//		if (index < 0 || index >= size) {
//			throw new IndexOutOfBoundsException("넘었다");
//		}
//		Node node = header;
//		if (index < (size / 2)) {
//			for (int i = 0; i <= index; i++) {
//				node = node.next;
//			}
//		} else {
//			for (int i = size; i > index; i--) {
//				node = node.previous;
//			}
//		}
//		return node;
//	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		char[] arr = br.readLine().toCharArray();
//		Main test = new Main();
		LinkedList<Character> li = new LinkedList<>();

//		test.addFirst();
		int n = Integer.parseInt(br.readLine());

//		int cur = test.size;

//		for (int i = 0; i < n; i++) {
//			System.out.println(i);
//			String[] s = br.readLine().split(" ");
//			switch (s[0]) {
//			case "P":
//				test.add(cur - 1, s[1]);
//				cur++;
//				break;
//			case "L":
//				if (cur > 0) {
//					cur--;
//				}
//				break;
//			case "D":
//				if (cur < test.size) {
//					cur++;
//				}
//				break;
//			case "B":
//				if (cur > 0) {
//					test.remove(cur-1);
//					cur--;
//				}
//				break;
//			}
//		}
//		
//		Node result = test.header;
//		for(int i = 0; i<test.size; i++) {
//			result = result.next;
//			bw.write(result.data+"");
//		}
		int i = 0;
		for (i = 0; i < arr.length; i++) {
			li.add(arr[i]);
		}
		int cur = i;
		int liSize = i;
		for (i = 0; i < n; i++) {
			bw.write(i + "\n");
			StringTokenizer s = new StringTokenizer(br.readLine());
			char check = s.nextToken().charAt(0);

			switch (check) {
			case 'P':
				if (cur != 0) {
					li.add(cur, s.nextToken().charAt(0));
				} else {
					li.addFirst(s.nextToken().charAt(0));
				}
				cur++;
				break;
			case 'L':
				if (cur > 0)
					cur--;
				break;
			case 'D':
				if (cur < li.size())
					cur++;
				break;
			case 'B':
				if (cur > 0) {
					li.remove(cur - 1);
					cur--;
				}
				break;
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int j = 0; j < li.size(); j++) {
			sb.append(li.get(j));
		}
		bw.write(sb + "");
		bw.flush();
	}
}
