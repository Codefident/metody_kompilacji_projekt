from lark import Transformer
import re


class Py_JS_Transformer(Transformer):
    def __init__(self):
        self.functions = """let range = (start, stop, step) => {
    if (stop === undefined) {
        stop = start;
        start = 0;
    }

    if (step === undefined)
        step = 1;
    else if (step == 0)
        throw new Error("step cannot be 0");

    if ((step > 0 && start >= stop) || (step < 0 && start <= stop))
        return [];

    let result = [];
    for (let i = start; step > 0 ? i < stop : i > stop; i += step)
        result.push(i);
    return result;
}

let len = (obj) => {
    if (typeof obj === "string" || Array.isArray(obj))
        return obj.length
    if (typeof obj === "object")
        return Object.keys(obj).length
    return 0
}

// user code"""
        self.declared_vars = set()    
    
    def start(self, items):
        return f"{self.functions}\n{'\n'.join(items)}"

    def simple_stmt(self, items):
        return "; ".join(items) + ";"
    

    # assignments (with augassigns)

    def assign_stmt(self, items):
        return "".join(items)

    def assign(self, items):
        print(f"assign: {items}")
        var_name, operator, value = items
        let = ""
        if var_name not in self.declared_vars and re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", var_name):
            self.declared_vars.add(var_name)
            let = "let "
        return f"{let}{var_name} = {value};"
    
    def augassign(self, items):
        var_name, op, value = items
        return f"{var_name} {op} {value};"
    
    def assign_target(self, items):
        return "".join(items)

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
    
    def atom_expr(self, items):
        return "".join(items)
    
    def atom(self, items):
        return "".join(items)
    
    def true_(self, _):
        return "true"
    
    def false_(self, _):
        return "false"
    
    def none_(self, _):
        return "null"
    
    def obj_expr(self, items):
        return f"{{{', '.join(items)}}}"
    
    def obj_item(self, items):
        return f"{items[0]}: {items[1]}"

    def list_expr(self, items):
        return f"[{', '.join(items)}]"
    
    def index_access(self, items):
        return f"{items[0]}[{items[1]}]"
    
    def dot_access(self, items):
        return f"{items[0]}.{items[1]}"
    
    def add(self, items):
        return " ".join(items)

    def sub(self, items):
        return " ".join(items)

    def mul(self, items):
        return " ".join(items)

    def div(self, items):
        return " ".join(items)

    def floordiv(self, items):
        return f"Math.floor({items[0]} / {items[2]})"

    def mod(self, items):
        return " ".join(items)
    
    def pow(self, items):
        return f"Math.pow({items[0]}, {items[2]})"
    

    # loops and flow

    def for_stmt(self, items):
        var_name, iterable, body = items
        if "range(" == iterable[:6]:
            args = iterable[6:-1].split(",")
            args = [arg.strip() for arg in args]
            proceed = True
            for arg in args:
                if ")" in arg or "(" in arg:
                    proceed = False
                    break
            if len(args) > 3:
                proceed = False
            if proceed:
                match len(args):
                    case 1:
                        return f"for (let {var_name} = 0; {var_name} < {args[0]}; {var_name}++) {{\n{body}\n}}"
                    case 2:
                        return f"for (let {var_name} = {args[0]}; {var_name} < {args[1]}; {var_name}++) {{\n{body}\n}}"
                    case 3:
                        if int(args[2]) > 0:
                            comp = "<"
                        else:
                            comp = ">"
                        return f"for (let {var_name} = {args[0]}; {var_name} {comp} {args[1]}; {var_name} += {args[2]}) {{\n{body}\n}}"
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

        if "includes" in condition:
            var, test, obj = condition.split(" ")
            if test == "includes":
                return f"if ({obj}.includes({var})) {{\n{body}\n}}{''.join(rest)}"
            else:
                return f"if (!{obj}.includes({var})) {{\n{body}\n}}{''.join(rest)}"

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
        if params is None:
            params = []
        return f"let {func_name} = ({', '.join(params)}) => {{\n{body}\n}}"

    def func_call(self, items):
        full_func_name, args = items
        if args is None:
            args = []

        names: list = full_func_name.split(".")

        match names[-1]:
            case "print":
                names[-1] = "console.log"
            case "append":
                names[-1] = "push"
            case "int":
                names[-1] = "parseInt"
            case "float":
                names[-1] = "parseFloat"
        
        return f"{'.'.join(names)}({', '.join(args)})"

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
    

    # tokens

    def NAME(self, token):
        return token.value

    def NUMBER(self, token):
        return token.value
    
    def negative_number(self, items):
        return f"-{items[0]}"

    def STRING(self, token):
        return token.value
    
    def COMMENT(self, token):
        return f"//{token}"
    
    def LPAR(self, token):
        return token.value
    
    def RPAR(self, token):
        return token.value

    def LBRACE(self, token):
        return token.value

    def RBRACE(self, token):
        return token.value

    def LBRACK(self, token):
        return token.value

    def RBRACK(self, token):
        return token.value

    def COLON(self, token):
        return token.value

    def COMMA(self, token):
        return token.value

    def DOT(self, token):
        return token.value

    def ASSIGN(self, token):
        return token.value

    def ADD_ASSIGN(self, token):
        return token.value

    def SUB_ASSIGN(self, token):
        return token.value

    def MUL_ASSIGN(self, token):
        return token.value

    def DIV_ASSIGN(self, token):
        return token.value

    def MOD_ASSIGN(self, token):
        return token.value

    def ADD(self, token):
        return token.value

    def SUB(self, token):
        return token.value

    def MUL(self, token):
        return token.value

    def DIV(self, token):
        return token.value

    def FLOORDIV(self, token):
        return token.value

    def MOD(self, token):
        return token.value

    def POW(self, token):
        return token.value

    def LT(self, token):
        return token.value

    def GT(self, token):
        return token.value

    def EQ(self, token):
        return token.value

    def GE(self, token):
        return token.value

    def LE(self, token):
        return token.value

    def NE_LEGACY(self, token):
        return token.value

    def NE(self, token):
        return token.value

    def IN(self, token):
        return token.value

    def NOT(self, token):
        return token.value

    def IS(self, token):
        return token.value

    def FOR(self, token):
        return token.value

    def WHILE(self, token):
        return token.value

    def IF(self, token):
        return token.value

    def ELIF(self, token):
        return "else if"

    def ELSE(self, token):
        return token.value
    
    def OR(self, token):
        return "||"

    def DEF(self, token):
        return "function"

    def RETURN(self, token):
        return token.value

    def BREAK(self, token):
        return token.value

    def CONTINUE(self, token):
        return token.value

    def TRUE(self, token):
        return "true"

    def FALSE(self, token):
        return "false"

    def NONE(self, token):
        return "null"

