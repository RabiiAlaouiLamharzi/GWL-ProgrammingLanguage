import contextlib

cnt = 1
g = 0
counter = 0
stack = []
A = []
typ = 0
ope = []

with open("stack.txt", "w") as o:
            o.write('')
            o.close()
            
class Main_function:
    global cnt
    f = 0
    with open('AST.txt','r') as o:
        for line in o:
            for word in line.split():
                if(str(word) == "program"):
                    f = 1
                if(cnt == 3 and f == 1):
                        print('PROGRAM' + '\t' + word)
                        f = 0
                        break
                cnt = cnt +1
                
class typedef:
   global cnt 
   global g 
   global A
   f = 0
   cnt = 1
   
   with open('AST.txt','r') as o:
        for line in o:
            for word in line.split():
                if(str(word) == "typedef"):
                    if(g == 0):
                        print('\nDATA' + '\n\n')
                        g = 1
                    f = 1
                    pass
                else:
                    if(cnt == 2 and str(word) != "struct" and str(word) != "-----------" and str(word).isalpha()):
                        A.append(word)
                    else:
                        pass
                if(f == 1):
                    cnt = cnt +1
            cnt = 1
    
class constant_definition:
    global cnt
    global g
    f = 0
    cnt = 1
    with open('AST.txt','r') as o:
        for line in o:
            for word in line.split():
                if(str(word) == "$Define"):
                    print('\nDATA' + '\n\n')
                    g = 1
                    f = 1
                if(cnt == 3 and f == 1):
                    re = word
                if(cnt == 5 and f == 1):
                    if(word.isnumeric()):
                        print('CONST' + '    ' + re + '    ' + 'INT' + '    ' + '1    ' + word)
                if(f == 1):
                    cnt = cnt +1
                    
class variable_declaration:
    global cnt
    global g
    global A
    cnt = 1
    f = 0
    k = 0
    g = 0
    no = 0
    x = 0
    with open('AST.txt','r') as o:
        for line in o:
            for word in line.split():
                if(str(word) != "Function" and str(word) != "FunctionCall" and str(word) != "Selection" and str(word) != "typedef" and str(word) != "print" and str(word) != "-----------" and x != 1):
                    for wo in A:
                        if(str(word) == wo and cnt == 1):
                            re = wo
                            g = 1
                            f = 1
                        if(cnt == 3 and g == 1 and str(word) != "struct" and str(word) != "int" and str(word) != "fraction" and str(word) != "string"):
                            print('VAR' + '    ' + word + '    ' + re + '    ' + '1    ' + '*')
                            g = 0
                    if((str(word) == "int") or (str(word) == "fraction") or (str(word) == "string")):
                        if(k == 0):
                            if(word == 'int'):
                                re = 'INT'
                            elif(word == 'fraction'):
                                re = 'FRACTION'
                            elif(word == 'string'):
                                re = 'STRING'
                            f = 1
                    if(cnt == 5 and f == 1):
                            rec = word
                            k = 1
                    if(cnt == 2 and k == 1):
                            print('VAR' + '    ' + rec + '    ' + re + '    ' + '1    ' + word)
                            f = 0
                            k = 0
                else:
                    if(str(word) != "Function" or str(word) != "FunctionCall" or str(word) == "typedef" or str(word) == "Selection" or str(word) == "print"):
                        x = 1
                if(f == 1):
                    cnt = cnt +1
            cnt = 1
            x = 0
        no = 0
    g = 0
       
class variable_assignment:
    global cnt
    global g
    cnt = 1
    f = 0
    k = 0
    b = 0
    r = 0
    with open('AST.txt','r') as o:
        for line in o:
            for word in line.split():
                if (r == 0):
                    if((str(word) == line[0]) and (str(word) == ":")):
                        if(k == 0):
                            if(g == 0):
                                print('\nCODE' + '\n\n')
                                g = 1
                            b = 1
                            f = 1
                    if(cnt == 3 and f == 1 and b == 1):
                            rec = word
                            k = 1
                    if(cnt == 2 and k == 1):
                        if((str(word) == "+") or (str(word) == "-") or (str(word) == "*") or (str(word) == "/")):
                            r = 1
                        else:
                            print('ASSIGN' + '    ' + word + '    ' + rec + '\n')
                            f = 0
                            k = 0
                    if(f == 1):
                        cnt = cnt +1
            b = 0
            cnt = 1
            
