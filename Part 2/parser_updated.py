import contextlib
import constants as fl

arr = []
arrSym = []
arrLit = []
A = []
cnt = 1
c = 1
d = 1
e = 1
y = 0
t = 0
nop = 0
current_token = ''
Symbol = ''
Literal = 0

x = open("variable_declaration.txt","w")
x.write('')

def get_next_token():
    
    global c
    word = arr[c]
    c = c + 1
    return word
    
def get_previous_token():
    
    global c
    c = c - 1
    word = arr[c]
    return word
    
def get_next_symbol():
    
    global d
    word = arrSym[d]
    d = d + 1
    return word
    
def get_previous_Symbol():
    
    global d
    d = d - 1
    word = arrSym[d]
    return word
    
def get_next_literal():
    
    global e
    word = arrLit[e]
    e = e + 1
    return word

def program():

  global current_token
  global Symbol
  if current_token != 'PROGRAM':
      return False
  current_token = get_next_token()
  if current_token != 'UDISTAT':
      return False
  current_token = get_next_token()
  #if we're here, we can construct a node of the cst
  fl.program('PROGRAM',Symbol)
  Symbol = get_next_symbol()
  
def user_defined_datatype():

    global current_token
    if current_token != 'UDISTAT':
        return False
    return True
    
def simple_type():

    global current_token
    if current_token != 'INT':
        if current_token != 'FRACTION':
            return False
        else:
            return True
    else:
        return True
    
def typedef_struct_declaration():
    
    global Symbol
    global current_token
    global t
    
    t = 1
    if current_token != 'TYPEDEF':
        return False
    current_token = get_next_token()
    if current_token != 'STRUCT':
        return False
    current_token = get_next_token()
    if current_token != 'LBRACK':
        return False
    current_token = get_next_token()
    variable_node = variable_assignment()
    if (variable_node == False):
        return False
    while(variable_assignment() != False):
        variable_node = variable_assignment()
    if current_token != 'RBRACK':
        return False
    current_token = get_next_token()
    UDD_node = user_defined_datatype()
    if not UDD_node:
        return False
    current_token = get_next_token()
    #if we're here, we can construct a node of the cst
    fl.typeDefstructDeclarationNode('TYPEDEF', 'STRUCT', 'LBRACK', 'RBRACK', Symbol)
    Symbol = get_next_symbol()
    t = 0
    lp = open("variable_declaration.txt", "w")
    lp.write('')
    
    
