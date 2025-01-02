from parser import parse_python
from transformer import py_js_transformer


input_file_path = "examples/is_prime.py"

tree = parse_python(input_file_path)
print(tree.pretty())
print()
# gen = tree.iter_subtrees_topdown()
# for cos in gen:
#     print(cos)
#     print()

transformer = py_js_transformer()
js_code = transformer.transform(tree)
print()
print(js_code)

with open("output.js", "w") as file:
    file.write(js_code)