class function:
    
    global cnt
    global g
    global stack
    global ope
    cnt = 1
    f = 0
    k = 0
    t = 0
    u = 0
    gh = 0
    dh = 0
    op =''
    with open('AST.txt','r') as o:
        for line in o:
            for word in line.split():
                if(str(word) == "Function"):
                    if(g == 0):
                            print('\nCODE' + '\n\n')
                            g = 1
                    if(k == 0):
                        f = 1
                if(cnt == 3 and f == 1):
                    if(t == 0):
                        rec = word
                        k = 1
                        t = 1
                    else:
                        pass
                    
                if(str(word) == '+'):
                    gh = 1
                    op = '+'
                if(str(word) == '-'):
                    gh = 1
                    op = '-'
                if(str(word) == '*'):
                    gh = 1
                    op = '*'
                if(str(word) == '/'):
                    gh = 1
                    op = '/'
                    
                if(str(word) == 'return'):
                    u = 1
                if(cnt == 4 and u == 1):
                    if(word != '-----------'):
                        stack.append(op)
                    with open("stack.txt", "a") as o:
                        with contextlib.redirect_stdout(o):
                            if(word != '-----------'):
                                print('PUSH    ' + '"' + op + '"')
                if(f == 1):
                    cnt = cnt +1
            cnt = 1
            
class function_call:

    global cnt
    global g
    global stack
    global ope
    cnt = 1
    f = 0
    k = 0
    t = 0
    d = None
    q = None
    y = 0
    to = 0
    with open('AST.txt','r') as o:
        for line in o:
            for word in line.split():
                    if(str(word) == "FunctionCall"):
                        if(g == 0):
                            print('\nCODE' + '\n\n')
                        f = 1
                    if(cnt == 7 and f == 1):
                        with open("stack.txt", "a") as o:
                            with contextlib.redirect_stdout(o):
                                stack.append(word)
                                print('PUSH    ' + '"' + str(word) + '"')
                                y = 1
                    if(cnt == 2 and y == 1):
                        with open("stack.txt", "a") as o:
                            with contextlib.redirect_stdout(o):
                                stack.append(word)
                                print('PUSH    ' + '"' + str(word) + '"')
                                to = 1

                    if(to == 1):
                        if(stack == False):
                            print('NOOP    ' + '*    ' +  + '*    ' + '*')
                        else:
                            a = stack.pop()
                            b = stack.pop()
                            oper = stack.pop()
                            if(oper == '+'):
                                result = int(a) + int(b)
                                with open("stack.txt", "a") as o:
                                    with contextlib.redirect_stdout(o):
                                        print('POP            ' + '"' + str(result) + '"')
                                        print('WRITE    ' + '"' + str(result) + '"')
                            
                            if(oper == '-'):
                                result = int(a) - int(b)
                                with open("stack.txt", "a") as o:
                                    with contextlib.redirect_stdout(o):
                                        print('POP            ' + '"' + str(result) + '"')
                                        print('WRITE    ' + '"' + str(result) + '"')
                                
                            if(oper == '*'):
                                result = int(a) * int(b)
                                with open("stack.txt", "a") as o:
                                    with contextlib.redirect_stdout(o):
                                        print('POP            ' + '"' + str(result) + '"')
                                        print('WRITE    ' + '"' + str(result) + '"')
                                
                            if(oper == '/'):
                                if(int(a) > int(b)):
                                    if(int(b) == 0):
                                        with open("stack.txt", "a") as o:
                                            with contextlib.redirect_stdout(o):
                                                print("You can't divide by zero !\n")
                                    else:
                                        result = int(a) / int(b)
                                        with open("stack.txt", "a") as o:
                                            with contextlib.redirect_stdout(o):
                                                print('POP            ' + '"' + str(result) + '"')
                                                print('WRITE    ' + '"' + str(result) + '"')
                                else:
                                    if(int(a) == 0):
                                        with open("stack.txt", "a") as o:
                                            with contextlib.redirect_stdout(o):
                                                print("You can't divide by zero !\n")
                                    else:
                                        result = int(b) / int(a)
                                        with open("stack.txt", "a") as o:
                                            with contextlib.redirect_stdout(o):
                                                print('POP            ' + '"' + str(result) + '"')
                                                print('WRITE    ' + '"' + str(result) + '"')
                                        
                    if(f == 1):
                        cnt = cnt +1
            cnt = 1
    with open("stack.txt", "r") as o:
        content = o.read()
    print(content)
            
    
class arithmetic_assignment:   
    global cnt
    global g
    cnt = 1
    f = 0
    k = 0
    y = 0
    z = 0
    no = 0
    with open('AST.txt','r') as o:
        for line in o:
            for word in line.split():
                if(str(word) != "Function" and no == 0):
                    if(word == 'return'):
                        no = 0
                    if(str(word) == ":"):
                        if(k == 0):
                            if(g == 0):
                                print('\nCODE' + '\n\n')
                                g = 1
                            f = 1
                    if(cnt == 3 and f == 1):
                        if(word == '-----------'):
                            pass
                        else:
                            re = word
                            k = 1
                    if(cnt == 2 and k == 1):
                            if((str(word) == "+") or (str(word) == "-") or (str(word) == "*") or (str(word) == "/")):
                                if(word == '+'):
                                    rec = 'ADD'
                                elif(word == '-'):
                                    rec = 'SUB'
                                elif(word == '*'):
                                    rec = 'MULT'
                                elif(word == '/'):
                                    rec = 'DIV'
                                y = 1
                    if(cnt == 4 and y == 1):
                            re2 = word
                            z = 1
                    if(cnt == 2 and z == 1):
                            print(rec + '    ' + re2 + '    ' + word + '    ' + re)
                            f = 0
                            k = 0
                            y = 0
                            z = 0
                    if(f == 1):
                        cnt = cnt +1
                else:
                    no = 1
            cnt = 1
            