def variable_assignment():
 
    global Symbol
    global current_token
    global t
    global nop
    f = 0
    UDI_node = user_defined_identifier()
    if not UDI_node:
        if (current_token == 'INT'):
            current_token = get_next_token()
            UDI_node = user_defined_identifier()
            if not UDI_node:
                return False
            current_token = get_next_token()
            if current_token == 'DOT':
                current_token = get_next_token()
                UDI_node = user_defined_identifier()
                if not UDI_node:
                    return False
            if(t == 0):
                fl.VarDeclarationNode('INT', Symbol)
                Symbol = get_next_symbol()
            else:
                if(nop == 0):
                    with open("variable_declaration.txt", "a") as o:
                        with contextlib.redirect_stdout(o):
                            fl.VarDeclarationNode('INT', Symbol)
                else:
                    with open("body.txt", "a") as o:
                        with contextlib.redirect_stdout(o):
                            fl.VarDeclarationNode('INT', Symbol)
                Symbol = get_next_symbol()
            return True
                
        elif (current_token == 'FRACTION'):
            current_token = get_next_token()
            UDI_node = user_defined_identifier()
            if not UDI_node:
                return False
            current_token = get_next_token()
            if current_token == 'DOT':
                current_token = get_next_token()
                UDI_node = user_defined_identifier()
                if not UDI_node:
                    return False
            if(t == 0):
                fl.VarDeclarationNode('FRACTION', Symbol)
                Symbol = get_next_symbol()
            else:
                if(nop == 0):
                    with open("variable_declaration.txt", "a") as o:
                        with contextlib.redirect_stdout(o):
                            fl.VarDeclarationNode('FRACTION', Symbol)
                else:
                    with open("body.txt", "a") as o:
                        with contextlib.redirect_stdout(o):
                            fl.VarDeclarationNode('FRACTION', Symbol)
                Symbol = get_next_symbol()
            return True
        else:
            return False
                    
    current_token = get_next_token()
    if current_token == 'DOT':
        f = 1
        current_token = get_next_token()
        UDI_node = user_defined_identifier()
        if not UDI_node:
            return False
        current_token = get_next_token()
    if current_token != 'ASSIGN':
        if(current_token == 'UDISTAT'):
            Symbol2 = get_next_symbol()
            if(t == 0):
                fl.VarDeclarationNode(Symbol, Symbol2)
                Symbol = Symbol2
                current_token = get_previous_token()
            else:
                if(nop == 0):
                    with open("variable_declaration.txt", "a") as o:
                        with contextlib.redirect_stdout(o):
                            fl.VarDeclarationNode(Symbol, Symbol2)
                else:
                    with open("body.txt", "a") as o:
                        with contextlib.redirect_stdout(o):
                            fl.VarDeclarationNode(Symbol, Symbol2)
                Symbol = Symbol2
            return True
        else:
            return False
    current_token = get_next_token()
    function_call_node = function_call()
    number_node = None
    fraction_node = None
    UDI_node = None
    if not function_call:
        number_node = number()
        fraction_node = None
        UDI_node = None
        if not number_node:
            fraction_node = fraction()
            UDI_node = None
            if not fraction_node:
                UDI_node = user_defined_identifier()
                if not UDI_node:
                    return False
    current_token = get_next_token()
    if (current_token == 'ADD' or current_token == 'SUB' or current_token == 'MULT' or current_token == 'DIV'):
        current_token = get_next_token()
        UDI_node = user_defined_identifier()
        number_node = None
        if not UDI_node:
            number_node = number()
            if not number_node:
                return False
    #if we're here, we can construct a node of the cst
    if(f == 0):
        if(function_call_node == False):
            Symbol = get_next_symbol()
            Symbol2 = get_next_symbol()
            if(t == 0):
                fl.VarAssignmentNode(Symbol,'ASSIGN', Symbol2)
                Symbol = get_next_symbol()
            else:
                if(nop == 0):
                    with open("variable_declaration.txt", "a") as o:
                        with contextlib.redirect_stdout(o):
                            fl.VarAssignmentNode(Symbol,'ASSIGN', Symbol2)
                else:
                    with open("body.txt", "a") as o:
                        with contextlib.redirect_stdout(o):
                            fl.VarAssignmentNode(Symbol,'ASSIGN', Symbol2)
                Symbol = get_next_symbol()
            return True
        else:
            print ("variable_assignment")
    else:
        Symbol = get_next_symbol()
        Symbol2 = get_next_symbol()
        Symbol3 = get_next_symbol()
        blan = Symbol + '.' + Symbol2
        if(t == 0):
            fl.VarAssignmentNode(blan, 'ASSIGN', Symbol2)
            f = 0
            current_token = get_previous_token()
            current_token = get_previous_token()
        else:
            if(nop == 0):
                with open("variable_declaration.txt", "a") as o:
                    with contextlib.redirect_stdout(o):
                        fl.VarAssignmentNode(blan, 'ASSIGN', Symbol2)
                        f = 0
                        current_token = get_previous_token()
                        current_token = get_previous_token()
            else:
                with open("body.txt", "a") as o:
                    with contextlib.redirect_stdout(o):
                        fl.VarAssignmentNode(blan, 'ASSIGN', Symbol2)
                        f = 0
                        current_token = get_previous_token()
                        current_token = get_previous_token()
        return True
    
