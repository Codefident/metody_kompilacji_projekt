from lark import Lark

grammars_paths = {
    "simple": "simple_grammar.lark",
    "normal": "python_grammar.lark"
}

with open(grammars_paths["normal"], 'r') as grammar_file:
    grammar = grammar_file.read()

parser = Lark(grammar=grammar)

def parse_python(file_path: str):
    with open(file_path, 'r') as file:
        code = file.read()

    print(f"Parsing {file_path}...")
    tree = parser.parse(code)

    print("Result:")
    print(tree.pretty())


path = "examples/example0.py"
parse_python(path)
