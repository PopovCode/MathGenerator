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
        random_action = get_random_action(ACTIONS=ACTIONS)

        a = random_operand(lower=LOWER, upper=UPPER)
        b = random_operand(lower=LOWER, upper=UPPER)

        c = calc(a=a, action=random_action, b=b)
        if (c >= 0 and c < UPPER):
            mathTask.append(f"{a} {random_action} {b} = ")
            mathAnswers.append(f"{a} {random_action} {b} = {c}")
            count = count + 1

    save_file(filename='output/txt/MathTasks.txt', list=mathTask)
    save_to_pdf(filename='output/pdf/MathTasks.pdf', list=mathTask, title='Математические операции')

    save_file(filename='output/txt/MathAnswers.txt', list=mathAnswers)
    save_to_pdf(filename='output/pdf/MathAnswers.pdf', list=mathTask, title='Математические операции (Ответы)')


def logical_operations(LOWER, UPPER, AMOUND_TASKS):
    log_operations = []
    count = 0

    while count < AMOUND_TASKS:
        a = random_operand(lower=LOWER, upper=UPPER)
        b = random_operand(lower=LOWER, upper=UPPER)
        log_operations.append(f'{a}          {b}')
        count = count + 1

    save_file(filename='output/txt/LogicalOperations.txt', list=log_operations)
    save_to_pdf(filename='output/pdf/LogicalOperations.pdf', list=log_operations, title="Логические операции")

def save_to_pdf(filename, list, title):
    pdf = FPDF('P', 'mm', format="A4")
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSerifCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 16)
    pdf.cell(200, 10, title, ln=1, align='C')
    print(f'[INFO] {filename} saved.')
    for item in list:
        pdf.cell(10, 15, item, ln=True)
    pdf.output(filename)

def main():
    # Нижняя и верхняя границы чисел (в каком пределе умеем считать)
    LOWER_OPERAND = 1
    UPPER_OPERAND = 20

    # Операции с числами
    ACTIONS = ['+', '-']

    # Количество генерируемых задач
    AMOUND_TASKS = 15

    math_operations(LOWER=LOWER_OPERAND, UPPER=UPPER_OPERAND, ACTIONS=ACTIONS, AMOUND_TASKS=AMOUND_TASKS)
    logical_operations(LOWER=LOWER_OPERAND, UPPER=UPPER_OPERAND, AMOUND_TASKS=AMOUND_TASKS)

if __name__ == "__main__":
    main()