def constant_declaration():

    global Symbol
    global Literal
    global current_token
    if current_token != 'DOLLARDEFINE':
        return False
    current_token = get_next_token()
    UDI_node = user_defined_identifier()
    if not UDI_node:
        return False
    current_token = get_next_token()
    number_node = number()
    if not number_node:
        return False
    current_token = get_next_token()
    #if we're here, we can construct a node of the cst
    fl.constDeclarationNode('DOLLARDEFINE', Symbol, Literal)
    Symbol = get_next_symbol()
    Literal = get_next_literal()
    
def simple_type():

    global Symbol
    global current_token
    if current_token != 'INT':
        if current_token != 'FRACTION':
            return False
        else:
            return True
    else:
        return True

def function_declaration():
    
    global Symbol
    global current_token
    global t
    t = 1
    if current_token != 'VOID':
        UDD_node = user_defined_datatype()
        Symbol = get_next_symbol()
        s1 = Symbol
        if not UDD_node:
            return False
    else:
        s1 = 'VOID'
    current_token = get_next_token()
    function_name_node = function_name()
    if not function_name_node:
        return False
    current_token = get_next_token()
    if current_token != 'LPAREN':
        return False
    current_token = get_next_token()
    parameter_node = parameter_list()
    if (parameter_node == False):
        return False
    if current_token != 'RPAREN':
        return False
    current_token = get_next_token()
    if current_token != 'LBRACK':
        return False
    current_token = get_next_token()
    body_token = body()
    if(current_token == 'RBRACK'):
        current_token = get_next_token()
    if current_token != 'RETURN':
        return False
    current_token = get_next_token()
    
    number_node = number()
    fraction_node = None
    UDI_node = None
    if not number_node:
        fraction_node = fraction()
        UDI_node = None
        if not fraction_node:
            UDI_node = user_defined_identifier()
            if not UDI_node:
                return False
    current_token = get_next_token()
    if current_token != 'RBRACK':
        return False
    #if we're here, we can construct a node of the cst
    current_token = get_next_token()
    Symbol = get_next_symbol()
    print ("function")
    fl.functionDeclarationNode(s1, function_name_node, 'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK')
    t = 0

def function_declaration_num():
    
    global Symbol
    global current_token
    if current_token != 'INT':
        if current_token != 'FRACTION':
            f = 1
    current_token = get_next_token()
    function_name_num_node = function_name_num()
    if not function_name_num_node:
        f = 1
    current_token = get_next_token()
    if current_token != 'LPAREN':
        f = 1
    current_token = get_next_token()
    parameter_node = parameter_list()
    if not parameter_node:
        f = 1
    while (current_token == 'SEPARATE'):
        current_token = get_next_token()
        parameter_node = parameter_list()
        if not parameter_node:
            f = 1
    if current_token != 'RPAREN':
        f = 1
    current_token = get_next_token()
    if current_token != 'LBRACK':
        f = 1
    current_token = get_next_token()
    body_token = body()
    if body_token != False:
        current_token = get_next_token()
    if current_token != 'RBRACK':
        f = 1
    #if we're here, we can construct a node of the cst
    if (f == 0):
        print ("program")
    
def function_name():

    global Symbol
    global current_token
    UDI_node = user_defined_identifier()
    if not UDI_node:
        return False
    print ("the function name is ",Symbol)
    A.append(Symbol)
    Symbol = get_next_symbol()
    return Symbol
 
def function_name_num():

    global Symbol
    global current_token
    UDI_node = user_defined_identifier()
    if not UDI_node:
        return False
    number_node = number()
    if not number_node:
        return False
    return current_token
    
def parameter_list():

    global Symbol
    global current_token
    var_node = variable_assignment()
    while(current_token == 'SEPARATE'):
        current_token = get_next_token()
        var_node = variable_assignment()
    if (var_node == False):
        return False

def body():
    
    global Symbol
    global current_token
    global nop
    u = 0
    if(nop != 1):
        nop = 1
    else:
        u = 1
    statements_node = statements()
    if (statements_node == False):
        return False
    if(u != 1):
        nop = 0
    
