
print ('\n\t\t\t---------<CONCRETE SYNTAX TREE>----------\n\n\n')


def program(reservedNode:str , name: str):
    
        print('  <program> ------ ' + reservedNode)
        print('\n\t    ------ '+'<program_name>----- ' + name+'\n')

def typeDefstructDeclarationNodeSTART(ReservedNode1: str, ReservedNode2: str, LbrackNode: str):

        print('\t    ----- <typeDefstruct_declaration> ----- ' + ReservedNode1)
        print('\n\t\t\t\t\t      ------ ' + ReservedNode2)
        print('\n\t\t\t\t\t      ------ ' + LbrackNode)
        print('\n')

def typeDefstructDeclarationNodeEND(RbrackNode: str, UserDefinedNode: str):        
        
        print('\n\t\t\t\t\t      '+'------ ' + RbrackNode)
        print('\n\t\t\t\t\t      ----- <UserDefinedDatatype> ------ ' + UserDefinedNode)
        print('\n')
        
def VarDeclarationNode(SimpleType: str, UserDefinedNode: str, flag: int):
    
        tab = ''
        if (flag == 0):
            print('\t    ----- <variable_declaration> -----<simple_type> ------' + SimpleType)
            print('\n')
            print('\t\t\t\t         ----- <var_name> ------ ' + UserDefinedNode)
            print('\n')
        else:
            b = flag
            while(b > 0):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print(tab + '      ----- <variable_declaration> -----<simple_type> ------' + SimpleType)
            print('\n')
            b = flag
            tab = ''
            while(b > 0):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print(tab + '\t\t\t\t   ----- <var_name> ------ ' + UserDefinedNode)
            print('\n')
 
def VarAssignmentNode(UserDefinedNode: str, Assigned_element: str, element: str, flag: int):
    
        tab = ''
        if (flag == 0):
            print('\t    ----- <variable_assignment> -----<var_name> ------' + UserDefinedNode)
            print('\n')
            print('\n\t\t\t\t\t-----' + Assigned_element)
            print('\n')
            print('\n\t\t\t\t\t----- <var_value> ------ ' + element)
            print('\n')
        else:
            b = flag
            print('\n')
            while(b > 0):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print(tab + '      ----- <variable_assignment> -----<var_name> ------ ' + UserDefinedNode)
            print('\n')
            print(tab + '\t\t\t\t   -----' + Assigned_element)
            print('\n')
            print(tab + '\t\t\t\t   ----- <var_value> ------ ' + element)
            print('\n')
            
def VarAssignmentNode2(UserDefinedNode: str, Assigned_element: str, element: str, ope: str, element2: str, flag: int):
    
        tab = ''
        if (flag == 0):
            print('\t    ----- <variable_assignment> -----<var_name> ------' + UserDefinedNode)
            print('\n')
            print('\n\t\t\t\t\t-----' + Assigned_element)
            print('\n')
            print('\n\t\t\t\t\t----- <var_value> ------ ' + element)
            print('\n')
            print('\n\t\t\t\t\t                  ------ ' + ope)
            print('\n')
            print('\n\t\t\t\t\t                  ------ ' + element2)
            print('\n')
        else:
            b = flag
            print('\n')
            while(b > 0):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print(tab + '      ----- <variable_assignment> -----<var_name> ------ ' + UserDefinedNode)
            print('\n')
            print(tab + '\t\t\t\t   -----' + Assigned_element)
            print('\n')
            print(tab + '\t\t\t\t   ----- <var_value> ------ ' + element)
            print('\n')
            print(tab + '\t\t\t\t                     ------ ' + ope)
            print('\n')
            print(tab + '\t\t\t\t                     ------ ' + element2)
            print('\n')
        
def constDeclarationNode(ReservedNode: str, UserDefinedNode: str,NumLiteralNode: str):
        print('\t    ----- <constant_declaration> -----' + ReservedNode)
        print('\n\t\t\t\t\t ----- <cst_name> ------ ' + UserDefinedNode)
        print('\n\t\t\t\t\t ----- <value> ------ ' + NumLiteralNode)
        print('\n')
        
def functionDeclarationNodeSTART(ReservedNode: str, UserDefinedNode: str, LParenNode: str):
        print('\t    ----- <function_declaration> -----<return_ype> ------ ' + ReservedNode)
        print('\n\t\t\t\t\t ----- <function_name> ------ ' + UserDefinedNode)
        print('\n\t\t\t\t\t ----------- ' + LParenNode)
        print('\n')
        
def functionDeclarationNodeMID(RParenNode: str, LbrackNode: str):
        print('\n\t\t\t\t\t----------- ' + RParenNode)
        print('\n\t\t\t\t\t----------- ' + LbrackNode)
        
def functionDeclarationNodeEND(RbrackNode: str, Return: str):
        print('\n\t\t\t\t\t----------- ' + RbrackNode)
        print('\n\t\t\t\t\t----- <return> ------ ' + Return)
        
def functionDeclarationNumSTART(SimpleTypenode: str, UserDefinedNode: str, LParenNode: str):
        print('\t    ----- <function_declaration> -----<return_ype> ------ ' + SimpleTypenode)
        print('\n\t\t\t\t\t ----- <function_name> ------ ' + UserDefinedNode)
        print('\n\t\t\t\t\t ----------- ' + LParenNode)
        print('\n')
        
