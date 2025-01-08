from parser import parse_python
from transformer import Py_JS_Transformer


input_file_path = "examples/example0.py"

tree = parse_python(input_file_path)
print(tree.pretty())

transformer = Py_JS_Transformer()
js_code = transformer.transform(tree)

with open("output.js", "w") as file:
    file.write(js_code)
