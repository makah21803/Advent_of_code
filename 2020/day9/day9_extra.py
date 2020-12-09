import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = [row.strip() for row in file.readlines()]

preamble_lenght = 25

class Validate():

    def __init__(self):
        self.preamble = [int(list[i]) for i in range(preamble_lenght)]
        self.code = [int(line) for i, line in enumerate(list) if i >= preamble_lenght]

    def run(self):
        for entry in self.code:
            if not self.condition(entry):
                print('Found a value of {} which is not allowed.'.format(entry))
                self.fix(entry)
                return

            self.preamble.pop(0)
            self.preamble.append(entry)
        print('Validated, all seems fine.')

    def condition(self, value):
        allowed_values = self.get_all_additions(self.preamble)
        if value not in allowed_values:
            return False
        return True

    def get_all_additions(self, numbers):
        used_numbers = []
        additions = []
        for num in numbers:
            for pnum in used_numbers:
                addition = num + pnum
                if addition not in additions:
                    additions.append(addition)
            used_numbers.append(num)

        return additions

    def fix(self, invalid_entry):
        fix_found = False
        code_all = [int(line) for i, line in enumerate(list)]
        for e, entry in enumerate(code_all):
            sum = 0
            sum_elements = []
            for i in range(len(code_all)-e):
                next_number = code_all[e+i]
                sum += next_number
                sum_elements.append(next_number)
                if sum == invalid_entry and len(sum_elements) > 1:
                    fix_found = True
                    break
                elif sum > invalid_entry:
                    break

            if fix_found:
                answer = min(sum_elements) + max(sum_elements)
                print('Fix found, the sum of min and max is: {}'.format(answer))
                return
                break
        print('Fix not found.')


Validate().run()
