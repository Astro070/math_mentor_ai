import sympy as sp

def solve_math(question):
    try:
        x = sp.symbols('x')

        if "derivative" in question.lower():
            expr = question.split("of")[-1].strip()
            expression = sp.sympify(expr)
            result = sp.diff(expression, x)

            return f"The derivative is: {result}"

        elif "integrate" in question.lower():
            expr = question.split("of")[-1].strip()
            expression = sp.sympify(expr)
            result = sp.integrate(expression, x)

            return f"The integral is: {result}"

        else:
            return "I currently support derivative and integration problems."

    except Exception:
        return "Could not solve the problem."