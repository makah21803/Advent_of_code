import re

file = open("input_data.txt", "r")

list = file.readlines()


class DisplayDecoding():
    def __init__(self, line):
        self.segment_dict = {"a":"", "b":"", "c":"", "d":"", "e":"", "f":"", "g":""}
        self.digit_dict = {}

        self.input = self.split_input_output(line, output=False) + self.split_input_output(line)
        self.save_unique_digits(self.input)
        self.save_segments()

    def decode_output(self):
        output = []
        for digit in self.input[-4:]:
            digit = ''.join(sorted([self.segment_dict[l] for l in digit]))
            output.append(self.decode_digit(digit))
        return ''.join(output)

    def decode_digit(self, digit):
        if digit == "cf":
            return "1"
        elif digit == "acdeg":
            return "2"
        elif digit == "acdfg":
            return "3"
        elif digit == "bcdf":
            return "4"
        elif digit == "abdfg":
            return "5"
        elif digit == "abdefg":
            return "6"
        elif digit == "acf":
            return "7"
        elif digit == "abcdefg":
            return "8"
        elif digit == "abcdfg":
            return "9"
        elif digit == "abcefg":
            return "0"
        else:
            print("{} not found".format(digit))

    def save_segments(self):

        a = self.get_a(self.digit_dict["1"], self.digit_dict["7"])
        if a is False:
            print('Getting "a" failed')
            return
        self.segment_dict[a] = "a"

        g = self.get_g(self.input, self.digit_dict["4"], self.digit_dict["7"])
        if g is False:
            print('Getting "g" failed')
            return
        self.segment_dict[g] = "g"

        e = self.get_e(self.input, self.digit_dict["4"], self.digit_dict["7"], g)
        if e is False:
            print('Getting "e" failed')
            return
        self.segment_dict[e] = "e"

        b = self.get_b(self.input, self.digit_dict["7"], e, g)
        if b is False:
            print('Getting "b" failed')
            return
        self.segment_dict[b] = "b"

        d = self.get_d(self.input, self.digit_dict["7"], b, e, g)
        if d is False:
            print('Getting "d" failed')
            return
        self.segment_dict[d] = "d"

        f = self.get_f(self.input, a, b, d, e, g)
        if f is False:
            print('Getting "f" failed')
            return
        self.segment_dict[f] = "f"

        c = self.get_c(a, b, d, e, f, g)
        if c is False:
            print('Getting "c" failed')
            return
        self.segment_dict[c] = "c"

    def split_input_output(self, line, output=True):
        display = re.split(" \| ", line)[int(output)]
        digits = [d.strip() for d in re.split(" ", display) if d.strip() != ""]
        return digits

    def is_unique_digit(self, digit):
        if len(digit) in [2, 4, 3, 7]:
            return True
        return False

    def save_unique_digits(self, _input):
        for digit in _input:
            if len(digit) == 2:
                self.digit_dict["1"] = digit
            elif len(digit) == 4:
                self.digit_dict["4"] = digit
            elif len(digit) == 3:
                self.digit_dict["7"] = digit
            elif len(digit) == 7:
                self.digit_dict["8"] = digit
        return

    def get_a(self, one, seven):
        if len(one) == 2 and len(seven) == 3:
            return [l for l in seven if l not in one][0]
        return False

    def get_b(self, _input, seven, e, g):
        if len(seven) != 3 or e =="" or g == "":
            return False
        relevant_inputs = [s for s in _input if len(s) in [6,]]
        for relevant_input in relevant_inputs:
            remaining = [l for l in relevant_input if l not in seven and l not in [e, g]]
            if len(remaining) == 1:
                return remaining[0]
        return False

    def get_c(self, a, b, d, e, f, g):
        if a =="" or b == "" or d =="" or e == "" or f == "" or g == "":
            return False
        return [l for l in "abcdefg" if l not in [a, b, d, e, f, g]][0]

    def get_d(self, _input, seven, b, e, g):
        if len(seven) != 3 or b =="" or e == "" or g == "":
            return False
        relevant_inputs = [s for s in _input if len(s) in [5, 6]]
        for relevant_input in relevant_inputs:
            remaining = [l for l in relevant_input if l not in seven and l not in [b, e, g]]
            if len(remaining) == 1:
                return remaining[0]
        return False

    def get_e(self, _input, four, seven, g):
        if len(four) != 4 or len(seven) != 3 or g == "":
            return False
        relevant_inputs = [s for s in _input if len(s) in [5, 6]]
        for relevant_input in relevant_inputs:
            remaining = [l for l in relevant_input if l not in four and l not in seven and l not in [g,]]
            if len(remaining) == 1:
                return remaining[0]
        return False

    def get_f(self, _input, a, b, d, e, g):
        if a =="" or b == "" or d =="" or e == "" or g == "":
            return False
        relevant_inputs = [s for s in _input if len(s) == 6]
        for relevant_input in relevant_inputs:
            remaining = [l for l in relevant_input if l not in [a, b, d, e, g]]
            if len(remaining) == 1:
                return remaining[0]
        return False

    def get_g(self, _input, four, seven):
        if len(four) != 4 or len(seven) != 3:
            return False
        relevant_inputs = [s for s in _input if len(s) in [5, 6]]
        for relevant_input in relevant_inputs:
            remaining = [l for l in relevant_input if l not in four and l not in seven]
            if len(remaining) == 1:
                return remaining[0]
        return False

total_sum = 0
for line in list:
    digit = int(DisplayDecoding(line).decode_output())
    total_sum += digit


print("The total sum is: {}".format(total_sum))



