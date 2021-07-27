import random
from fpdf import FPDF


def save_file(filename, list):
    file = open(filename, 'w')
    for line in list:
        file.write(line + '\n')
    file.close()
    print(f'[INFO] {filename} saved.')

def random_operand(lower, upper):
    return random.randint(lower, upper)

def calc(a, action, b):
    if action == "+":
        return a+b
    elif action == "-":
        return a-b

def get_random_action(ACTIONS):
    return ACTIONS[random.randint(0, len(ACTIONS) - 1)]

def math_operations(LOWER, UPPER, ACTIONS, AMOUND_TASKS):
    mathTask = []
    mathAnswers = []
    count = 0

    while count < AMOUND_TASKS:
        random_action = get_random_action(ACTIONS)

        a = random_operand(lower=LOWER, upper=UPPER)
        b = random_operand(lower=LOWER, upper=UPPER)

        c = calc(a, random_action, b)
        if (c >= 0 and c < UPPER):
            mathTask.append(f"{a} {random_action} {b} = ")
            mathAnswers.append(f"{a} {random_action} {b} = {c}")
            count = count + 1

    save_file('MathTasks.txt', mathTask)
    save_file('MathAnswers.txt', mathAnswers)

def logical_operations(LOWER, UPPER, AMOUND_TASKS):
    log_operations = []
    count = 0

    while count < AMOUND_TASKS:
        a = random_operand(lower=LOWER, upper=UPPER)
        b = random_operand(lower=LOWER, upper=UPPER)
        log_operations.append(f'{a}          {b}')
        count = count + 1

    save_file('LogicalOperations.txt', log_operations)
    save_to_pdf('LogicalOperations.pdf', log_operations)

def save_to_pdf(filename, list):
    pdf = FPDF('P', 'mm', 'Letter')
    pdf.add_page()
    pdf.set_font('helvetica', '', 16)
    pdf.cell(100,10, 'Logical', ln=1, align='C')
    for item in list:
        pdf.cell(100, 15, item, ln=True)
    pdf.output(filename)

def main():
    # Нижняя и верхняя границы чисел (в каком пределе умеем считать)
    LOWER_OPERAND = 1
    UPPER_OPERAND = 20

    # Операции с числами
    ACTIONS = ['+', '-']

    # Количество генерируемых задач
    AMOUND_TASKS = 20

    math_operations(LOWER_OPERAND,UPPER_OPERAND, ACTIONS, AMOUND_TASKS)
    logical_operations(LOWER_OPERAND, UPPER_OPERAND, AMOUND_TASKS)



if __name__ == "__main__":
    main()