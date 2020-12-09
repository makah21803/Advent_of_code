import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = [row.strip() for row in file.readlines()]


class Program():

    def __init__(self):
        self.call_dict = {'acc': self.acc, 'jmp': self.jmp, 'nop': self.nop}

        self.next_line = 0
        self.acc_value = 0
        self.code = list

    def run(self):
        line = self.next_line
        if self.code[line] == '':
            print('Validation reached the end of the code. The final value of acc is: {}'.format(self.acc_value))
            return

        arg = self.code[line].split(' ')[1]
        call = self.code[line].split(' ')[0]

        self.call_dict[call](arg)

    def acc(self, arg):
        self.acc_value = self.addition(self.acc_value, arg)
        self.next_line += 1
        self.run()

    def jmp(self, arg):
        self.next_line = self.addition(self.next_line, arg)
        self.run()

    def nop(self, arg):
        self.next_line += 1
        self.run()

    def addition(self, original_value, value):
        sign = value[0]
        for s in ('+', '-'):
            value = value.replace(s, '')
        value = int(value)

        if sign == '+':
            return original_value + value
        elif sign == '-':
            return original_value - value
        else:
            print('Attempt for an unknown operation: {}'.format(sign))
            return


class Validator(Program):

    def __init__(self):
        self.used_lines = []
        self.fix_number = 0
        self.orig_code = list
        self.testing_loop = False
        self.fixed = False
        super(Validator, self).__init__()

    def reset_init(self):
        self.used_lines = []
        self.next_line = 0
        self.acc_value = 0

    def run(self):
        line = self.next_line
        try:
            self.code = self.new_code
        except:
            print('No new_code')

        if self.code[line] in ('', '\n', None) or line >= len(self.code):
            print('\nValidation reached the end of the code. The final value of acc is: {}'.format(self.acc_value))
            self.testing_loop = False
            return True

        if line in self.used_lines:
            print('Infinite loop at {} commands ending on line: {} \nThe current value of acc is: {}'.format(len(self.used_lines), line, self.acc_value))
            self.fix_loop()
            return

        self.log_line()

        arg = self.code[line].split(' ')[1]
        call = self.code[line].split(' ')[0]

        self.call_dict[call](arg)

    def log_line(self):
        self.used_lines.append(self.next_line)

    def fix_loop(self):
        if self.testing_loop:
            return

        possible_changes = {'jmp':'nop', 'nop':'jmp'}
        self.testing_loop = True

        self.orig_lines = self.used_lines
        for n, line_num in enumerate(self.orig_lines):
            if self.testing_loop:
                line_to_fix = self.orig_code[line_num]
                print('changed line {}'.format(line_num))
                change_selected = line_to_fix.split(' ')[0]
                if change_selected in possible_changes:
                    new_line = '{} {}'.format(possible_changes[change_selected], line_to_fix.split(' ')[1])
                    print('Fix attempt #{}: \nfrom {} to {}'.format(n, line_to_fix, new_line))
                    self.new_code = [new_line if line_num == i else line for i, line in enumerate(self.orig_code)]
                    self.reset_init()
                    self.run()
                    if not self.testing_loop:
                        return
                    else:
                        print('Fix attempt #{}: {}'.format(n, line_to_fix))
                        continue
                else:
                    print('Fix attempt #{}: {}'.format(n, line_to_fix))
                    continue


validate = True
if validate:
    Validator().run()
else:
    Program().run()
