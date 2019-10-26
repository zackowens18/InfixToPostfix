functions = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':0 }
formula = input("Formula to Evaluate:")
formula = formula.replace(' ','')
answer = ''
stack = [] 
stringAdder = ''
for i in range(len(formula)):
    if(formula[i] not in functions):
        if(formula[i]==')'):
            top =''
            while(top != '('):
                answer+=top
                top=stack.pop()
        else:
            stringAdder += formula[i]
    else:
        if(formula[i]=='('):
            stack.append('(')
        else:
            while(len(stack)>0 and functions[formula[i]]>=functions[stack[-1]]):
                answer+=stack.pop()
            stack.append(formula[i])
        

print(answer)
        
