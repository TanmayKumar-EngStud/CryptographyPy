from os import system
from collections import deque
system('clear')
class Solution:
    def operate(self,i1: int,i2: int, op1: str,op2: str) -> int:
        if op1 == "+" :
            if op2 == "+":
                return "+",i1+i2
            else: 
                x= i2 - i1
                if x < 0:
                    return "-",abs(x)
                else:
                    return "+",x
        elif op1 == "-":
            if op2 == "-":
                return "-",i1+i2
            else:
                x = i1 - i2
                if x < 0:
                    return "-",abs(x)
                else:
                    return "+",x
    
    def solve(self, stack): # This must work well
        i=0
        opMain = ""
        while stack[len(stack)] is not "(":
            if i is not 0:
                stack.append(opMain)
                stack.append(i)
            i1 = int(stack.pop())
            op1 = str(stack.pop())
            if stack[len(stack)] is "(":
                stack.pop()
                stack.append(op1)
                stack.append(i1)
                break
            i2 = int(stack.pop())
            op2 = str(stack.pop())
            opMain,i=self.operate(i1, i2, op1,op2)
        stack.pop() #Removing the opening bracket
        stack.append(i) # Adding the result.
    def solve2(self, stack):
        i=0
        opMain = ""
        while len(stack) is not 0:
            if i is not 0:
                stack.append(opMain)
                stack.append(i)
            i1 = int(stack.pop())
            op1 = str(stack.pop())
            if len(stack) is None:
                if(op1 == "+"):
                    return i1
                else:
                    return -i1
            i2 = int(stack.pop())
            op2 = str(stack.pop())
            opMain,i=self.operate(i1, i2, op1,op2)
        stack.pop() #Removing the opening bracket
        stack.append(i)
    def calculate(self, s: str) -> int:
        ans =0
        longInt=0
        stack = deque()
        
        for i in s:
            if i != " " :
                if i== ")":
                    self.solve(stack)      
               
                elif i == "+" or i == "-":
                    stack.append(str(longInt))
                    stack.append(i)
                    longInt = 0
                else:
                    longInt = longInt*10 + int(i)
        if longInt != 0:
            stack.append(str(longInt))
        ans = self.solve2(stack)
        return ans
ans =Solution().calculate("2-1 + 2")
print(ans)