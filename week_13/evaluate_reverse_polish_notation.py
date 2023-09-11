class Solution:
    def add(self, a,b):
        return a+b
    def sub(self, a,b):
        return a-b
    def mul(self, a,b):
        return a*b
    def div(self, a,b):
        return a/b

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] in operators:
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(self.add(operand_1, operand_2))
                elif tokens[i] == "-":
                    stack.append(self.sub(operand_1, operand_2))
                elif tokens[i] == "*":
                    stack.append(self.mul(operand_1, operand_2))
                else:
                    stack.append(self.div(operand_1, operand_2))
            else:
                stack.append(tokens[i])
        return int(stack[0])
        