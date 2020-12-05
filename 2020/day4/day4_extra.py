import re

file = open("2020/day4/input_data.txt", "r")

list = file.readlines()

passports = []
passport_dict = {}
for line in list:
    if line == "\n":
        passports.append(passport_dict)
        passport_dict = {}
        continue
    parts = str(line).split(" ")
    for field in parts:
        field_name = str(field.split(":")[0])
        field_value = field.split(":")[1]
        field_value = re.sub("\n$", "", field_value)
        if field_name != "cid":
            passport_dict[field_name] = field_value

# passports.append(passport_dict)

count = 0
for passport in passports:
    if len(passport) >= 7:
        valid = True
        for field in sorted(passport):
            if field == "byr":
                value = int(passport[field])
                if value < 1920 or value > 2002 or len(passport[field]) > 4:
                    valid = False
                    
            elif field == "iyr":
                value = int(passport[field])
                if value < 2010 or value > 2020 or len(passport[field]) > 4:
                    valid = False
                    
            elif field == "eyr":
                value = int(passport[field])
                if value < 2020 or value > 2030 or len(passport[field]) > 4:
                    valid = False
                    
            elif field == "hgt":
                value = passport[field]
                if re.search('cm$', value):
                    value = int(re.sub('cm$', '', value))
                    if value < 150 or value > 193:
                        valid = False
                elif re.search('in$', value):
                    value = int(re.sub('in$', '', value))
                    if value < 59 or value > 76:
                        valid = False
                else:
                    valid = False

            elif field == "hcl":
                value = str(passport[field])
                if not re.search('^#[0-9a-f]', value) or len(value)!=7:
                    valid = False

            elif field == "ecl":
                value = str(passport[field])
                if value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    valid = False
            
            elif field == "pid":
                value = str(passport[field])
                if len(value) == 9:
                    try:
                        v = int(value)
                    except:
                        valid = False
                else:
                    valid = False
                # todo: why this didnt work?
                if re.search('0-9', value) and len(value) != 9:
                    continue
                else:
                    valid = False

            elif field == "cid":
                continue
            
            else:
                valid = False
            
        if valid:
            print ('len: {} \n {}'.format(len(passport), passport))
            count += 1


print('finished, answer is: {}'.format(count))
