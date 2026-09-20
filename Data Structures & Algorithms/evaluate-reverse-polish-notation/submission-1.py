class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {'+', '-', '*', '/'}
        stack = []
        ans = 0

        for token in tokens:
            if token in operations:
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    ans = b + a
                elif token == '-':
                    ans = b - a
                elif token == '*':
                    ans = b * a
                elif token == '/':
                    ans = int(b / a)
 
                stack.append(ans)
            else:
                stack.append(int(token)) 
        
        return stack[0]