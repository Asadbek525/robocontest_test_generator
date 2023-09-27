lang = open('lang.txt', 'r').read().strip()
import re
code = ''
if lang == 'python3' or lang == 'pypy':
    pattern = re.compile(r"(while|for|if|switch\s*\()")
    if pattern.search(code):
        print("Error: The code contains a while/for/if/switch statement.")
        exit(171)

    #check user used abs and min and max functions
    pattern = re.compile(r"(abs|min|max|eval|exec)\s*\(")

    # check user used ** operator
    if '**' in code:
        print('Error: ** operator is not allowed')
        exit(171)
    
    # check user used lambda
    pattern = re.compile(r"\\blambda\\b")
    if pattern.search(code):
        print('Error: Lambda functions are not allowed')
        exit(171)

        
    # check user used def and class
    pattern = re.compile(r"\\b(def|class)\\b")
    if pattern.search(code):
        print('Error: Defining functions and classes are not allowed')
        exit(171)
        
    # check user used yield and return
    pattern = re.compile(r"\\b(yield|return)\\b")
    if pattern.search(code):
        print('Error: Returning and yielding are not allowed')
        exit(171)
    pattern = re.compile("(\\[|\\]|\\{|\\})")
    if pattern.search(code):
        print('Error: Arrays and dictionaries are not allowed')
        exit(171)



if lang == 'cpp':
    with open('code.txt', 'r') as f:
        code = f.read()
        
    pattern = re.compile(r"(while|if|for|switch)\s*\(")
    if pattern.search(code):
        print('Error: Loops and conditions are not allowed')
        exit(171)
    
    pattern = re.compile("#include\\s+<(?!iostream)[^>]+>")
    if pattern.search(code):
        print('Error: The code includes a library other than iostream.')
        exit(171)
        
    #check user used abs, min, max
    pattern = re.compile(r"(abs|min|max|fabs)\s*\(")
    if pattern.search(code):
        print('Error: Restricted built-in function used')
        exit(171)
        
    # check user used goto
    pattern = re.compile(r"\\bgoto\\b")
    if pattern.search(code):
        print('Error: goto is not allowed')
        exit(171)
    
    # check user used compare operators
    pattern = re.compile(r"\\b(==|!=|<=|>=|<|>)\\b")
    if pattern.search(code):
        print('Error: Comparing operators are not allowed')
        exit(171)
    
# check user used array and dictionary
pattern = re.compile("(\\[|\\]|\\{|\\})")
if pattern.search(code):
    print('Error: Arrays and dictionaries are not allowed')
    exit(171)
    
# check user used bitwise operators
pattern = re.compile("(&|\\||\\^|~)")
if pattern.search(code):
    print('Error: Bitwise operators are not allowed')
    exit(171)
    
# check user used logical operators
pattern = re.compile("(\\band\\b|\\bor\\b|\\bnot\\b)")
if pattern.search(code):
    print('Error: Logical operators are not allowed')
    exit(171)
    
# check user used && and ||
pattern = re.compile("(\\|\\||&&)")
if pattern.search(code):
    print('Error: Logical operators are not allowed')
    exit(171)
