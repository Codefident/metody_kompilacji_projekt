from lark import Lark, Transformer
from lark.indenter import PythonIndenter


grammars_paths = {
    "simple": "grammars/python_simple_grammar.lark",
    "normal": "grammars/python_grammar.lark",
    "full": "grammars/full_python_grammar.lark"
}


def parse_python(file_path: str):

    # get grammar
    with open(grammars_paths["normal"], 'r') as grammar_file:
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

    return parser.parse(code)
