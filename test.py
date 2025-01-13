from lark import Lark, exceptions
from lark.indenter import PythonIndenter
from colorama import Fore
from test_cases import test_cases


grammars_paths = {
    "prev": "grammars/prev_python_grammar.lark",
    "normal": "grammars/python_grammar.lark",
    "full": "grammars/full_python_grammar.lark"
}

with open(grammars_paths["normal"], 'r') as grammar_file:
    grammar = grammar_file.read()

parser = Lark(
    grammar=grammar,
    parser="lalr",
    postlex=PythonIndenter()
)


def run_tests():
    passed, failed, total = 0, 0, 0
    for i, (code, should_pass) in enumerate(test_cases):
        try:
            parser.parse(code + "\n")
            if should_pass:
                print(f"Test {i + 1}: ✅ PASS (Positive accepted) -> {Fore.LIGHTGREEN_EX + code + Fore.RESET}")
                passed += 1
            else:
                print(f"Test {i + 1}: ❌ FAIL (Negative accepted) -> {Fore.LIGHTRED_EX + code + Fore.RESET}")
                failed += 1
        except exceptions.LarkError:
            if should_pass:
                print(f"Test {i + 1}: ❌ FAIL (Positive rejected) -> {Fore.LIGHTGREEN_EX + code + Fore.RESET}")
                failed += 1
            else:
                print(f"Test {i + 1}: ✅ PASS (Negative rejected) -> {Fore.LIGHTRED_EX + code + Fore.RESET}")
                passed += 1
        total += 1
    print("------------------------")
    print(f"Passed {passed}/{total} tests")
    
run_tests()
