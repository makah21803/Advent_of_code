
import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
test_file = open(dirname+"/test_data.txt", "r")

input_list = [line.strip() for line in file.readlines()]
# input_list = [line.strip() for line in test_file.readlines()]



class Monkeys():
    def __init__(self, input_monkeys, managing_stress=True):
        self.monkeys = {}
        self.managing_stress = managing_stress
        self.common_denominator = 1

        for line in input_monkeys:
            if line[:6] == "Monkey":
                monkey = int(line[-2])
                self.monkeys[monkey] = {}
                continue
            line_bits = line.split(":")
            if line_bits[0].strip() == "Starting items":
                self.monkeys[monkey]["items"] = ([int(item.strip()) for item in line_bits[-1].split(",")])
            elif line_bits[0].strip() == "Operation":
                self.monkeys[monkey]["op"] = ([step.strip() for step in line_bits[-1].strip().split(" ") if step not in ['new', '=']])
            elif line_bits[0].strip() == "Test":
                self.monkeys[monkey]["test"] = (int(line_bits[-1].split(" ")[-1].strip()))
            elif line_bits[0].strip() == "If true":
                self.monkeys[monkey]["send_to"] = ([int(line_bits[-1].split(" ")[-1].strip()),])
            elif line_bits[0].strip() == "If false":
                self.monkeys[monkey]["send_to"].append(int(line_bits[-1].split(" ")[-1].strip()))
            else:
                self.monkeys[monkey]["inspected"] = 0

        for divider in [self.monkeys[monkey]["test"] for monkey in self.monkeys]:
            self.common_denominator *= divider

        # print("Initial state:")
        # for monkey in self.monkeys:
        #     print(f"Monkey {monkey}: {self.monkeys[monkey]}")

    def calculate_distress(self, a, operation, b, old):
        a = int(a) if a != "old" else old
        b = int(b) if b != "old" else old
        if operation == "+":
            return a + b
        elif operation == "*":
            return a * b
        return False

    def reduce_distress(self, distress):
        if self.managing_stress:
            distress = distress //3
        return distress % self.common_denominator

    def throwing(self, rounds):
        for round_n in range(rounds):
            for monkey in self.monkeys:
                for i in range(len(self.monkeys[monkey]["items"])):
                    item = self.monkeys[monkey]["items"].pop(0)
                    self.monkeys[monkey]["inspected"] += 1
                    distress = self.calculate_distress(self.monkeys[monkey]["op"][0],
                                                       self.monkeys[monkey]["op"][1],
                                                       self.monkeys[monkey]["op"][2],
                                                       item)

                    distress = self.reduce_distress(distress)
                    send_to = self.monkeys[monkey]["send_to"][int(distress % self.monkeys[monkey]['test'] != 0)]
                    # print(f"Monkey {monkey} thrown item {distress} to monkey {send_to}")
                    self.monkeys[send_to]["items"].append(distress)

            # if (round_n+1) % 1000 == 0:
            #     print(f"\nRound {round_n+1}:")
            #     self.print_state()

    def calculate_monkey_business(self):
        monkey_inspections = [self.monkeys[monkey]["inspected"] for monkey in self.monkeys]
        monkey_inspections.sort()
        return monkey_inspections[-1] * monkey_inspections[-2]

    def print_state(self):
        for monkey in self.monkeys:
            print(f"Monkey {monkey} inspected {self.monkeys[monkey]['inspected']} times.")

    def run(self, rounds):
        self.throwing(rounds)
        return self.calculate_monkey_business()


monkey_business = Monkeys(input_list)
print(f"\nPart One: \nThe Monkey business level at the end is {Monkeys(input_list).run(20)}")
print(f"\nPart Two: \nThe Monkey business level at the end is {Monkeys(input_list, managing_stress=False).run(10000)}")

