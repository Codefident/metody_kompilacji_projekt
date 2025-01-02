from lark import Lark
from lark.indenter import PythonIndenter

# get grammar
grammars_paths = {
    "normal": "python_grammar.lark",
    "full": "python.lark"
}

with open(grammars_paths["normal"], 'r') as grammar_file:
    grammar = grammar_file.read()


# create parser
parser = Lark(
    grammar=grammar,
    parser="lalr",
    postlex=PythonIndenter()
)


def parse_python(file_path: str):
    with open(file_path, 'r') as file:
        code = file.read()
    code += "\n"

    print(f"Parsing {file_path}...")
    tree = parser.parse(code)

    print("Result:")
    print(tree.pretty())


path = "examples/example0.py"
parse_python(path)
