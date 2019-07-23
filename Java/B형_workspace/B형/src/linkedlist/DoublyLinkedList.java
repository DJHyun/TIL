package linkedlist;

public class DoublyLinkedList {

	private Node header;
	private int size;

	public DoublyLinkedList() {
		header = new Node(null);
		size = 0;
	}

	private class Node {
		private Object data;
		private Node previousNode;
		private Node nextNode;

		Node(Object data) {
			this.data = data;
			this.previousNode = null;
			this.nextNode = null;
		}
	}

	public Node getNode(int index) {
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException("index 넘어갔다");
		}

		Node node = header;

//		for (int i = 0; i <= index; i++) {
//			node = node.nextNode;
//		}
		if (index < (size / 2)) {
			for (int i = 0; i <= index; i++) {
				node = node.nextNode;
			}
		} else {
			for (int i = size; i > index; i--) {
				node = node.previousNode;
			}
		}

		return node;
	}

	public void addFirst(Object data) {
		Node newNode = new Node(data);

		newNode.nextNode = header.nextNode;

		if (header.nextNode != null) {
			header.nextNode.previousNode = newNode;
		} else {
			header.previousNode = newNode;
		}

		header.nextNode = newNode;
		size++;
	}

	public void add(Object data, int index) {
		if (index == 0) {
			addFirst(data);
			return;
		}
		Node previous = getNode(index - 1);
		Node next = previous.nextNode;

		Node newNode = new Node(data);

		previous.nextNode = newNode;
		newNode.previousNode = previous;
		newNode.nextNode = next;

		if (newNode.nextNode != null) {
			next.previousNode = newNode;
		} else {
			header.previousNode = newNode;
		}
		size++;
	}

	public Node removeFirst() {
		Node firstNode = header.nextNode;
		header.nextNode = firstNode.nextNode;
		if (header.nextNode != null) {
			firstNode.nextNode.previousNode = null;
		} else {
			header.previousNode = null;
		}
		size--;
		return firstNode;
	}

	public Node remove(int index) {
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException("index 넘어감");
		} else if (index == 0) {
			return removeFirst();
		}
		Node removeNode = getNode(index);
		Node previousNode = removeNode.previousNode;
		Node nextNode = removeNode.nextNode;

		previousNode.nextNode = nextNode;
		if (nextNode != null) {
			nextNode.previousNode = previousNode;
		} else {
			header.previousNode = previousNode;
		}
		size--;
		return removeNode;
	}

	public static void main(String[] args) {
		DoublyLinkedList test = new DoublyLinkedList();

		test.addFirst("1번");
		test.addFirst("2번");
		test.addFirst("3번");
		test.add("1.5번", 2);
		test.remove(2);
		test.removeFirst();
		for (int i = 0; i < test.size; i++) {
			System.out.println(test.getNode(i).data);
		}

	}
}
