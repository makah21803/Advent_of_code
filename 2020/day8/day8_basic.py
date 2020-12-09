import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname + "/input_data.txt", "r")

list = file.readlines()


class Program():
    CODE = list

    def __init__(self):
        self.call_dict = {'acc': self.acc, 'jmp': self.jmp, 'nop': self.nop}

        self.next_line = 0
        self.acc_value = 0

    def run(self):
        line = self.next_line
        if self.CODE[line] == "\n":
            print('Validation reached the end of the code. The final value of acc is: {}'.format(self.acc_value))
            return

        arg = self.CODE[line].split(' ')[1]
        call = self.CODE[line].split(' ')[0]

        self.call_dict[call](arg)

    def log_line(self):
        self.used_lines.append(self.next_line)

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
        self.fix_number = 1
        super(Validator, self).__init__()

    def run(self):
        line = self.next_line

        if line in self.used_lines:
            print('Infinite loop at line: {} \nThe current value of acc is: {}'.format(line, self.acc_value))
            return False

        if line == "\n":
            print('Validation reached the end of the code. The final value of acc is: {}'.format(self.acc_value))
            return True

        self.log_line()
        if line >= len(self.CODE):
            print('Next line out of code range.')
            return False

        super(Validator, self).run()


validate = True
if validate:
    Validator().run()
else:
    Program().run()