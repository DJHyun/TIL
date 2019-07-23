package linkedlist;

public class SimpleLinkedList {

	static Node header;
	static int size;

	public class Node {
		Object data;
		Node nextNode;

		Node(Object data) {
			this.data = data;
			this.nextNode = null;
		}
	}

	public SimpleLinkedList() {
		header = new Node(null);
		size = 0;
	}

	public void addNode(Object data) {
		Node newNode = new Node(data);
		newNode.nextNode = header.nextNode;
		header.nextNode = newNode;
		size++;
	}

	public Node getNode(int index) {
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException("ÀÎµ¦½º ³Ñ¾ú´å!");
		}
		Node node = header.nextNode;
		for (int i = 0; i < index; i++) {
			node = node.nextNode;
		}
		return node;
	}
	
	

	public static void main(String[] args) {

		SimpleLinkedList sl = new SimpleLinkedList();
		sl.addNode("µé¾î°¡");
		System.out.println(sl);
		System.out.println(sl.getNode(0).data);

	}

}
