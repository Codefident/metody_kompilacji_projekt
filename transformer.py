from lark import Transformer, Tree


class py_js_transformer(Transformer):
    def __init__(self):
        self.range_function = "function range(n) { return Array.from({ length: n }, (_, i) => i); }"
        self.declared_vars = set()    
    
    def start(self, items):
        return f"{self.range_function}\n\n{'\n'.join(items)}"

    def simple_stmt(self, items):
        return "; ".join(items) + ";"
    

    # assignments (with augassigns)

    def assign_stmt(self, items):
        return "".join(items)

    def assign(self, items):
        var_name, value = items
        let = ""
        if var_name not in self.declared_vars:
            self.declared_vars.add(var_name)
            let = "let "
        return f"{let}{var_name} = {value};"
    
    def augassign(self, items):
        var_name, op, value = items
        return f"{var_name} {op} {value};"

    def aug_add(self, _):
        return "+="
    
    def aug_sub(self, _):
        return "-="
    
    def aug_mul(self, _):
        return "*="
    
    def aug_div(self, _):
        return "/="
    
    def aug_mod(self, _):
        return "%="
    

    # exprs and operators

    def expr(self, items):
        return " ".join(items)

    def list_expr(self, items):
        return f"[{', '.join(items)}]"
    
    def add(self, items):
        return f"({items[0]} + {items[1]})"

    def sub(self, items):
        return f"({items[0]} - {items[1]})"

    def mul(self, items):
        return f"({items[0]} * {items[1]})"

    def div(self, items):
        return f"({items[0]} / {items[1]})"

    def floordiv(self, items):
        return f"Math.floor({items[0]} / {items[1]})"

    def mod(self, items):
        return f"({items[0]} % {items[1]})"
    

    # loops and flow

    def for_stmt(self, items):
        var_name, iterable, body = items
        return f"for (let {var_name} of {iterable}) {{\n{body}\n}}"

    def while_stmt(self, items):
        condition, body = items
        return f"while ({condition}) {{\n{body}\n}}"

    def break_stmt(self, _):
        return "break;"

    def continue_stmt(self, _):
        return "continue;"

    def return_stmt(self, items):
        return f"return {items[0] if items else ''};"
    

    # ifs and tests

    def if_stmt(self, items):
        condition, body, *rest = items

        for i in range(len(rest)):
            if rest[i] is None:
                rest[i] = ''

        return f"if ({condition}) {{\n{body}\n}}{''.join(rest)}"

    def elif_(self, items):
        condition, body = items
        return f" else if ({condition}) {{\n{body}\n}}"
    
    def else_(self, items):
        return f" else {{\n{''.join(items)}\n}}"
    
    def or_test(self, items):
        return f"{items[0]} || {items[1]}"
    
    def and_test(self, items):
        return f"{items[0]} && {items[1]}"
    
    def not_test(self, items):
        return f"!{''.join(items)}"


    # functions

    def func_def(self, items):
        func_name, params, body = items
        return f"function {func_name}({', '.join(params)}) {{\n{body}\n}}"

    def func_call(self, items):
        func_name, args = items
        if func_name == "print":
            func_name = "console.log"
        return f"{func_name}({', '.join(args)})"

    def params(self, items):
        return items

    def arguments(self, items):
        return items
    

    # indented block of code

    def block(self, items):
        return "\n".join(items)


    # comparisons

    def comparison(self, items):
        left, op, right = items
        return f"{left} {op} {right}"

    def comp_op(self, token):
        return token.value

    def lower_than(self, _):
        return "<"

    def greater_than(self, _):
        return ">"

    def equals(self, _):
        return "=="

    def greater_or_equals(self, _):
        return ">="

    def lower_or_equals(self, _):
        return "<="

    def not_equals(self, _):
        return "!="

    def not_equals_legacy(self, _):
        return "!="

    def in_operator(self, _):
        return "includes"

    def not_in_operator(self, _):
        return "!includes"

    def is_operator(self, _):
        return "==="

    def is_not_operator(self, _):
        return "!=="
    

    # other tokens

    def NAME(self, token):
        value = token.value
        match token.value:
            case "True":
                value = "true"
            case "False":
                value = "false"
            case "None":
                value = "null"
        return value

    def NUMBER(self, token):
        return token.value

    def STRING(self, token):
        return token.value
    
    def COMMENT(self, token):
        print("COMMENT")
        return f"//{token}"
