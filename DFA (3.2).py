# Santiago Andrés Serrano Vacca		A01734988
# Ana Paula Pedroza Ramírez		    A00830553
# Andrea Catalina Fernández Mena	A01197705
# Thomas Freund Paternostro		    A00831997

# Actividad 3.2: Programando un DFA
# Código compatible con Python 3.10+

expresion = ""

def lexerAritmetico(nombre_archivo):
    global expresion
    print("Token", "Tipo", sep="\t")
    with open(nombre_archivo) as f:
        lines = f.readlines()
        for line in lines:
            expresion = line.replace('\n', "")
            V(expresion)

def V(rem):
    if len(rem) == 0:
        return
    match rem[0]:
        case ' ':
            return V(rem[1:])
        case '.':
            return P(rem[1:])
        case '-':
            return NOR(rem[1:])
        case '=':
            return EQ(rem[1:])
        case '+':
            return S(rem[1:])
        case '*':
            return M(rem[1:])
        case '/':
            return D(rem[1:])
        case '^':
            return POT(rem[1:])
        case '(':
            return SP(rem[1:])
        case ')':
            return EP(rem[1:])
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return N(rem[1:], rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return VAR(rem[1:], rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return VAR(rem[1:], rem[0])

def N(rem, charsTillNow):
    if len(rem) == 0:
        print(charsTillNow, "Entero", sep="\t")
        return
    match rem[0]:
        case ' ':
            print(charsTillNow, "Entero", sep="\t")
            return V(rem[1:])
        case '.':
            return NDE(rem[1:], charsTillNow + rem[0])
        case '-':
            print(charsTillNow, "Entero", sep="\t")
            return R(rem[1:])
        case '=':
            return DEAD(rem[1:], "se intentó usar un operador de asignación después de un entero.")
        case '+':
            print(charsTillNow, "Entero", sep="\t")
            return S(rem[1:])
        case '*':
            print(charsTillNow, "Entero", sep="\t")
            return M(rem[1:])
        case '/':
            print(charsTillNow, "Entero", sep="\t")
            return D(rem[1:])
        case '^':
            print(charsTillNow, "Entero", sep="\t")
            return POT(rem[1:])
        case '(':
            return DEAD(rem[1:], "se intentó poner un paréntesis que abre inmediatamente después de un entero, sin nada de por medio.")
        case ')':
            print(charsTillNow, "Entero", sep="\t")
            return EP(rem[1:])
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return N(rem[1:], charsTillNow+rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return DEAD(rem[1:], "se intentó poner una e después de un entero, sin poner el punto antes.")
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return DEAD(rem[1:], "una variable no puede comenzar con un número.")

def NDE(rem, charsTillNow):
    if len(rem) == 0:
        print(charsTillNow, "Real", sep="\t")
        return
    match rem[0]:
        case ' ':
            print(charsTillNow, "Real", sep="\t")
            return V(rem[1:])
        case '.':
            return DEAD(rem[1:], "no puede haber dos puntos en un solo número.")
        case '-':
            print(charsTillNow, "Real", sep="\t")
            return R(rem[1:])
        case '=':
            return DEAD(rem[1:], "se intentó poner un signo de asignación después de un número.")
        case '+':
            print(charsTillNow, "Real", sep="\t")
            return S(rem[1:])
        case '*':
            print(charsTillNow, "Real", sep="\t")
            return M(rem[1:])
        case '/':
            print(charsTillNow, "Real", sep="\t")
            return D(rem[1:])
        case '^':
            print(charsTillNow, "Real", sep="\t")
            return POT(rem[1:])
        case '(':
            return DEAD(rem[1:], "se intentó poner un paréntesis inmediatamente después de un número, sin nada de por medio.")
        case ')':
            print(charsTillNow, "Real", sep="\t")
            return EP(rem[1:])
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return NDE(rem[1:], charsTillNow + rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return NE(rem[1:], charsTillNow + rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return DEAD(rem[1:], "una variable no puede comenzar con un número.")

def P(rem, charsTillNow="."):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, no se puede terminar con un simple punto.", sep="")
        return
    match rem[0]:
        case ' ':
            return DEAD(rem[1:], "un punto no puede estar solo.")
        case '.':
            return DEAD(rem[1:], "un punto no puede tener otro punto después.")
        case '-':
            return DEAD(rem[1:], "un punto solo no puede tener un signo de resta inmediatamente después.")
        case '=':
            return DEAD(rem[1:], "un punto solo no puede tener un signo de asignación después.")
        case '+':
            return DEAD(rem[1:], "un punto solo no puede tener, inmediatamente después, un símbolo de suma.")
        case '*':
            return DEAD(rem[1:], "un punto solo no puede tener, inmediatamente después, un símbolo de multiplicación.")
        case '/':
            return DEAD(rem[1:], "un punto solo no puede tener, inmediatamente después, un símbolo de división.")
        case '^':
            return DEAD(rem[1:], "un punto solo no puede tener, inmediatamente después, un símbolo de potencia.")
        case '(':
            return DEAD(rem[1:], "un punto solo no puede tener, inmediatamente después, un paréntesis.")
        case ')':
            return DEAD(rem[1:], "un punto solo no puede tener, inmediatamente después, un paréntesis.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return NDE(rem[1:], charsTillNow + rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return DEAD(rem[1:], "un punto no puede tener, inmediatamente después, una e.")
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return DEAD(rem[1:], "una variable no puede comenzar con un punto.")

def NE(rem, charsTillNow):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un número en notación exponencial que no tiene nada después de la E.", sep="")
        return
    match rem[0]:
        case ' ':
            return DEAD(rem[1:], "no se especificó a qué valor se está elevando el número en notación exponencial (no hay nada después de la E).")
        case '.':
            return DEAD(rem[1:], "un número en notación exponencial no puede tener un exponente decimal.")
        case '-':
            return NEN(rem[1:], charsTillNow + rem[0])
        case '=':
            return DEAD(rem[1:], "no se puede poner un símbolo de asignación como exponente de un número en notación exponencial.")
        case '+':
            return DEAD(rem[1:], "no se puede poner un símbolo positivo como exponente de un número en notación exponencial.")
        case '*':
            return DEAD(rem[1:], "no se puede poner un símbolo de multiplicación como exponente de un número en notación exponencial.")
        case '/':
            return DEAD(rem[1:], "no se puede poner un símbolo de división como exponente de un número en notación exponencial.")
        case '^':
            return DEAD(rem[1:], "no se puede poner un símbolo de potencia como exponente de un número en notación exponencial.")
        case '(':
            return DEAD(rem[1:], "el exponente de un número en notación exponencial no puede ir dentro de paréntesis.")
        case ')':
            return DEAD(rem[1:], "el exponente de un número en notación exponencial no puede ser un paréntesis que cierra.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return NENC(rem[1:], charsTillNow + rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return DEAD(rem[1:], "se pusieron dos letras e en un número en notación exponencial.")
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return DEAD(rem[1:], "una variable no puede ser el exponente de un número en notación exponencial.")

def NENC(rem, charsTillNow):
    if len(rem) == 0:
        print(charsTillNow, "Real en notación exponencial", sep="\t")
        return
    match rem[0]:
        case ' ':
            print(charsTillNow, "Real en notación exponencial", sep="\t")
            return V(rem[1:])
        case '.':
            return DEAD(rem[1:], "el exponente de un número en notación exponencial no puede ser decimal.")
        case '-':
            print(charsTillNow, "Real en notación exponencial", sep="\t")
            return R(rem[1:])
        case '=':
            return DEAD(rem[1:], "se intentó poner un símbolo de asignación después de un número.")
        case '+':
            print(charsTillNow, "Real en notación exponencial", sep="\t")
            return S(rem[1:])
        case '*':
            print(charsTillNow, "Real en notación exponencial", sep="\t")
            return M(rem[1:])
        case '/':
            print(charsTillNow, "Real en notación exponencial", sep="\t")
            return D(rem[1:])
        case '^':
            print(charsTillNow, "Real en notación exponencial", sep="\t")
            return POT(rem[1:])
        case '(':
            return DEAD(rem[1:], "se intentó poner un paréntesis después de un número, sin nada de por medio.")
        case ')':
            print(charsTillNow, "Real en notación exponencial", sep="\t")
            return EP(rem[1:])
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return NENC(rem[1:], charsTillNow + rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return DEAD(rem[1:], "un número en notación exponencial no puede tener más de una e.")
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return DEAD(rem[1:], "un número en notación exponencial no puede tener letras (exceptuando la e que denota que está en notación exponencial).")

def NEN(rem, charsTillNow):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un número en notación exponencial que no tiene nada después de la E-.", sep="")
        return
    match rem[0]:
        case ' ':
            return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener espacios.")
        case '.':
            return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener puntos después de la e.")
        case '-':
            return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener más de un símbolo '-'.")
        case '=':
            return DEAD(rem[1:], "hay un signo de asignación dentro de un número en notación exponencial con exponente negativo.")
        case '+':
            return DEAD(rem[1:], "un número en notación exponencial no puede tener un exponente negativo y positivo a la vez.")
        case '*':
            return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener signos de multiplicación dentro de sí mismo.")
        case '/':
            return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener signos de división dentro de sí mismo.")
        case '^':
            return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener signos de exponenciación dentro de sí mismo.")
        case '(':
            return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener paréntesis dentro de sí mismo.")
        case ')':
            return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener paréntesis dentro de sí mismo.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return NENC(rem[1:], charsTillNow + rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener más de una e.")
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return DEAD(rem[1:], "un número en notación exponencial con exponente negativo no puede tener letras (excepto la e que indica que está en notación exponencial).")

def VAR(rem, charsTillNow):
    if len(rem) == 0:
        print(charsTillNow, "Variable", sep="\t")
        return
    match rem[0]:
        case ' ':
            print(charsTillNow, "Variable", sep="\t")
            return V(rem[1:])
        case '.':
            return DEAD(rem[1:], "una variable no puede tener puntos.")
        case '-':
            print(charsTillNow, "Variable", sep="\t")
            return R(rem[1:])
        case '=':
            print(charsTillNow, "Variable", sep="\t")
            return EQ(rem[1:])
        case '+':
            print(charsTillNow, "Variable", sep="\t")
            return S(rem[1:])
        case '*':
            print(charsTillNow, "Variable", sep="\t")
            return M(rem[1:])
        case '/':
            print(charsTillNow, "Variable", sep="\t")
            return D(rem[1:])
        case '^':
            print(charsTillNow, "Variable", sep="\t")
            return POT(rem[1:])
        case '(':
            return DEAD(rem[1:], "una variable no puede tener paréntesis.")
        case ')':
            print(charsTillNow, "Variable", sep="\t")
            return EP(rem[1:])
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return VAR(rem[1:], charsTillNow+rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return VAR(rem[1:], charsTillNow+rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return VAR(rem[1:], charsTillNow+rem[0])

def NOR(rem):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un signo de resta que no tiene nada después.", sep="")
        return
    match rem[0]:
        case ' ':
            return R(rem[1:])
        case '.':
            return P(rem[1:], rem[0])
        case '-':
            return DEAD(rem[1:], "no pueden haber dos símbolos de resta pegados.")
        case '=':
            return DEAD(rem[1:], "no puede haber un signo de asignación inmediatamente después de un signo de resta.")
        case '+':
            return DEAD(rem[1:], "no puede haber un signo de suma inmediatamente después de un signo de resta.")
        case '*':
            return DEAD(rem[1:], "no puede haber un signo de multiplicación inmediatamente después de un signo de resta.")
        case '/':
            return DEAD(rem[1:], "no puede haber un signo de división inmediatamente después de un signo de resta.")
        case '^':
            return DEAD(rem[1:], "no puede haber un signo ^ inmediatamente después de un signo de resta.")
        case '(':
            print('-', "Resta", sep="\t")
            return SP(rem[1:])
        case ')':
            return DEAD(rem[1:], "no puede haber un paréntesis que cierra inmediatamente después de un signo de resta.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return NN(rem[1:], '-' + rem[0])
            if(rem[0].lower() == 'e'): # E,e
                print('-', "Resta", sep="\t")
                return VAR(rem[1:], rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                print('-', "Resta", sep="\t")
                return VAR(rem[1:], rem[0])

def R(rem):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un signo de resta que no tiene nada después.", sep="")
        return
    match rem[0]:
        case ' ':
            print('-', "Resta", sep="\t")
            return V(rem[1:])
        case '.':
            print('-', "Resta", sep="\t")
            return P(rem[1:])
        case '-':
            print('-', "Resta", sep="\t")
            return NOR(rem[1:])
        case '=':
            return DEAD(rem[1:], "no puede haber un signo de asignación inmediatamente después de un signo de resta.")
        case '+':
            return DEAD(rem[1:], "no puede haber un signo de suma inmediatamente después de un signo de resta.")
        case '*':
            return DEAD(rem[1:], "no puede haber un signo de mulitplicación inmediatamente después de un signo de resta.")
        case '/':
            return DEAD(rem[1:], "no puede haber un signo de división inmediatamente después de un signo de resta.")
        case '^':
            return DEAD(rem[1:], "no puede haber un ^ inmediatamente después de un signo de resta.")
        case '(':
            print('-', "Resta", sep="\t")
            return SP(rem[1:])
        case ')':
            return DEAD(rem[1:], "no puede haber un paréntesis que cierra inmediatamente después de un signo de resta.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                print('-', "Resta", sep="\t")
                return N(rem[1:], rem[0])
            if(rem[0].lower() == 'e'): # E,e
                print('-', "Resta", sep="\t")
                return VAR(rem[1:], rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                print('-', "Resta", sep="\t")
                return VAR(rem[1:], rem[0])

def NN(rem, charsTillNow):
    if len(rem) == 0:
        print(charsTillNow, "Entero negativo", sep="\t")
        return
    match rem[0]:
        case ' ':
            print(charsTillNow, "Entero negativo", sep="\t")
            return V(rem[1:])
        case '.':
            return NDE(rem[1:], charsTillNow + rem[0])
        case '-':
            print(charsTillNow, "Entero negativo", sep="\t")
            return NOR(rem[1:])
        case '=':
            return DEAD(rem[1:], "no puede haber un signo de asignación después de un entero negativo.")
        case '+':
            print(charsTillNow, "Entero negativo", sep="\t")
            return S(rem[1:])
        case '*':
            print(charsTillNow, "Entero negativo", sep="\t")
            return M(rem[1:])
        case '/':
            print(charsTillNow, "Entero negativo", sep="\t")
            return D(rem[1:])
        case '^':
            print(charsTillNow, "Entero negativo", sep="\t")
            return POT(rem[1:])
        case '(':
            return DEAD(rem[1:], "no puede haber un paréntesis que abre después de un número negativo, sin nada de por medio.")
        case ')':
            print(charsTillNow, "Entero negativo", sep="\t")
            return EP(rem[1:])
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return NN(rem[1:], charsTillNow + rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return NE(rem[1:], charsTillNow + rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return DEAD(rem[1:], "un entero negativo no puede contener letras.")

def EQ(rem):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un signo = que no tiene nada después.", sep="")
        return
    match rem[0]:
        case ' ':
            return EQ(rem[1:])
        case '.':
            print('=', "Asignación", sep="\t")
            return P(rem[1:])
        case '-':
            print('=', "Asignación", sep="\t")
            return NOR(rem[1:])
        case '=':
            return DEAD(rem[1:], "no pueden haber dos símbolos de asignación juntos.")
        case '+':
            print('=', "Asignación", sep="\t")
            return S(rem[1:])
        case '*':
            return DEAD(rem[1:], "no puede haber un símbolo de multiplicación después de un signo de asignación.")
        case '/':
            return DEAD(rem[1:], "no puede haber un símbolo de división después de un signo de asignación.")
        case '^':
            return DEAD(rem[1:], "no puede haber un ^ después de un signo de asignación.")
        case '(':
            print('=', "Asignación", sep="\t")
            return SP(rem[1:])
        case ')':
            return DEAD(rem[1:], "no puede haber un paréntesis que cierra después de un signo de asignación.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                print('=', "Asignación", sep="\t")
                return N(rem[1:], rem[0])
            if(rem[0].lower() == 'e'): # E,e
                print('=', "Asignación", sep="\t")
                return VAR(rem[1:], rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                print('=', "Asignación", sep="\t")
                return VAR(rem[1:], rem[0])

def S(rem):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un signo de suma que no tiene nada después.", sep="")
        return
    match rem[0]:
        case ' ':
            return S(rem[1:])
        case '.':
            print('+', "Suma", sep="\t")
            return P(rem[1:])
        case '-':
            print('+', "Suma", sep="\t")
            return NOR(rem[1:])
        case '=':
            return DEAD(rem[1:], "no puede haber un signo de asignación después de un signo de suma.")
        case '+':
            return DEAD(rem[1:], "no pueden haber dos signos de suma juntos.")
        case '*':
            return DEAD(rem[1:], "no puede haber un signo de multiplicación después de un signo de suma.")
        case '/':
            return DEAD(rem[1:], "no puede haber un signo de división después de un signo de suma.")
        case '^':
            return DEAD(rem[1:], "no puede haber un signo ^ después de un signo de suma.")
        case '(':
            print('+', "Suma", sep="\t")
            return SP(rem[1:])
        case ')':
            return DEAD(rem[1:], "no puede haber un paréntesis que cierra después de un signo de suma.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                print('+', "Suma", sep="\t")
                return N(rem[1:], rem[0])
            if(rem[0].lower() == 'e'): # E,e
                print('+', "Suma", sep="\t")
                return VAR(rem[1:], rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                print('+', "Suma", sep="\t")
                return VAR(rem[1:], rem[0])

def M(rem):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un signo de multiplicación que no tiene nada después.", sep="")
        return
    match rem[0]:
        case ' ':
            return M(rem[1:])
        case '.':
            print('*', "Multiplicación", sep="\t")
            return P(rem[1:])
        case '-':
            print('*', "Multiplicación", sep="\t")
            return NOR(rem[1:])
        case '=':
            return DEAD(rem[1:], "no puede haber un signo de asignación después de un signo de muliplicación.")
        case '+':
            print('*', "Multiplicación", sep="\t")
            return S(rem[1:])
        case '*':
            return DEAD(rem[1:], "no puede haber dos signos de multiplicación juntos.")
        case '/':
            return DEAD(rem[1:], "no puede haber un signo de división después de un signo de muliplicación.")
        case '^':
            return DEAD(rem[1:], "no puede haber un signo ^ después de un signo de muliplicación.")
        case '(':
            print('*', "Multiplicación", sep="\t")
            return SP(rem[1:])
        case ')':
            return DEAD(rem[1:], "no puede haber un paréntesis que cierra después de un signo de muliplicación.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                print('*', "Multiplicación", sep="\t")
                return N(rem[1:], rem[0])
            if(rem[0].lower() == 'e'): # E,e
                print('*', "Multiplicación", sep="\t")
                return VAR(rem[1:], rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                print('*', "Multiplicación", sep="\t")
                return VAR(rem[1:], rem[0])

def D(rem):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un signo de división que no tiene nada después.", sep="")
        return
    match rem[0]:
        case ' ':
            return D(rem[1:])
        case '.':
            print('/', "División", sep="\t")
            return P(rem[1:])
        case '-':
            print('/', "División", sep="\t")
            return NOR(rem[1:])
        case '=':
            return DEAD(rem[1:], "no puede haber un signo de asignación después de un signo de división.")
        case '+':
            print('/', "División", sep="\t")
            return S(rem[1:])
        case '*':
            return DEAD(rem[1:], "no puede haber un signo de multiplicación después de un signo de división.")
        case '/':
            return COM(rem[1:], "//")
        case '^':
            return DEAD(rem[1:], "no puede haber un signo ^ después de un signo de división.")
        case '(':
            print('/', "División", sep="\t")
            return SP(rem[1:])
        case ')':
            return DEAD(rem[1:], "no puede haber un paréntesis que cierra después de un signo de división.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                print('/', "División", sep="\t")
                return N(rem[1:], rem[0])
            if(rem[0].lower() == 'e'): # E,e
                print('/', "División", sep="\t")
                return VAR(rem[1:], rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                print('/', "División", sep="\t")
                return VAR(rem[1:], rem[0])

def COM(rem, charsTillNow):
    if len(rem) == 0:
        print(charsTillNow, "Comentario", sep="\t")
        return
    match rem[0]:
        case ' ':
            return COM(rem[1:], charsTillNow + rem[0])
        case '.':
            return COM(rem[1:], charsTillNow + rem[0])
        case '-':
            return COM(rem[1:], charsTillNow + rem[0])
        case '=':
            return COM(rem[1:], charsTillNow + rem[0])
        case '+':
            return COM(rem[1:], charsTillNow + rem[0])
        case '*':
            return COM(rem[1:], charsTillNow + rem[0])
        case '/':
            return COM(rem[1:], charsTillNow + rem[0])
        case '^':
            return COM(rem[1:], charsTillNow + rem[0])
        case '(':
            return COM(rem[1:], charsTillNow + rem[0])
        case ')':
            return COM(rem[1:], charsTillNow + rem[0])
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return COM(rem[1:], charsTillNow + rem[0])
            if(rem[0].lower() == 'e'): # E,e
                return COM(rem[1:], charsTillNow + rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return COM(rem[1:], charsTillNow + rem[0])

def POT(rem):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un signo ^ que no tiene nada después.", sep="")
        return
    match rem[0]:
        case ' ':
            return POT(rem[1:])
        case '.':
            print('^', "Potencia", sep="\t")
            return P(rem[1:])
        case '-':
            print('^', "Potencia", sep="\t")
            return NOR(rem[1:])
        case '=':
            return DEAD(rem[1:], "no puede haber un signo de asignación después de un signo '^'.")
        case '+':
            print('^', "Potencia", sep="\t")
            return S(rem[1:])
        case '*':
            return DEAD(rem[1:], "no puede haber un signo de multiplicación después de un signo '^'.")
        case '/':
            print('^', "Potencia", sep="\t")
            return D(rem[1:])
        case '^':
            return DEAD(rem[1:], "no puede haber dos signos ^ juntos.")
        case '(':
            print('^', "Potencia", sep="\t")
            return SP(rem[1:])
        case ')':
            return DEAD(rem[1:], "no puede haber un paréntesis que cierra después de un signo '^'.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                print('^', "Potencia", sep="\t")
                return N(rem[1:], rem[0])
            if(rem[0].lower() == 'e'): # E,e
                print('^', "Potencia", sep="\t")
                return VAR(rem[1:], rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                print('^', "Potencia", sep="\t")
                return VAR(rem[1:], rem[0])

def SP(rem):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\"es sintácticamente inválida: al final, hay un signo ( que no tiene nada después.", sep="")
        return
    match rem[0]:
        case ' ':
            print('(', "Paréntesis que abre", sep="\t")
            return V(rem[1:])
        case '.':
            print('(', "Paréntesis que abre", sep="\t")
            return P(rem[1:])
        case '-':
            print('(', "Paréntesis que abre", sep="\t")
            return NOR(rem[1:])
        case '=':
            return DEAD(rem[1:], "no puede haber un signo de asignación dentro de paréntesis sin nada antes.")
        case '+':
            return DEAD(rem[1:], "no puede haber un signo de suma dentro de paréntesis sin nada antes.")
        case '*':
            return DEAD(rem[1:], "no puede haber un signo de multiplicación dentro de paréntesis sin nada antes.")
        case '/':
            print('(', "Paréntesis que abre", sep="\t")
            return D(rem[1:])
        case '^':
            return DEAD(rem[1:], "no puede haber un signo ^ dentro de paréntesis sin nada antes.")
        case '(':
            print('(', "Paréntesis que abre", sep="\t")
            return SP(rem[1:])
        case ')':
            return DEAD(rem[1:], "no puede haber paréntesis sin nada adentro.")
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                print('(', "Paréntesis que abre", sep="\t")
                return N(rem[1:], rem[0])
            if(rem[0].lower() == 'e'): # E,e
                print('(', "Paréntesis que abre", sep="\t")
                return VAR(rem[1:], rem[0])
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                print('(', "Paréntesis que abre", sep="\t")
                return VAR(rem[1:], rem[0])

def EP(rem):
    if len(rem) == 0:
        print(')', "Paréntesis que cierra", sep="\t")
        return
    match rem[0]:
        case ' ':
            print(')', "Paréntesis que cierra", sep="\t")
            return V(rem[1:])
        case '.':
            return DEAD(rem[1:], "no puede haber un punto inmediatamente después de cerrar paréntesis.")
        case '-':
            print(')', "Paréntesis que cierra", sep="\t")
            return NOR(rem[1:])
        case '=':
            return DEAD(rem[1:], "no puede haber un signo de asignación inmediatamente después de cerrar paréntesis.")
        case '+':
            print(')', "Paréntesis que cierra", sep="\t")
            return S(rem[1:])
        case '*':
            print(')', "Paréntesis que cierra", sep="\t")
            return M(rem[1:])
        case '/':
            print(')', "Paréntesis que cierra", sep="\t")
            return D(rem[1:])
        case '^':
            print(')', "Paréntesis que cierra", sep="\t")
            return POT(rem[1:])
        case '(':
            return DEAD(rem[1:], "no se pueden abrir paréntesis inmediatamente después de cerrarlos, sin nada de por medio.")
        case ')':
            print(')', "Paréntesis que cierra", sep="\t")
            return EP(rem[1:])
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return DEAD(rem[1:], "no puede haber un número inmediatamente después de cerrar paréntesis.")
            if(rem[0].lower() == 'e'): # E,e
                return DEAD(rem[1:], "no puede haber letras inmediatamente después de cerrar paréntesis.")
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return DEAD(rem[1:], "no puede haber letras inmediatamente después de cerrar paréntesis.")

def DEAD(rem, message):
    if len(rem) == 0:
        print("La expresión \"", expresion, "\" es inválida: ", message, sep="")
        return
    match rem[0]:
        case ' ':
            return DEAD(rem[1:], message)
        case '.':
            return DEAD(rem[1:], message)
        case '-':
            return DEAD(rem[1:], message)
        case '=':
            return DEAD(rem[1:], message)
        case '+':
            return DEAD(rem[1:], message)
        case '*':
            return DEAD(rem[1:], message)
        case '/':
            return DEAD(rem[1:], message)
        case '^':
            return DEAD(rem[1:], message)
        case '(':
            return DEAD(rem[1:], message)
        case ')':
            return DEAD(rem[1:], message)
        case _:
            if(rem[0].isdigit()): # 0,1,2,3,4,5,6,7,8,9
                return DEAD(rem[1:], message)
            if(rem[0].lower() == 'e'): # E,e
                return DEAD(rem[1:], message)
            if(rem[0].isalpha() or rem[0] == '_'): # ({A,B...Z} U {a,b...z} U {_}) - {E,e}
                return DEAD(rem[1:], message)