from lark import Lark, exceptions
from lark.indenter import PythonIndenter
from colorama import Fore, Style


def parse_python(file_path: str):

    # get grammar
    with open("python_grammar.lark", 'r') as grammar_file:
        grammar = grammar_file.read()

    # create parser
    parser = Lark(
        grammar=grammar,
        parser="lalr",
        postlex=PythonIndenter()
    )

    with open(file_path, 'r') as file:
        code = file.read()
    code += "\n"
    print(repr(code))
    try:
        tree = parser.parse(code)
        print("\nTree:")
        print(Fore.LIGHTGREEN_EX + tree.pretty() + Fore.RESET)
        return tree
    
    except exceptions.UnexpectedToken as e:
        print(Fore.RED + f"Unexpected token: {Style.BRIGHT + e.token + Style.NORMAL}\nIn line {e.line}, column {e.column}" + Style.RESET_ALL)
        print()

        token_len = len(e.token)
        token_col = e.column
        code_context = e.get_context(code)
        code_colored = code_context[:token_col-1] + Fore.RED + e.token + Fore.RESET + code_context[token_col + token_len-1:]
        print(code_colored)

        print("Expected one of the following:")
        print(Fore.LIGHTCYAN_EX, e.expected, Style.RESET_ALL)
        print()

        return None
