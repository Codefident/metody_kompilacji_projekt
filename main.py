from parser import parse_python
from transformer import Py_JS_Transformer


input_file_path = "examples/example0.py"

tree = parse_python(input_file_path)
print(tree.pretty())
# gen = tree.iter_subtrees_topdown()
# for cos in gen:
#     print(cos)
#     print()

transformer = Py_JS_Transformer()
js_code = transformer.transform(tree)
print()
print(js_code)

with open("output.js", "w") as file:
    file.write(js_code)
