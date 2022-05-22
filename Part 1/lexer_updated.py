import sys
import re

# We create a file, we fill it with white space so it can exist.
open('tokens.txt', 'w').close()

# Literal table is initially empty
literal_table = []
# Symbol table initially contain reserved words.
symbolTable = ['Define', 'program', 'if', 'for', 'default', 'struct', 'typedef', 'return', 'static', 'case', 
               'else', 'int', 'fraction', 'void', 'go', 'stop', 'break', 'True', 'False', 'Print', 'Read']

# This function is going to be our lexer. We will pass to it a line of code each time, and it will 
# extract all tokens found in that line and then print them in "tokens.txt" and to the output screen.

def lexer(line_1, numb):

    # All of those variables are used as flags 
    f = 0
    flag = 0
    flag2 = 0
    yes = 0

    for word in line_1.split():

        # Check if the token is a comment (check for '#')
        f = 0
        flag2 = 0
        regex_pattern = re.compile(r"#")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'SLCOM'
            token_id = 24
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + str(word))
            print("\n")
            # when the flag is 1, this means that a # is encountered, and anything after it will be counted as a comment
            flag = 1

        # Check if there is a left Bracket BEFORE a stream of characters 
        result = re.search("^\[.*", str(word))
        if result:
            token_type = 'LBRACK'
            token_id = 23
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + "[")
            print("\n")

        # Check if there is a left parenthesis BEFORE a stream of characters 
        result = re.search("^\(.*", str(word))
        if result:
            token_type = 'LPAREN'
            token_id = 21
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + "(")
            print("\n")

        # Check if there is a right parenthesis BEFORE a stream of characters 
        result = re.search("^\).*", str(word))
        if result:
            token_type = 'RPAREN'
            token_id = 22
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + ")")
            print("\n")

        # Check if there is a left bracket BEFORE a stream of characters
        result = re.search("^\].*", str(word))
        if result:
            token_type = 'RBRACK'
            token_id = 24
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + "]")
            print("\n")

        # Check if there is a comma (separate) BEFORE a stream of characters
        result = re.search("^\,.*", str(word))
        if result:
            token_type = 'SEPARATE'
            token_id = 20
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + ",")
            print("\n")

        # Check if the token contain an identifier
        regex_pattern = re.compile(r"[a-zA-Z'_']+")
        result = regex_pattern.findall(str(word))
        if result and flag == 0:

            # We set our identifier to contain only letters in additon to well-specifed characters
            res = re.sub('[^a-zA-Z\.\!\?\$\'_]+', '', word)
            if (str(res) == '$Define'):
                token_type = 'DOLLARDEFINE'
                token_id = 28
            elif (str(res) == 'program'):
                token_type = 'PROGRAM'
                token_id = 29
            elif (str(res) == 'if'):
                token_type = 'IF'
                token_id = 30
            elif (str(res) == 'for'):
                token_type = 'FOR'
                token_id = 31
            elif (str(res) == 'default'):
                token_type = 'DEFAULT'
                token_id = 32
            elif (str(res) == 'struct'):
                token_type = 'STRUCT'
                token_id = 33
            elif (str(res) == 'typedef'):
                token_type = 'TYPEDEF'
                token_id = 34
            elif (str(res) == 'return'):
                token_type = 'RETURN'
                token_id = 35
            elif (str(res) == 'static'):
                token_type = 'STATIC'
                token_id = 36
            elif (str(res) == 'case'):
                token_type = 'CASE'
                token_id = 37
            elif (str(res) == 'else'):
                token_type = 'ELSE'
                token_id = 38
            elif (str(res) == 'int'):
                token_type = 'INT'
                token_id = 39
            elif (str(res) == 'fraction'):
                token_type = 'FRACTION'
                token_id = 40
            elif (str(res) == 'void'):
                token_type = 'VOID'
                token_id = 41
            elif (str(res) == 'go'):
                token_type = 'GO'
                token_id = 42
            elif (str(res) == 'stop'):
                token_type = 'STOP'
                token_id = 43
            elif (str(res) == 'break'):
                token_type = 'BREAK'
                token_id = 44
            elif (str(res) == 'True'):
                token_type = 'TRUE'
                token_id = 45
            elif (str(res) == 'False'):
                token_type = 'FALSE'
                token_id = 46
            elif (str(res) == 'print'):
                token_type = 'PRINT'
                token_id = 47
            elif (str(res) == 'read'):
                token_type = 'READ'
                token_id = 48
            else:

                token_type = 'UDISTAT'
                token_id = 1
                # We set our identifier to contain only letters in additon to well-specifed characters
                result = re.sub('[^a-zA-Z\.\!\?\$\'_]+', '', word)
                for char in result:
                    if char == '.':
                        yes = 1
                if yes == 1:
                    new_word = result.split('.')
                    word1 = new_word[0]
                    word2 = new_word[1]
                    yes = 0
                    symbolTable.append(str(word1))
                    symbolTable.append(str(word2))
                    ou = open('tokens.txt', 'a')
                    text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ', str(word1), ' ']
                    ou.writelines(text_list)
                    ou.write("\n")
                    text_list = [str(numb), ' ', str(19), ' ', str('DOT'), ' ']
                    ou.writelines(text_list)
                    ou.write("\n")
                    text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ', str(word2), ' ']
                    ou.writelines(text_list)
                    ou.write("\n")
                    ou.close()
                    print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + str(word1))
                    print("\n")
                    print("line " + str(numb) + " Token" + " #" + str(19) + " : " + '.')
                    print("\n")
                    print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + str(word2))
                    print("\n")
                    f = 1

                else:
                    symbolTable.append(str(result))
                    ou = open('tokens.txt', 'a')
                    text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ', str(result), ' ']
                    ou.writelines(text_list)
                    ou.write("\n")
                    ou.close()
                    print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + str(result))
                    print("\n")
                    f = 1

            if (f == 0):
            # if f = 0 our identifier is a well-defined reserved word 
                ou = open('tokens.txt', 'a')
                text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
                ou.writelines(text_list)
                ou.write("\n")
                ou.close()
                # reserved words can only contain letters and/or the dollar sign
                result = re.sub('[^a-zA-Z\$]+', '', word)
                print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + str(result))
                print("\n")

        # Check if the token contain a number
        regex_pattern = re.compile(r"([0-9]+)")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'NUMBERSTAT'
            token_id = 2
            # A number can only contain digits
            result = re.sub('[^0-9]', '', word)
            literal_table.append(str(result))
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ', str(result), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + str(result))
            print("\n")

        # Check if the token contain a fraction
        regex_pattern = re.compile(r"([0-9]+/[1-9]+)")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'FRACTIONSTAT'
            token_id = 3
            # A fraction can only contain digits and '/'
            result = re.sub('[^0-9\/0-9]', '', word)
            literal_table.append(str(result))
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ', str(result), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + str(result))
            print("\n")

        # Check if the token contain a '+'
        regex_pattern = re.compile(r"\+")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'ADD'
            token_id = 4
            flag2 = 1

        # Check if the token contain a '-'
        regex_pattern = re.compile(r"\-")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'SUB'
            token_id = 5
            flag2 = 1

        # Check if the token contain a '*'
        regex_pattern = re.compile(r"\*")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'MULT'
            token_id = 6
            flag2 = 1

        # Check if the token contain a '/'
        regex_pattern = re.compile(r"\/")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'DIV'
            token_id = 7
            flag2 = 1

        # Check if the token contain a ':'
        regex_pattern = re.compile(r"\:")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'ASSIGN'
            token_id = 8
            flag2 = 1

        # Check if the token contain a '%'
        regex_pattern = re.compile(r"\%")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'MOD'
            token_id = 9
            flag2 = 1

        # Check if the token contain a '&'
        regex_pattern = re.compile(r"\&")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'AND'
            token_id = 10
            flag2 = 1

        # Check if the token contain a '|'
        regex_pattern = re.compile(r"\|")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'OR'
            token_id = 11
            flag2 = 1

        # Check if the token contain a '~'
        regex_pattern = re.compile(r"\~")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'NOT'
            token_id = 12
            flag2 = 1

        # Check if the token contain a '@>'
        regex_pattern = re.compile(r"\@>")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'GREATER'
            token_id = 13
            flag2 = 1

        # Check if the token contain a '@<'
        regex_pattern = re.compile(r"\@<")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'LESS'
            token_id = 14
            flag2 = 1

        # Check if the token contain a '>='
        regex_pattern = re.compile(r"\>=")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'GREATEREQUAL'
            token_id = 15
            flag2 = 1

        # Check if the token contain a '<='
        regex_pattern = re.compile(r"\<=")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'LESSEQUAL'
            token_id = 16
            flag2 = 1

        # Check if the token contain a '=<'
        regex_pattern = re.compile(r"\==")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'CEQUAL'
            token_id = 17
            flag2 = 1

        # Check if the token contain a '!=!'
        regex_pattern = re.compile(r"\!=!")
        result = regex_pattern.findall(str(word))
        if result:
            token_type = 'DIFF'
            token_id = 18
            flag2 = 1

        if (flag2 == 1):
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + str(word))
            print("\n")
        
        # Check if there is a comma (separate) AFTER a stream of characters
        result = re.search("^.+\,$", str(word))
        if result:
            token_type = 'SEPARATE'
            token_id = 20
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + ",")
            print("\n")
        
        # Check if there is a left parenthesis AFTER a stream of characters
        result = re.search("^.+\($", str(word))
        if result:
            token_type = 'LPAREN'
            token_id = 21
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + "(")
            print("\n")
        
        # Check if there is a right parenthesis AFTER a stream of characters
        result = re.search("^.+\)$", str(word))
        if result:
            token_type = 'RPAREN'
            token_id = 22
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + ")")
            print("\n")

        # Check if there is a left bracket AFTER a stream of characters
        result = re.search("^.+\[$", str(word))
        if result:
            token_type = 'LBRACK'
            token_id = 23
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + "[")
            print("\n")

        # Check if there is a right parenthesis AFTER a stream of characters
        result = re.search("^.+\]$", str(word))
        if result:
            token_type = 'RBRACK'
            token_id = 24
            ou = open('tokens.txt', 'a')
            text_list = [str(numb), ' ', str(token_id), ' ', str(token_type), ' ']
            ou.writelines(text_list)
            ou.write("\n")
            ou.close()
            print("line " + str(numb) + " Token" + " #" + str(token_id) + " : " + "]")
            print("\n")

if __name__ == '__main__':
    LineNumber = 1

    # open the file infile.txt which is our text file that will extract tokens from 
    try:
        InputFile = open('infile.txt', 'r')
        InputFile.close()

    except OSError:
        print ("Inexistant Input File")
        sys.exit()

    # We will call the lexer function each time and pass to it the content of the test file line by line
    with open('infile.txt', 'r') as InputFile:
        for line in InputFile:
            lexer(line, LineNumber)
            LineNumber += 1

    # We will fill SymbolTables.txt with the content of the list "symbolTable"
    open('SymbolTables.txt', 'w').close()
    with open('SymbolTables.txt', 'a') as symb:
        for word in symbolTable:
            symb.writelines(word)
            symb.writelines(' ')
    
    # We will fill LiteralTables.txt with the content of the list "literal_table"
    open('LiteralTables.txt', 'w').close()
    with open('LiteralTables.txt', 'a') as lit:
        for word in literal_table:
            lit.writelines(word)
            lit.writelines(' ')