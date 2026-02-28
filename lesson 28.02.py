'''
def black_hole(*args):
    print(f"args = {args}, \n\t type(arg) = {type(args)}")
    for argument in args:
        print(f"{argument} --> {type(argument)}")


black_hole(0,4,6, "25", "name", 2*5, [0, 24])

arg = 0,4,6, "25", "name", 2*5, [0, 24]
print(f"arg = {type(arg)}")

print()

def black_hole_named(**kwargs):
    print(f"kwargs = {kwargs}, \n\t type(kwargs) = {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"key - {key}, value - {value}")


black_hole_named(name="Nick", planet="Earth", school=217, lst=[2, "0"])

kw_arg = {'name': "Nick", 'planet': "Earth", 'school': 217, 'lst': [2, "0"]}
print(f"kw_arg = {kw_arg}, \n\ttype(kw_arg) - {type(kw_arg)}")


def black_hole_full(*args, **kwargs):
    print(f"args - {args}")
    print(f"kwargs - {kwargs}")
    for arg in args:
        print(f"arg - {arg}")
    for key, value in kwargs.items():
        print(f"key - {key}, value - {value}")


black_hole_full(12, 45, ["a", 25], name="Nick", planet="Earth", school=217)


def black_hole_mixed(var_1, var_2=5, *args, **kwargs):
    print(f"var_1 = {var_1}")
    print(f"var_2 = {var_2}")
    for arg in args:
        print(f"arg - {arg}")
    for key, value in kwargs.items():
        print(f"key - {key}, value - {value}")


black_hole_mixed(0.5, name="Nick", planet="Earth", school=217)
black_hole_mixed(0.5, 12, 12, 'strings', 2*5, name="Nick", planet="Earth", school=217)


lst = [60, 3]
tpl = (60, 3)
dct = {"t": 3,"v": 60}

def way(v, t):
    print(f"S = {v} * {t} = {v * t}")

way(*lst)
way(*tpl)
way(**dct)






# f-strings f-рядки
f_name = "Yeva"
l_name = "Yakovets"
school = 217
cls = "9-B"
print("My name is -", f_name, "l_name -", l_name, "school -", school, "cls -", cls)
print(f"My name is - {f_name}, l_name - {l_name}, school - {school}, cls - {cls}")
print(f"My name is - {f_name:8}, l_name - {l_name:15}, school - {school:6}, cls - {cls:6}")
print(f"My name is - {f_name:<8}, l_name - {l_name:^15}, school - {school:>6}, cls - {cls:^6}")
print(f"My name is - {f_name:<8}, l_name - {l_name:_^15}, school - {school::>6}, cls - {cls:*^6}")

day = 28
print(f"Today's day: {day:7d}")

pi = 3.14159265
print(f"pi = {pi:10.3f}")

income = 202356
costs = 143274
profit = income / costs - 1
print(f"profit = {profit:^10.3f}")
print(f"profit = {profit:^10.3%}")
print(f"profit = {(income / costs - 1):^10.3%}")



#format()
f_name = "Yeva"
l_name = "Yakovets"
school = 217
cls = "9-B"
print("My name is -", f_name, "l_name -", l_name, "school -", school)
print("My name - {}, f_name - {}, school - {}.".format(f_name, l_name, school))
print("My name - {:.^10}, f_name - {:.^15}, school - {:_>8d}.".format(f_name, l_name, school))
print("My l_name - {1:^15}, name - {0:^10}, school - {2:_>8}.".format(f_name, l_name, school))

print("Today: {day:.^6} {month:_^16}".format(month="february", day="28"))



#  use --> %
month = "february"
day = 28
print("Today: %d %s" % (day, month))
day = "second"
s_bool = True
print("Today: %s %s" % (day, month))


#     \t - табуляція(4 пробіла)     \n - перехід на новий рядок
print("За час нашого навчання ми постійно стикалися з рядками.")
print("За час нашого навчання\n ми постійно\n стикалися з рядками.")
print("За час нашого навчання\n ми постійно\n стикалися з рядками.")
print("За час нашого навчання\n\t\t ми постійно\n\t\t\t стикалися з рядками.")
'''

print(" Nothing\n will work\n unless you do")

print('"Anyone who\n\t stops learning is old,\n\t whether at twenty or eighty"\n\t Henry Ford')

print('"Success is not the key to happiness.\n\tHappiness\n\t\t is\n\t\t\t the\n\t\t\t\t key\n\t\t\t\t\t to\n\t\t\t\t\t\t success."')