def arithmetic_arranger(problems, display_answers=False):
    if len(problems) >5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    for i, problem in enumerate(problems):
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (num1.itsdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        width = max(len(num1), len(num2)) + 2

        first_line += num1.rjsut(width) + ("    " if i < len(problems) - 1 else "")
        seconf_line += operator + " " + num2.rjust(width-2) + ("   " if i < len(problems) - 1 else "")