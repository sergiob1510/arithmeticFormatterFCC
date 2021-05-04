def arithmetic_arranger(problems, option=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        psplit = problem.split()

        if psplit[1] != "+" and psplit[1] != "-":
            return "Error: Operator must be '+' or '-'."

        if not psplit[0].isnumeric() or not psplit[2].isnumeric():
            return "Error: Numbers must only contain digits."

        if len(psplit[0]) > 4 or len(psplit[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        operator = psplit[1]
        operand1 = psplit[0]
        operand2 = psplit[2]
        max_operand_size = max(len(operand1), len(operand2))

        if operator == "+":
            solution = int(operand1) + int(operand2)

        elif operator == "-":
            solution = int(operand1) - int(operand2)

        rjusted_operand1 = operand1.rjust(max_operand_size)
        rjusted_operand2 = operand2.rjust(max_operand_size)
        line1 = line1 + "  " + rjusted_operand1 + "    "
        line2 = line2 + operator + " " + rjusted_operand2 + "    "
        line3 = line3 + "-" * (max_operand_size + 2) + "    "
        line4 = line4 + str(solution).rjust(max_operand_size + 2) + "    "

        if option == True:
            output = line1[:-4] + "\n" + line2[:-4] + "\n" + line3[:-4] + "\n" + line4[:-4]
        else:
            output = line1[:-4] + "\n" + line2[:-4] + "\n" + line3[:-4]

    return output