def statements():

    global Symbol
    global current_token
    variable_assignment_node = variable_assignment()
    task_node = None
    selection_node = None
    loop_node = None
    function_call_node = None
    function_call_num_node = None
    if (variable_assignment_node == False):
        task_node = task()
        selection_node = None
        loop_node = None
        function_call_node = None
        function_call_num_node = None
        if (task_node == False):
            selection_node = selection()
            loop_node = None
            function_call_node = None
            function_call_num_node = None
            if (selection_node == False):
                loop_node = loop()
                function_call_node = None
                function_call_num_node = None
                if (loop_node == False):
                    function_call_node = function_call()
                    function_call_num_node = None
                    if (function_call_node == False):
                        function_call_num_node = function_call_num()
                        if (function_call_num_node == False):
                            return False
    #if we're here, we can construct a node of the cst
    if (current_token != 'RBRACK'):
        current_token = get_next_token()
    print ("statement")
    
def task():

    global Symbol
    global current_token
    read_node = read()
    print_node = None
    if (read_node == False):
        print_node = print_()
        if (print_node == False):
            return False
    #if we're here, we can construct a node of the cst
    print ("task")

def read():

    global Symbol
    global current_token
    if current_token != 'READ':
        return False
    current_token = get_next_token()
    number_node = number()
    UDI_node = None
    fraction_node = None
    if not number_node:
        UDI_node = user_defined_identifier()
        fraction_node = None
        if not UDI_node:
            fraction_node = fraction() 
            if not fraction_node:
                return False
    #if we're here, we can construct a node of the cst
    print ("read")
    
def print_():

    global Symbol
    global current_token
    if current_token != 'PRINT':
        return False
    current_token = get_next_token()
    Symbol = get_next_symbol()
    print ("print", Symbol) 
    Symbol = get_next_symbol()
    current_token = get_next_token()
    while(current_token == 'UDISTAT'):
        print ("print", Symbol) 
        Symbol = get_next_symbol()
        current_token = get_next_token()
    #if we're here, we can construct a node of the cst
   

def operation():

    global Symbol
    global current_token
    operand_node = operand()
    if not operand_node:
        return False
    current_token = get_next_token()
    if (current_token != 'ADD' and current_token != 'SUB' and current_token != 'MULT' and current_token != 'DIV' and current_token != 'MOD'):
        return False
    current_token = get_next_token()
    operand_node_2 = operand()
    if not operand_node:
        return False
    #if we're here, we can construct a node of the cst
    print ("program")

def operand():

    global Symbol
    global current_token
    function_call_num_node = function_call_num()
    number_node = None
    operation_node = None
    fraction_node = None
    if not function_call_num_node:
        number_node = number()
        operation_node = None
        fraction_node = None
        if not number_node:
            operation_node = operation()
            fraction_node = None
            if not operation_node:
                fraction_node = fraction()
                if not fraction_node:
                    f = 1
    #if we're here, we can construct a node of the cst
    if (f == 0):
        print ("program")

def function_call():
    
    global Symbol
    global current_token
    global y

    if current_token != 'UDISTAT':
        return False
    Symbol = get_next_symbol()
    if(Symbol != str(A[y])):
        Symbol = get_previous_Symbol()
        return False
    else:
        y = y+1
        current_token = get_next_token()
        if current_token != 'LPAREN':
            return False
        current_token = get_next_token()
        variable_declaration_node = variable_assignment()
        current_token = get_next_token()
        while(current_token == 'SEPARATE'):
            current_token = get_next_token()
            variable_declaration_node = variable_assignment()
            current_token = get_next_token()
        if current_token != 'RPAREN':
            return False
        #if we're here, we can construct a node of the cst
        print ("function_call")

def function_call_num():
    
    global Symbol
    global current_token
    function_call_num_node = function_call_num()
    if not function_call_num_node:
        f = 1
    current_token = get_next_token()
    if current_token != 'LPAREN':
        f = 1
    current_token = get_next_token()
    UDI_node = user_defined_identifier()
    if not UDI_node:
        f = 1
    current_token = get_next_token()
    while(current_token == 'SEPARATE'):
        current_token = get_next_token()
        UDI_node = user_defined_identifier()
        if not UDI_node:
            f = 1
        current_token = get_next_token()
    if current_token != 'RPAREN':
        f = 1
    #if we're here, we can construct a node of the cst
    if (f == 0):
        print ("program")
    
