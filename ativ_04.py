def fourop(n1,n2,op): 
    if (op == '+'):
        return(n1 + n2)
    elif (op == '-'):
        return(n1 - n2)
    elif (op == '*'):
        return(n1 * n2)
    elif (op == '/'):
        return(n1 / n2)
    else:
        return 'error!'
    
firstnumber = float(input('\nInforme o primeiro número: '))
secondnumber = float(input('\nInforme o segundo número: '))
operation = input('\nInforme a operação: ')  

print('\nResultado: ',fourop(firstnumber,secondnumber,operation))
    