def functionDeclarationNumMID(RParenNode: str, LbrackNode: str):
        print('\n\t\t\t\t\t----------- ' + RParenNode)
        print('\n\t\t\t\t\t----------- ' + LbrackNode)
        
def functionDeclarationNumEND(RbrackNode: str, Return: str):
        print('\n\t\t\t\t\t----------- ' + RbrackNode)
        print('\n\t\t\t\t\t----- <return> ------ ' + Return)
        
def selctionNodeSTART(ReservedNode: str, LParenNode: str, flag: int):
    
        tab = ''
        if (flag == 0):
            print('\t    ----- <Selection> -----' + ReservedNode)
            print('\n\t\t\t\t\t--------- ' + LParenNode)
        else:
            b = flag
            while(b > 1):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print('\n')
            print(tab + '----- <Selection> -----' + ReservedNode)
            print('\n')
            print(tab + '\t\t  --------- ' + LParenNode)

            
def selctionNodeMID(RParenNode: str, LbrackNode: str, flag: int):
    
        tab = ''
        if (flag == 0):
            print('\n\t\t\t\t\t----------- ' + RParenNode)
            print('\n\t\t\t\t\t----------- ' + LbrackNode)
        else:
            b = flag
            while(b > 1):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print('\n')
            print(tab + '\t\t  --------- ' + RParenNode)
            print('\n')
            print(tab + '\t\t  --------- ' + LbrackNode)

def selctionNodeEND(RbrackNode: str, flag: int):
    
        tab = ''
        if (flag == 0):
            print('\n\t\t\t\t\t----------- ' + RbrackNode)
        else:
            b = flag
            while(b > 1):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print('\n')
            print(tab + '\t\t  --------- ' + RbrackNode)
        
def selctionNodeElseSTART(ReservedNode: str, LbrackNode: str, flag: int):
    
        tab = ''
        if (flag == 0):
            print('\n\t\t\t\t\t----- <Else> -----' + ReservedNode)
            print('\n\t\t\t\t\t             -----' + LbrackNode)
        else:
            b = flag
            while(b > 1):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print('\n')
            print(tab + '\t\t  ----- <Else> -----' + ReservedNode)
            print('\n')
            print(tab + '\t\t\t       --------- ' + LbrackNode)

def selctionNodeElseEND(RbrackNode: str, flag: int):
        
        tab = ''
        if (flag == 0):
            print('\n\t\t\t\t\t             -----' + RbrackNode)
        else:
            b = flag
            while(b > 1):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print('\n')
            print(tab + '\t\t\t       --------- ' + RbrackNode)
            
def PrintNode(UserDefinedNode: str, flag: int):
        
        tab = ''
        if (flag == 0):
            print('\n\t\t\t\t\t----- <Print> -----' + UserDefinedNode)
        else:
            b = flag
            while(b > 1):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print('\n')
            print(tab + '\t\t\t       ----- <Print> -----' + UserDefinedNode)

        
def functioncallNode(UserDefinedNode: str, LbrackNode: str, UserDefinedNode2: str):
    
        print('\t\t\t\t              ----- <Function CAll> ----- ' + UserDefinedNode)
        print('\n\t\t\t\t\t\t\t            ----- ' + LbrackNode)
        print('\n\t\t\t\t\t\t\t            ----- ' + UserDefinedNode2)
        
        
def functioncallNodeMID(Sep: str, UserDefinedNode: str):
    
        print('\n\t\t\t\t\t\t\t            ----- ' + Sep)
        print('\n\t\t\t\t\t\t\t            ----- ' + UserDefinedNode)
        
def functioncallNodeEND(RparenNode: str):
    
        print('\n\t\t\t\t\t\t\t            ----- ' + RparenNode)
        
        #for statements
        #objFile = open("file.txt", "r")
        #with open ("file.txt", "r") as objFile:
           # for line in objFile:
              #  print('\t\t\t\t\t' +line.strip() + '\n\t\t\t')
        
        #print('\n\t\t\t\t\t----------- ' + RParenNode)
        
        
def comparisonNode(UserDefinedNode1: str, symbol: str, UserDefinedNode2: str, flag: int): 
    
        tab = ''
        if (flag == 0):
            print('\n\t\t\t\t\t--------<Name>---- ' + UserDefinedNode1)
            print('\n\t\t\t\t\t----------- ' + symbol)
            print('\n\t\t\t\t\t--------<Name>---- ' + UserDefinedNode2)
        else:
            b = flag
            while(b > 1):
                tab = tab + '\t\t\t\t\t'
                b = b -1
            print('\n')
            print(tab + '\t\t  --------<Name>---- ' + UserDefinedNode1)
            print('\n')
            print(tab + '\t\t  ----------- ' + symbol)
            print('\n')
            print(tab + '\t\t  --------<Name>---- ' + UserDefinedNode2)
        
def Conditional_Statement(ReservedNode: str):
    
        print('\n\t\t\t\t\t----------- ' + ReservedNode)
        
def main_functionSTART(ReservedNode1: str, ReservedNode2: str):

    print('\n')
    print('\t    ----- <main_function> ----- ' + ReservedNode1)
    print('\n\t\t\t\t  ------ ' + ReservedNode2)

def main_functionEND(ReservedNode1: str, ReservedNode2: str):
    
    print('\n\t\t\t\t  ------ ' + ReservedNode1)
    print('\n\t\t\t\t  ------ ' + ReservedNode2)