class Selection:
    
    global cnt
    global g
    global counter
    cnt = 1
    i = 0
    f = 0
    k = 0
    y = 0
    z1 = 0
    z2 = 0
    j1 = 0
    j2 = 0
    h1 = 0
    h2 = 0
    flag = 0
    re = None
    re2 = None
    a = None
    b = None
    a2 = None
    b2 = None
    wo = ''
    pr = 0
    fo = 0
    with open('AST.txt','r') as o:
        for line in o:
            for word in line.split():
                    if(pr == 1):
                        if(word != '-----------'):
                            wo = wo + ' ' + str(word)
                    if(str(word) == "print"):
                        pr = 1
                    if(str(word) == "Selection"):
                        if(i == 0):
                            pass
                        else:
                            f = 0
                            k = 0
                            y = 0
                            z1 = 0
                            z2 = 0
                            j1 = 0
                            j2 = 0
                            h1 = 0
                            h2 = 0
                            flag = 0
                            re = None
                            re2 = None
                            a = None
                            b = None
                            a2 = None
                            b2 = None
                        i = i+1
                        if(k == 0):
                            if(g == 0):
                                print('\nCODE' + '\n\n')
                                g = 1
                            f = 1
                    if(cnt == 3 and f == 1):
                        if(word == 'if'):
                            k = 1
                    if(cnt == 5 and k == 1):
                            if((str(word) == ">") or (str(word) == "<") or (str(word) == "==")):
                                if(word == '>'):
                                    rec = 'JGRTR'
                                elif(word == '<'):
                                    rec = 'JLESS'
                                elif(word == '=='):
                                    rec = 'JEQL'
                                y = 1
                    if(cnt == 7 and y == 1):
                            if((str(word) == "+") or (str(word) == "-") or (str(word) == "*") or (str(word) == "/")):
                                if(word == '+'):
                                    re = 'ADD'
                                    gh = '+'
                                elif(word == '-'):
                                    re = 'SUB'
                                    gh = '-'
                                elif(word == '*'):
                                    re = 'MULT'
                                    gh = '*'
                                elif(word == '/'):
                                    re = 'DIV'
                                    gh = '/'
                                j1 = 1
                            else:
                                if(re == None):
                                    re = word
                                z1 = 1
                    if(cnt == 9 and j1 == 1):
                            a = word
                            h1 = 1
                    if(cnt == 2 and h1 == 1):
                            if(flag == 0):
                                b = word
                                result1 = a + gh + b
                                if(counter == 0):
                                    print('         ' + rec + '    ' + re + '    ' + result1)
                                else:
                                    if(counter == 1):
                                        print('START' + '    ' + rec + '    ' + re + '    ' + result1)
                                    else:
                                        print('NEXT' + str(counter) + '    ' + rec + '    ' + re + '    ' + result1)
                                counter = counter + 1
                                flag = 1
                    if(cnt == 2 and z1 == 1):
                            if((str(word) == "+") or (str(word) == "-") or (str(word) == "*") or (str(word) == "/")):
                                if(word == '+'):
                                    re2 = 'ADD'
                                    gh = '+'
                                elif(word == '-'):
                                    re2 = 'SUB'
                                    gh = '-'
                                elif(word == '*'):
                                    re2 = 'MULT'
                                    gh = '*'
                                elif(word == '/'):
                                    re2 = 'DIV'
                                    gh = '/'
                                j2 = 1
                            else:
                                if(re2 == None):
                                    re2 = word
                                z2 = 1
                    if(cnt == 4 and j2 == 1):
                            a2 = word
                            h2 = 1
                    if(cnt == 2 and h2 == 1):
                            if(flag == 0):
                                b2 = word
                                result2 = a2 + gh + b2
                                if(counter == 0):
                                    print('         ' + rec + '    ' + re + '    ' + result2 + '    NEXT' + str(counter+1))
                                else:
                                    if(counter == 1):
                                        print('START' + '    ' + rec + '    ' + re + '    ' + result2  + '    NEXT' + str(counter+1))
                                    else:
                                        print('NEXT' + str(counter) + '    ' + rec + '    ' + re + '    ' + result2  + '    NEXT' + str(counter+1))
                                counter = counter + 1
                                flag = 1
                    if(f == 1):
                        cnt = cnt +1
            cnt = 1
            if(pr == 1):
                print('\t WRITE   ' + '"'+wo+'"')
                pr = 0
                wo = ''
    