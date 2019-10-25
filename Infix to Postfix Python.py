#!/usr/bin/env python
# coding: utf-8

# In[8]:


functions = {'+':1, '-':1, '*':2, '/':2, '^':3}
formula = input("Formula to Evaluate:")
formula = formula.replace(' ','')
answer = ''
stack = [] 
stringAdder = ''
for i in range(len(formula)):
    if(formula[i] not in functions):
        
        if(formula[i]=='('):
            stack.append('(')
        else:
            stringAdder += formula[i]
    else:
        stringAdder[::-1]
        answer += stringAdder+','
        stringAdder=''
        if(len(stack)>0):
            if(stack[-1]==')'):
                while(stack.pop()!='('):
                    answer +=stack.pop()
        
        stack.append(formula[i])

print(answer)
        
    


# In[ ]:




