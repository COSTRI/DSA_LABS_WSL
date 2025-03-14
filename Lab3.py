#1815522
#Write a function to check for balanced parentheses in an expression and evaluate a postfix expression using stacks
 
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def is_empty(self):
        # Return True if the stack is empty, otherwise False
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")  # Raise an error if stack is empty

    def peek(self):
        # Return the top item of the stack without removing it
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")  # Raise an error if stack is empty

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def __str__(self):
        # Return a string representation of the stack
        return str(self.items)




#Function to check balanced parentheses
def is_balanced(expression):
    #Create a stack to keep track of opening parentheses
    stack = Stack()
    #Dictionary to match closing parentheses with their corresponding opening ones
    parentheses = { ')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in parentheses.values(): #if it's an opening parenthesis
            stack.push(char)
        elif char in parentheses.keys(): #if it's a closing parenthesis
            #Check if the stack is empty or the top item doesn't match
            if stack.is_empty() or stack.pop() != parentheses[char]:
                return False
            
    #The expression is balanced if the stack is empty at the end
    return stack.is_empty()




#Function to Evaluate a Postfix Expression using stacks
def evaluate_postfix(expression):
    #create a stack to evaluate the postfix expression
    stack = Stack()
    #set of operators
    operators = {'+', '-', '*', '/'}

    #split the expression into tokens
    for char in expression.split():
        if char.isdigit():
            stack.push(int(char))#push it onto the stack
        elif char in operators: # if the token is an operator
            b = stack.pop() #Pop the top two numbers
            a = stack.pop()
            #perform the operation based on the operator and push the result back unto the stack

            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)

    #The result of the expression is the last item in the stack
    return stack.pop()



#Example of usage
#check balanced parenthesis
expression = "{[()()]}"
print(f"Is the expression {expression} balanced? {is_balanced(expression)}")


#Evaluate postfix expression
postfix_expression = "3 4 + 2 * 7 /"
print(f"The result of the postfix expression '{postfix_expression}' is {evaluate_postfix(postfix_expression)}")