# PART 1
# with open("day11_input.txt", "r") as file:
    
#     """ SAMPLE INPUT
#     Monkey 0:
#     Starting items: 62, 92, 50, 63, 62, 93, 73, 50
#     Operation: new = old * 7
#     Test: divisible by 2
#         If true: throw to monkey 7
#         If false: throw to monkey 1
    
#     Monkey 1:
#     """

#     monkeys = []
#     current_monkey = {}

#     for line in file:

#         line = line.strip().split(":")
        
#         if line == [""]:
#             if current_monkey: monkeys.append(current_monkey)
#             current_monkey = {}
#         else: current_monkey[line[0].strip()] = line[1].strip()

# for monkey in monkeys:
    
#     # items
#     stack = []
#     prev = monkey["Starting items"].split(",")
#     for item in prev: stack.append(int(item))
#     monkey["Starting items"] = stack[::-1]
    
#     # operation
#     op = monkey["Operation"].split(" ")[-2:]
#     if op[-1].isdigit(): op[-1] = int(op[-1])
#     monkey["Operation"] = op

#     # test
#     test = ["%"]
#     test.append(int(monkey["Test"].split(" ")[-1]))
#     monkey["Test"] = test

#     # if true / if false
#     if_true = int(monkey["If true"].split(" ")[-1])
#     if_false = int(monkey["If false"].split(" ")[-1])
#     monkey["If false"], monkey["If true"] = if_false, if_true

#     monkey["Total inspections"] = 0
#     print(monkey)
    

# for round in range(1, 21):
    
#     # {'Monkey 0': '', 'Starting items': [98, 79], 'Operation': ['*', 19], 'Test': ['%', 23], 'If true': 2, 'If false': 3}
#     for monkey in monkeys:
        
#         while monkey["Starting items"]:
#             curr_item = monkey["Starting items"].pop()
#             curr_item = eval(f'{curr_item} {monkey["Operation"][-2]} { monkey["Operation"][-1] if type(monkey["Operation"][-1]) == int else curr_item}')
#             curr_item = curr_item // 3
#             monkey["Total inspections"] += 1

#             if (curr_item // monkey["Test"][-1]) == (curr_item / monkey["Test"][-1]):
#                 monkeys[monkey["If true"]]["Starting items"].append(curr_item)
#                 print(f"{curr_item} is thrown to monkey {monkey['If true']}")
#             else:
#                 monkeys[monkey["If false"]]["Starting items"].append(curr_item)
#                 print(f"{curr_item} is thrown to monkey {monkey['If false']}")
    
#     print("Round: ", round)
#     for monkey in monkeys:
#         print(monkey["Starting items"])
    
# totals = []

# for i in range(len(monkeys)):
#     totals.append(monkeys[i]["Total inspections"])

# print(totals)
# totals = sorted(totals, reverse=True)
# print(totals)
# print(totals[0] * totals[1])


# PART 2

with open("day11_input.txt", "r") as file:
    
    """ SAMPLE INPUT
    Monkey 0:
    Starting items: 62, 92, 50, 63, 62, 93, 73, 50
    Operation: new = old * 7
    Test: divisible by 2
        If true: throw to monkey 7
        If false: throw to monkey 1
    
    Monkey 1:
    """

    monkeys = []
    current_monkey = {}

    for line in file:

        line = line.strip().split(":")
        
        if line == [""]:
            if current_monkey: monkeys.append(current_monkey)
            current_monkey = {}
        else: current_monkey[line[0].strip()] = line[1].strip()

for monkey in monkeys:
    
    # items
    stack = []
    prev = monkey["Starting items"].split(",")
    for item in prev: stack.append(int(item))
    monkey["Starting items"] = stack[::-1]
    
    # operation
    op = monkey["Operation"].split(" ")[-2:]
    if op[-1].isdigit(): op[-1] = int(op[-1])
    monkey["Operation"] = op

    # test
    test = ["%"]
    test.append(int(monkey["Test"].split(" ")[-1]))
    monkey["Test"] = test

    # if true / if false
    if_true = int(monkey["If true"].split(" ")[-1])
    if_false = int(monkey["If false"].split(" ")[-1])
    monkey["If false"], monkey["If true"] = if_false, if_true

    monkey["Total inspections"] = 0
    print(monkey)

modulator = 1
for monkey in monkeys:
    modulator *= (modulator * monkey["Test"][-1])

print(modulator)

for round in range(1, 10001):
    
    # {'Monkey 0': '', 'Starting items': [98, 79], 'Operation': ['*', 19], 'Test': ['%', 23], 'If true': 2, 'If false': 3}
    for monkey in monkeys:
        
        while monkey["Starting items"]:
            curr_item = monkey["Starting items"].pop()
            curr_item = eval(f'{curr_item} {monkey["Operation"][-2]} { monkey["Operation"][-1] if type(monkey["Operation"][-1]) == int else curr_item}')

            monkey["Total inspections"] += 1
            curr_item = curr_item % modulator

            if curr_item % monkey["Test"][-1] == 0:
                monkeys[monkey["If true"]]["Starting items"].append(curr_item)
            else:
                monkeys[monkey["If false"]]["Starting items"].append(curr_item)
                
    
    # 
    if round in [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
        print("Round: ", round)
        for monkey in monkeys:
            print(monkey["Total inspections"])
    
totals = []

for i in range(len(monkeys)):
    totals.append(monkeys[i]["Total inspections"])

print(totals)
totals = sorted(totals, reverse=True)
print(totals)
print(totals[0] * totals[1])

