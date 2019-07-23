// baekjoon source = "https://www.acmicpc.net/problem/1158"
package linkedlist;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 조세퍼스문제_1158 {

	private Node header;
	private int size;
	static int n;
	static int k;

	public 조세퍼스문제_1158() {
		header = new Node(-1);
		size = 0;
	}

	private class Node {
		private int data;
		private Node previousNode;
		private Node nextNode;

		Node(int data) {
			this.data = data;
			this.previousNode = null;
			this.nextNode = null;
		}
	}

	public void add(int data) {
		Node node = new Node(data);
		node.nextNode = header.nextNode;
		if (header.nextNode != null) {
			header.nextNode.previousNode = node;
		} else {
			header.previousNode = node;
		}
		header.nextNode = node;
		size++;
	}

	public Node get(int index) {
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException("index 넘어감");
		}
		Node newNode = header;

		for (int i = 0; i <= index; i++) {
			newNode = newNode.nextNode;
		}
		return newNode;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] st = br.readLine().split(" ");
		n = Integer.parseInt(st[0]);
		k = Integer.parseInt(st[1]);

		조세퍼스문제_1158 test = new 조세퍼스문제_1158();

		for (int i = n; i > 0; i--) {
			test.add(i);
		}

		test.get(0).previousNode = test.get(test.size - 1);
		test.get(test.size - 1).nextNode = test.get(0);

		int check = k - 1;
		Node result = test.get(check);
		bw.write("<");
		while (test.size != 0) {
			if (test.size != 1) {
				bw.write(result.data + ", ");
			} else {
				bw.write(result.data + "");
			}
			result.previousNode.nextNode = result.nextNode;
			result.nextNode.previousNode = result.previousNode;
			for(int i = 0; i<k; i++) {
				result = result.nextNode;
			}
			test.size--;
		}
		bw.write(">");
		bw.flush();
	}
}
