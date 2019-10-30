functions = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':0 }
formula = input("Formula to Evaluate:")
formula = formula.replace(' ','')
print(formula)
answer = ''
stack = [] 
stringAdder = ''
for i in range(len(formula)):
    if(formula[i]==')'):
        top = stack.pop()
        while(top != '('):
            answer+=top
            top=stack.pop()                
    elif(formula[i] not in functions):
        answer += formula[i]
    
    elif(formula[i]=='('):
         stack.append('(')
    else:
        while(len(stack)>0 and functions[formula[i]]<=functions[stack[-1]]):
            answer+=stack.pop()
        stack.append(formula[i])
while(len(stack)>0):
    answer+=stack.pop()

print(answer)
