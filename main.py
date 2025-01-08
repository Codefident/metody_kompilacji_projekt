import sys
from parser import parse_python
from transformer import Py_JS_Transformer


input_file_path = "examples/is_prime.py"
if len(sys.argv) > 1:
    input_file_path = sys.argv[1]

tree = parse_python(input_file_path)
print(tree.pretty())

transformer = Py_JS_Transformer()
js_code = transformer.transform(tree)

with open("output.js", "w") as file:
    file.write(js_code)

print("\n============================================================")
print(f"Finished, check out your transformed code in output.js file!\n")
