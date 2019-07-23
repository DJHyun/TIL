// baekjoon source = "https://www.acmicpc.net/problem/1406"
package linkedlist;

import java.util.Scanner;

public class Main {

	private Node header;
	private int size;
	static String arr;

	public Main() {
		header = new Node(null);
		size = 0;
	}

	private class Node {
		private Object data;
		private Node previous;
		private Node next;

		Node(Object data) {
			this.data = data;
			this.previous = null;
			this.next = null;
		}
	}

	public void add() {
		for (int i = arr.length() - 1; i > 0; i--) {
			Node newNode = new Node(arr.charAt(i));
			newNode.next = header.next;
			if (header.next != null) {
				header.next.previous = newNode;
			}else {
				header.previous = newNode;
			}
			header.next = newNode;
			size++;
		}
	}
	
	public Node get(int index) {
		if(index < 0 || index>=size) {
			throw new IndexOutOfBoundsException("³Ñ¾ú´Ù");
		}
		Node node = header;
		if(index > (size/2)) {
			for(int i = 0; i<=index; i++) {
				node = header.next;
			}
		}else {
			for(int i = size; i> index; i--) {
				node = header.previous;
			}
		}
		return node;
	}
	
	
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		arr = sc.nextLine();
		int n = sc.nextInt();
		sc.nextLine();
		for (int i = 0; i < n; i++) {
			String s = sc.nextLine();
			System.out.println(s);
		}
		System.out.println(arr + " " + n + " ");
		Main test = new Main();
		test.add();
		for(int i = 0; i<test.size; i++) {
			System.out.println(test.get(i).data);
		}
	}
}
