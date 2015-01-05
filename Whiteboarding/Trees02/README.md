MOAR TREES
=======

Introduction
-------
A very curious application of trees is the concept of a 'parse tree'. Imagine,
for example, trying to write a program to interpret and evaluate the following
string:

    (((3 + 2) * (4 - 1) / 3 + 7) * (1 + (-5 + 6)))

You might start evaluating it from right to left, but the first problem arises
when you hit the first multiplication sign. You can't evaluate the
multiplication until after you've evaluated (4-1)/3 first, so there's a lot of
backtracking.

It turns out that backtracking (using recursion) is something trees do well.
Remember a depth-first-traversal that goes down the left side of a tree:

    def dft(node):
        print node.value
        if node.left:
            dft(node.left)
        if node.right:
            dft(node.right)

When you illustrate how this traverses a tree, you'll notice that it exhibits
an interesting backtracking behavior, where it follows a tree as far as it can,
then starts climbing back up when it can't.

In the same way, we can use that behavior to evaluate a mathematical expression
by first constructing a parse tree.

Consider the following expression: (3 + 2).

This mathematical statement is in 'infix' notation, that is, the operator goes
between the operands. More generally, the format is:

    num1 op num2
    where num1 and num2 are any real numbers, and op is one of + - / *

You'll notice quickly that regardless of the complexity of the statement, an
operator can only have two operands. That is, one number goes on the left, and
one goes on the right. We can exploit this regularity with binary trees.

In our previous example, each node of the binary tree contained a single
number. Now, we're going to modify the restrictions. Each node can now be a
either a number or an operator. If the node's value is an operator, we add the
additional constraint that it must have a left and right child. Each of these
children have the same constraints placed on them.

In the simple case of the expression above, we can translate '(3 + 2)' into the
following tree:

        +
       / \
      3   2

In a slightly more complicated scenario, we have the expression '(4 * 5 + 2)'

        +
       / \
      *   2
     / \
    4   5

We can apply this technique to any arbitrarily large or complex mathematical
expression, and decompose them into a series of nested binary trees.

Using this technique, we can now evaluate the entire tree recursively, which
gives us our backtracking behavior for free:

    def eval(node):
        if is_num(node.value):
            return node.value
        elif node.value == "+":
            return eval(node.left) + eval(node.right)
        elif node.value == "*":
            return eval(node.left) * eval(node.right)
        elif node.value == "/":
            return eval(node.left) / eval(node.right)
        elif node.value == "-":
            return eval(node.left) - eval(node.right)

Description
-------
You will write a piece of code that constructs a parse tree from a string
containing a mathematical expression, correctly interpreting parentheses. You
will use recursion heavily in this project, so you may need to review the the
text on recursion.

In exercise12.py, you will find an implementation of the above 'eval' method,
and a simple implementation of binary trees, as well as some utility functions
to assist you in constructing the binary tree.

Your job is to implement a function, build_parse_tree, that takes in a list of
tokens and produces a parse tree according to the following rules:

    Create an empty node.
    While there are tokens remaining, consume a token from the available input.

    1. If that token is a '(', call build_parse_tree on the remaining input,
    and assign the results of that to the left side of your current node.

    2. If the token is an operator + - / *, set the current node's value to
    that operator, then call build_parse_tree on the remaining input and assign
    the result of that to the right side of your current node.

    3. If the token is a number, set the value of the current node to the
    number (converting it from a string) and return that node.

    4. If the token is a ')', return the current node.

Applying these rules should produce a valid parse tree that can then be fed
into the evaluate_expression() function. If you run exercise12.py, the main function
should output a '24' given the sample input.

It has an example (which you should feel free to modify) of taking an input
string, tokenizing it, parsing the tokens, then evaluating the 'parse tree'.
All these steps are required for the program to run. With the current stub code
in place, the program will print a '5'. 

You do not need to modify anything except the build_parse_tree function, but
feel free to experiment with the other functions available.

Concepts required:
    * Binary trees
    * Recursion

Resources:
    * http://interactivepython.org/courselib/static/pythonds/Trees/bintreeapps.html#parse-tree
    * http://interactivepython.org/courselib/static/pythonds/Recursion/recursionsimple.html#what-is-recursion
