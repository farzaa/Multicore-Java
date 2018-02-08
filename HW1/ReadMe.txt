Hello Sir Cook!

To run this, just do:

javac Stack.java StackMain.java && java StackMain

Instead of please explaining all my thoughts here, please refer to the comments in the code.
I think the comments + code are much easier to follow then just a big explanation here.

My main function spawns some threads, then assigns jobs like push and pop to each of those threads, and at the end when
all threads are done I compare if stack.numOps == the number of operations I actually passed it. By checking
that these two numbers are equal we can be sure that the stack went through the proper number of operations.

Feel free to change:
THREAD_COUNT and OPERATIONS_PER_THREAD to whatever numbers you'd like in the main!
