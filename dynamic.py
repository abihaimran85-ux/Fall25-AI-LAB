 #AbihaImran
# SU92-BSDSM-F24-006
def solve_expression(expr):expr
     = expr.replace("×", "*")
    expr = expr.replace("÷", "/")
    new_expr = ""
    for i in range(len(expr)):
        if i > 0 and expr[i] == "(" and expr[i-1].isdigit():
            new_expr += "*" + expr[i]
        else:
            new_expr += expr[i]
    expr = new_expr
    result = eval(expr)
    print("Expression:", expr)
    print("Result =", result)

expression = "1+2×3(4-5÷4)-(3÷5)"
solve_expression(expression)
