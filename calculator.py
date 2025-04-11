def calculator():
        num1 = float(input('digite um numero:'))
        op = input("informe a operacação: ")
        num2 = float(input('digite outro: '))

        if op == "+":
                result = num1 + num2    
        elif op == "-":
                result = num1 - num2
        elif op == "/":
                result = num1 / num2
        elif op == "*":
                result = num1 * num2
        else:
                print('operação não reconhecida! ')
        
        print (f'{num1} {op} {num2} = {result}')
calculator()  

