import sys
from parser import parse_python
from transformer import Py_JS_Transformer
from colorama import Fore, Style


input_file_path = "examples/is_prime.py"
if len(sys.argv) > 1:
    input_file_path = sys.argv[1]

tree = parse_python(input_file_path)

if tree is None:
    message = f"Sorry, couldn't parse {Style.BRIGHT + input_file_path + Style.NORMAL}"
    print(Fore.RED + message + Style.RESET_ALL)

else:
    transformer = Py_JS_Transformer()
    js_code = transformer.transform(tree)

    with open("output.js", "w") as file:
        file.write(js_code)

    message = f"Finished transforming {Style.BRIGHT + input_file_path + Style.NORMAL}, check out your transformed code in {Style.BRIGHT + 'output.js' + Style.NORMAL} file!"
    print(Fore.CYAN + message + Style.RESET_ALL)
