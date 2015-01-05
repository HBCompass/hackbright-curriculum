EVEN MORE TREES
=======

Ugh, are we done with trees yet, also, stacks?!

Introduction
-------
You may have noticed that the arithmetic expressions we evaluated were highly
dependent on the existence of parentheses to separate each individual statement
out.

    (((3 + 2) * ((4 - 1) / 3) + 7) * (1 + (-5 + 6)))
(3+2)*3
3+2*3
We need a way to evaluate expressions without the assistance of parentheses.
Fortunately, someone much smarter came up with an algorithm that does exactly
that: the shunting-yard algorithm.

Description
-------
In exercise13.py, (identical to exercise12), you will implement Edsger
Djikstra's shunting yard algorithm, found here:

http://en.wikipedia.org/wiki/Shunting-yard_algorithm

However, instead of outputting the original expression in reverse polish
notation, you will emit a binary parse tree as before. To do that, we will have
to make some modifications to the algorithm as written.

First, we will ignore all mention of function calls, as we will only work with
basic operators and integers.

Second, instead simply putting operator tokens on the output queue, whenever an
operator is going to be moved to the output queue, instead it combines that
operator with the last two elements on the queueand turns it into a binary tree
node and puts the node on the queue.

* While there are tokens to be read:
    * Read a token.
    * If the token is a number, then add it to the output queue.
    * If the token is an operator, o1, then:
        * while there is an operator token, o2, at the top of the stack, and
          - either o1 is left-associative and its precedence is less than or equal to that of o2,
          - or o1 has precedence less than that of o2,
            * pop o2 off the stack, combine it with the last two elements on
              the queue to produce a binary tree node, then push that node onto
              the output queue.
        * push o1 onto the stack.
    * If the token is a left parenthesis, then push it onto the stack.
    * If the token is a right parenthesis:
        * Until the token at the top of the stack is a left parenthesis, 
          pop operators off the stack, combining them with the last 
          two elements on the queue to create a binary tree node and putting
          that node on the stack.
        * Pop the left parenthesis from the stack, but not onto the output queue.
        * If the stack runs out without finding a left parenthesis, 
          then there are mismatched parentheses.
    * When there are no more tokens to read:
        * While there are still operator tokens in the stack:
            * If the operator token on the top of the stack is a parenthesis, 
              then there are mismatched parentheses.
            * Pop the operator off the stack and combine it with the last two
              elements on the output queue to create a binary tree node, then
              push that node onto the queue.
* Return the final node on the output queue.

Concepts required:
    * Binary trees
    * Stacks
    * Queues

Resources:
    * http://interactivepython.org/courselib/static/pythonds/Trees/bintreeapps.html#parse-tree
    * http://en.wikipedia.org/wiki/Shunting-yard_algorithm
