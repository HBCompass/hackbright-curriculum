Trees #1
=======

Introduction
-------
Trees are a way of organizing things hierarchically. Many things can be
represented as a tree for visualization. Many things are _actually_ stored as
trees by their nature. On your system's hard drive, a directory structure is
stored as a tree. HTML and XML files are 'serialized' representations of trees
in a text file. We will be implementing the most basic form of tree (aside from
the degenerate form, the linked list), the binary tree.

A binary tree has the following attributes:

class BinaryTreeNode
    get_left() => BinaryTreeNode
    set_left(BinaryTreeNode)
    get_right() => BinaryTreeNode
    set_right(BinaryTreeNode)
    get_value() => int
    set_value(int)

The value can be an arbitrary number, and the get_left and get_right methods
can return a None.

Because a tree is a nested structure, it is difficult to visualize one in text
mode. However, we do have a few options.

The first option that we will implement is also one of the simplest, a depth
first traversal.

A depth-first traversal visits every node in your tree and prints out the value
of each node. It does this in a very specific order. First, it prints the value
of the current node. Then, if it has a left node, it prints the value there. If
that node also has a left child node, it prints that, too. When it finally
reaches the bottom, ie: there are no more left nodes, then it prints the right
node. Note, this is a variant of escaping the minotaur maze. In the minotaur
maze, we keep our hand on the right wall. If we imagine each junction in the
maze as a node, this is the equivalent of visiting the right-most node first.

Here are some examples:

        5
       / \
      6   7

    print depth_first_traversal(tree)
    => 5 6 7

        2
       / \
      9   1
     /
    8
    depth_first_traversal(tree)
    => 2 9 8 1

        2
       / \
      9   1
     /   / \
    8   3   6
       / \   \
      4   0   5

    depth_first_traversal(tree)
    => 2 9 8 1 3 4 0 6 5

The easiest way to do a depth-first traversal is with a recursive function. It
should print the value of the current node, then call itself on the left, then
right node in order.

It may help you to know that ending a print statement with a comma suppresses
the newline:

    eg:
    print "foo",
    print "bar",
    print "baz"
    => foo bar baz

Description
-------
In exercise11.py, you will find an 'abstract class' named BinaryTreeNode. It is
up to you to fill it in.

You will also need to fill in the depth_first_traversal method. To implement
the behavior described above.

As you do, run the tests to validate whether or not your implementation works.

    py.test -x

This time, the error messages will not guide your implementation. They are only
there to verify that you have done the exercise correctly.

Concepts required:
    * Binary trees
    * Depth first search

Resources:
    * http://interactivepython.org/courselib/static/pythonds/Trees/trees.html
    * http://interactivepython.org/courselib/static/pythonds/Recursion/recursionsimple.html
