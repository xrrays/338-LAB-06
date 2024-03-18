# generated using chatgpt

# Import the sys module to access command-line arguments
import sys


# Define functions for basic arithmetic operations
def add(a, b):
    """Adds two numbers and returns the sum."""
    return a + b


def subtract(a, b):
    """Subtracts two numbers and returns the difference."""
    return a - b


def multiply(a, b):
    """Multiplies two numbers and returns the product."""
    return a * b


def divide(a, b):
    """Divides two numbers and returns the quotient."""
    return a / b


# Create a dictionary to map operators to their corresponding functions
operands = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


# Define a Node class to represent nodes in the expression tree
class Node:
    def __init__(self, value):
        """
        Initializes a Node object with a value and sets the left and right children to None.

        Args:
            value: The value of the node, which can be a number or an operator.
        """
        self.value = value
        self.left = None
        self.right = None


# Function to build an expression tree from a mathematical expression string
def build_tree(expression):
    """
    Builds an expression tree from a mathematical expression string.

    Args:
        expression: The mathematical expression string.

    Returns:
        The root node of the expression tree.
    """

    tokens = expression.split()  # Split the expression into tokens (numbers and operators)
    stack = []  # Stack to store nodes while building the tree
    parent = None  # Variable to keep track of the parent node

    for token in tokens:
        if token == ')':
            # If token is closing parenthesis, pop right, parent, and left nodes from stack
            # and set the parent's left and right children, then push the parent back on the stack
            right = stack.pop()
            parent = stack.pop()
            left = stack.pop()
            parent.left = left
            parent.right = right
            stack.append(parent)
            continue
        elif token.isdigit():
            # If token is a number, create a Node with the number and push it on the stack
            stack.append(Node(int(token)))
        elif token in '+-*/':
            # If token is an operator, create a Node with the operator and push it on the stack
            node = Node(token)
            stack.append(node)

    # Check if there are exactly 3 elements remaining in the stack (representing a complete root node)
    if len(stack) == 3:
        right = stack.pop()
        parent = stack.pop()
        left = stack.pop()
        parent.left = left
        parent.right = right
        stack.append(parent)

    # Return the root node of the expression tree (the last element in the stack)
    return stack[-1]


# Function to perform a post-order traversal of the expression tree and evaluate the expression
def postorder(node):
    """
    Performs a post-order traversal of the expression tree and evaluates the expression.

    Args:
        node: The current node in the traversal.

    Returns:
        The evaluated result of the expression.
    """

    if node:
        left = postorder(node.left)  # Recursively evaluate the left subtree
        right = postorder(node.right)  # Recursively evaluate the right subtree
        if node.value in operands:  # If the node is an operator
            return int(operands[node.value](left, right))  # Use the corresponding function from the operands dictionary
        else:
            return node.value  # If the node is a number, return its value


# Main function to get the expression from command-line arguments and evaluate it
def main():
    """
    Gets the expression from command-line arguments and evaluates it.
    """

    expression = sys.argv[1]  # Get the expression from the second command-line argument
    root = build_tree(expression)  # Build the expression tree
    print(postorder(root))  # Evaluate the expression and print the result


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