def loop():

    global Symbol
    global current_token
    if current_token != 'FOR':
        f = 1
    current_token = get_next_token()
    if current_token != 'LPAREN':
        f = 1
    current_token = get_next_token()
    CSL_node = condition_statement_loop()
    if not CSL_node:
        f = 1
    current_token = get_next_token()
    if current_token != 'RPAREN':
        f = 1
    current_token = get_next_token()
    if current_token != 'LBRACK':
        f = 1
    body_node = body()
    if body_node != False:
        current_token = get_next_token()
    if current_token != 'RBRACK':
        f = 1
    #if we're here, we can construct a node of the cst
    if (f == 0):
        print ("program")

def condition_statement_loop():

    global Symbol
    global current_token
    VDL_node = variable_declaration_loop()
    if not VDL_node:
        f = 1
    current_token = get_next_token()
    if current_token != 'SEPARATE':
        f = 1
    current_token = get_next_token()
    if current_token == 'NOT':
        current_token = get_next_token()
    ComLoup_node = comparaison_loop()
    if not ComLoup_node:
        f = 1
    current_token = get_next_token()
    if current_token != 'SEPARATE':
        f = 1
    current_token = get_next_token()
    opeLoop_node = operation_loop()
    if not opeLoop_node:
        f = 1

def variable_declaration_loop():
    
    global Symbol
    global current_token
    if current_token != 'INT':
        f = 1
    current_token = get_next_token()
    VNL_node = variable_name_loop()
    if not VNL_node:
        f = 1
    current_token = get_next_token()
    if current_token != 'ASSIGN':
        f = 1
    current_token = get_next_token()
    number_node = number()
    if not number_node:
        f = 1

def variable_name_loop():

    global Symbol
    global current_token
    UDI_node = user_defined_identifier()
    if not UDI_node:
        return False
    return current_token

def comparaison_loop():

    global Symbol
    global current_token
    if current_token != 'LPAREN':
        f = 1
    current_token = get_next_token()
    VNL_node = variable_name_loop()
    if not VNL_node:
        f = 1
    current_token = get_next_token()
    if (current_token != 'GREATER' and current_token != 'LESS' and current_token != 'LESSEQUAL' and current_token != 'GREATEREQUAL'):
        f = 1
    current_token = get_next_token()
    FuncCall_node = function_call()
    number_node = None
    fraction_node = None
    if not FuncCall_node:
        number_node = number()
        fraction_node = None
        if not number_node:
            fraction_node = fraction()
            if not fraction_node:
                f = 1
    if (f == 0):
        print ("program")

def operation_loop():

    global Symbol
    global current_token
    VNL_node = variable_name_loop()
    if not VNL_node:
        f = 1
    current_token = get_next_token()
    if current_token != 'ASSIGN':
        f = 1
    current_token = get_next_token()
    VNL_node = variable_name_loop()
    if not VNL_node:
        f = 1
    current_token = get_next_token()
    if current_token != 'ADD':
        f = 1
    current_token = get_next_token()
    number_node = number()
    if not VNL_node:
        f = 1
    if (f == 0):
        print ("program")

def selection():

    global Symbol
    global current_token
    global t
    global nop
    if current_token != 'IF':
        return False
    current_token = get_next_token()
    if current_token != 'LPAREN':
        return False
    current_token = get_next_token()
    CS_node = condition_statement()
    if (CS_node == False):
        return False
    if current_token != 'RPAREN':
        return False
    current_token = get_next_token()
    if current_token != 'LBRACK':
        return False
    current_token = get_next_token()
    body_node = body()
    while (current_token != 'RBRACK'):
        body_node = body()
        if(current_token == 'RBRACK'):
            break
        current_token = get_next_token()
    if current_token != 'RBRACK':
        return False
    current_token = get_next_token()
    if current_token == 'ELSE':
        current_token = get_next_token()
        if current_token != 'LBRACK':
            return False
        current_token = get_next_token()
        body_node = body()
        if current_token != 'RBRACK':
            return False
    #if we're here, we can construct a node of the cst
    print ("selection")
    
