'''
Created on 28 de mar de 2018

@author: Romulo
'''
def eval_loop():
    while (True):
        expression = str(input())
        if (expression.lower() == "done"):
            break
        print(eval(expression))
        lastExpression = expression
    return print(eval(lastExpression))
if __name__ == '__main__':
    eval_loop()

