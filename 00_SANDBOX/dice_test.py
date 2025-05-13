from die import Die

# die_1 = Die()
# die_2 = Die()
# die_3 = Die()
#
# die_3.roll()
# die_2.roll()
#
# print(f"Die 1 is {die_1.get_value()}")
# print(f"Die 2 is {die_2.get_value()}")
# print(f"Die 3 is {die_3.get_value()}")

# print(die_1)
# die_1.roll()
# print(die_1)

dice_list = []
for i in range(8):
    dice_list.append(Die())

for i in range(8):
    dice_list[i].roll()
    print(dice_list[i].get_value())



