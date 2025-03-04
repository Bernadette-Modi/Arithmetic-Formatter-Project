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
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        width = max(len(num1), len(num2)) + 2

        first_line += num1.rjust(width) + ("    " if i < len(problems) - 1 else "")
        second_line += operator + " " + num2.rjust(width-2) + ("   " if i < len(problems) - 1 else "")
        dashes += "-" * width + ("   " if i < len(problems) - 1 else "")

        if display_answers:
            result = str(eval(problem))
            answers += result.rjust(width) + ("   " if i < len(problems) - 1 else "")
    
    arranged_problems = first_line + "\n" + second_line + "\n" + dashes
    if display_answers:
        arranged_problems += "\n" + answers
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))