# GWLProgrammingLanguage (Python RegEx)

In partial fulfillment of the CSC 3315 (Languages and Compilers Course), I coded a simple (but comprehensive) high-level programming language that is heavily inspired from C and Pascal. 

The Green World Language (GWL) designed for the Green World application, aims to allow a programmer to construct and change a world constructed of objects such as block, tub, and plant. The GWL has also some primitive operations, and a bunch of constraints that must hold between objects. Other language elements include Definitions/Declarations, Statements, Reserved Words, Punctuation, etc.

**The parts from 1 to 3 refer to the Milestones of the Project.**

- In *PART 1* : Lexical Description using regular expression + Specifying Tokens and the grammar using EBNF
               + Implementing a working **LEXER**
- In *PART 2* : Implementing a working **PARSER** (Acceptor + Tree Constructor). 
- In *PART 3* : Syntactic and static semantics analysis + Implementing a **GENERATOR** for Code Generation.

<img width="526" alt="Screenshot 2022-05-23 at 01 27 13" src="https://user-images.githubusercontent.com/103124512/169723040-a1e7bc0c-8395-44ac-b8b4-5a04739e6d9a.png"> 

<ins>PART 1</ins>

<img width="575" alt="Screenshot 2022-05-23 at 01 36 24" src="https://user-images.githubusercontent.com/103124512/169723503-74af8ef0-2add-431c-b013-4c712f32394e.png">

| Tokens | Grammar |
| :---: | :---: |
| <img width="473" alt="Screenshot 2022-05-23 at 01 37 30" src="https://user-images.githubusercontent.com/103124512/169723544-00e1fb7e-254d-4023-ade9-e1308ac9e458.png"> ... | <img width="457" alt="Screenshot 2022-05-23 at 01 38 33" src="https://user-images.githubusercontent.com/103124512/169723604-dcaa05d9-3743-422e-982a-b20743633dff.png"> ...|

Lexical Analysis is the very first phase in the compiler designing. The Lexer will scan the input file "infile.txt" and then break it into small units that matches the tokens that we have specified earlier. In other words, it will convert the sequence of characters in the input file into a sequence of tokens while discarding all whitespaces and comments. N.B. The lexer won’t be able to recognize the input if it has the right tokens in the wrong combinations.

The Lexer will operate by filling two tables: the symbol table and the literal table. Any symbol such as the reserved words and user defined identifiers will be stored in the symbol table. The table of literals will contain typically strings literals: any constant that has been declared in the input program. The tokens gotten form the lexer are then sent to the parser to generate a parse tree, for the input, from the language grammar. Normally, the lexical analyzer should generate an error if it encounters, during the tokenizing process, an invalid token, but to stay in simplicity and accuracy, the Lexer will be given only inputs which contain tokens that can be identified in our language. 

The Lexer will produce an output file “token_streams.txt” that will contain the token stream in the following format:

 ```
 line_number  token_id  token_value
 ```
A particular output that will be shown in the user screen will be printed in the following format: 

```
Line (line_number) Token #(token_id) : token_value
```

| An Actual Output Returned By the Lexer |
| :---: |
| <img width="181" alt="Screenshot 2022-05-23 at 02 36 18" src="https://user-images.githubusercontent.com/103124512/169727275-56b40b12-4f7f-483f-a4f8-14c8fc7abf74.png"> 
...|

<ins>PART 2</ins>

Parser is a compiler that is used to break the data into smaller elements coming from lexical analysis phase. The input file to the parser is the token file (tokens.txt) generated by the lexer (part 2). The output will contain the trees of both the main program and all other subprograms apparent in the main program.

**Parser Output Format - Examples**

| Example 1 | Example 2 | Example 3 | Example 4 |
| :---: | :---: | :---: | :---: |
| <img width="594" alt="Screenshot 2022-05-23 at 02 13 16" src="https://user-images.githubusercontent.com/103124512/169725657-4cea37cc-a919-46d0-af26-7c5968121ed7.png"> | <img width="568" alt="Screenshot 2022-05-23 at 02 13 35" src="https://user-images.githubusercontent.com/103124512/169725677-b2d6c947-2f68-4480-a8f7-eeffac90186b.png"> | <img width="620" alt="Screenshot 2022-05-23 at 02 14 04" src="https://user-images.githubusercontent.com/103124512/169725710-a378b051-9e0b-49df-8067-539c3d78785c.png"> | <img width="737" alt="Screenshot 2022-05-23 at 02 14 26" src="https://user-images.githubusercontent.com/103124512/169725734-43a0b107-9502-4236-a651-a8e2562f8603.png"> |

Parser Actual Output : Tree Generated for "infile.txt"

<img width="563" alt="Screenshot 2022-05-23 at 02 30 50" src="https://user-images.githubusercontent.com/103124512/169726862-d1e13a2d-b216-4f59-8452-f3c6a3f523fa.png">
...


<ins>PART 3</ins>

**Static Semantic Analysis**

The output of the parser is a Concrete Syntax Tree (CST). This kind of tree which follows the structure of the grammar and is useful for doing type checking, because the semantic rules follow the syntactic rules closely, allowing you to label the CST with type information and check for type conflicts. Nevertheless, we don’t need to do type checking as we have a simple type system and we’ll assume that the programs is written without any type issues.

The static semantic has as role to make sure that all parameters used in the function call match with the formal parameters of a function definition. Also, it should assure that all the variables are declared before being used.

The content of the symbol table was initialized to contain all the reserved words. It has information about the scope that an identifier occurs in.

For Code generation, we will generate code using as target language a simple assembly-like language under the name og GWAL

**GAWL generator:**

-	Input File: program1.txt, program2.txt, program3.txt (to be found in File Part 3).
-	Output Files:

| Output for "program1.txt" |
| :---: |
|<img width="392" alt="Screenshot 2022-05-23 at 02 50 25" src="https://user-images.githubusercontent.com/103124512/169728470-9941ba53-f9e9-409a-985c-55fc7e0b8f42.png">|

| Output for "program2.txt" ||
| :---: | :---: |
| Stopping Without Error | Stopping With Error |
|<img width="302" alt="image" src="https://user-images.githubusercontent.com/103124512/169728728-7c2d0c30-81e2-4b58-aabe-fb89170bdb89.png">| <img width="345" alt="image" src="https://user-images.githubusercontent.com/103124512/169728754-3055ffcd-25f8-4c55-8621-e6e62390c7c6.png"> |

| Output for "program3.txt" |
| :---: |
| <img width="360" alt="image" src="https://user-images.githubusercontent.com/103124512/169728786-764a958c-592b-473c-8874-efa9341572a9.png"> |







