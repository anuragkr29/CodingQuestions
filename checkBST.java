/*  The Node class implements a class that check if a given Binary Tree is a Binary Search Tree*/
class Node{
		int data;
		Node left , right;
		Node(int d , Node l , Node r){
			this.data = d;
			this.left = l;
			this.right = r;
		}
	}
public class checkBST {
	
	public static boolean isBST(Node root){
		return isValidBST(root , Integer.MIN_VALUE , Integer.MAX_VALUE);
	}
	private static boolean isValidBST(Node node, int minValue, int maxValue) {
		if(node == null)
			return true;
		else
			return node.data > minValue && node.data<maxValue && isValidBST(node.left, minValue, node.data) &&
					isValidBST(node.right, node.data, maxValue);
	}
	private Node root;
	public static void main(String[] args) {
		Node tree = new Node(15, null, null);
		tree.left = new Node(12,null,null);
		tree.right = new Node(18,null,null);
		tree.left.left = new Node(10,null,null);
		tree.left.right = new Node(13,null,null);
		
		System.out.println("The tree is a BST " + isBST(tree));
	}
}
