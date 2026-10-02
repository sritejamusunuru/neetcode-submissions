class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+":
                new_score = stack[-1] + stack[-2]
                stack.append(new_score)
            elif operations[i] == "D":
                new_score = 2 * stack[-1]
                stack.append(new_score)
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(int(operations[i]))
        return sum(stack)
        