def condition_statement():
    
    global Symbol
    global current_token
    if current_token == 'NOT':
        current_token = get_next_token()
    comp_node = comparaison()
    if (comp_node == False):
        return False
    current_token = get_next_token()
    while (current_token == 'AND' or current_token == 'OR'):
        Symbol = get_next_symbol()
        Symbol = get_next_symbol()
        Symbol = get_next_symbol()
        current_token = get_next_token()
        if current_token == 'NOT':
            current_token = get_next_token()
        comp_node = comparaison()
        if (comp_node == False):
            return False
        current_token = get_next_token()
    
def comparaison():

    global Symbol
    global current_token
    comp1_node = compared()
    if (comp1_node == False):
        return False
    current_token = get_next_token()
    if (current_token != 'CEQUAL' and current_token != 'DIFF' and current_token != 'GREATER' and current_token != 'LESS' and current_token != 'LESSEQUAL' and current_token != 'GREATEREQUAL'):
        return False
    current_token = get_next_token()
    comp2_node = compared()
    if (comp2_node == False):
        return False
  

def compared():

    global Symbol
    global current_token
    variable_name_loop_node = False
    number_node = None
    fraction_node = None
    UDI_node = None
    function_call_num_node = None
    if not variable_name_loop_node:
        number_node = number()
        fraction_node = None
        UDI_node = None
        function_call_num_node = None
        if not number_node:
            fraction_node = fraction()
            UDI_node = None
            function_call_num_node = None
            if not fraction_node:
                UDI_node = user_defined_identifier()
                function_call_num_node = None
                if not UDI_node:
                    function_call_num_node = False
                    if not function_call_num_node:
                        return False

def main_fucntion():

    global Symbol
    global current_token
    if current_token != 'GO':
        return False
    current_token = get_next_token()
    if current_token != 'LBRACK':
        return False
    current_token = get_next_token()
    body_node = body()
    if body_node != False:
        current_token = get_next_token()
    while(current_token != 'RBRACK'):
        body_node = body()
    if current_token != 'RBRACK':
        return False
    current_token = get_next_token()
    if current_token != 'STOP':
        return False
    print ("main_function")

def return_():

    global Symbol
    global current_token
    if current_token != 'RETURN':
            f = 1
    current_token = get_next_token()
    if (return_expression() != False):
        return_expression_node = return_expression()
        current_token = get_next_token()
    if (f == 0):
        print ("program")


def return_expression():

    global Symbol
    global current_token
    expression_node = expression()
    function_call_node = None
    function_call_num_node = None
    if not expression_node:
        function_call_node = function_call()
        function_call_num_node = None
        if not function_call_node:
            function_call_num_node = function_call_num()
            if not function_call_num_node:
                f = 1
    
def user_defined_identifier():

    global current_token
    if current_token != 'UDISTAT':
            return False
    return current_token

def number():

    global current_token
    if current_token != 'NUMBERSTAT':
            return False
    return current_token

def fraction():

    global current_token
    if current_token != 'FRACTION':
            return False
    return current_token

if __name__ == "__main__":
    
    with open('tokens.txt', 'r') as InputFile:
        for line in InputFile:
            for word in line.split():
                if (cnt == 3 and word != 'SLCOM'):
                    arr.append(word)
                if (cnt > 3):
                    if(word.isdecimal() == False):
                        arrSym.append(word)
                    else:
                        arrLit.append(word)
                cnt = cnt + 1
            cnt = 1
    current_token = arr[0]
    Symbol = arrSym[0]
    Literal = arrLit[0]
   # while (True):
    program()
    constant_declaration()
    constant_declaration()
    constant_declaration()
    typedef_struct_declaration()
    typedef_struct_declaration()
    variable_assignment()
    function_declaration()
    main_fucntion()