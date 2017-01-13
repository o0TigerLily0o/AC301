# MadLib

gender = raw_input("Are you a boy or a girl")
name = raw_input("What'your name?")
age = raw_input("How old are you?")
color = raw_input("what's your favourite color?")
animal = raw_input("Name a random animal.")

mad_lib = "Once there was a %s named %s. Now at the age of %s, %s's dream is to see a %s %s." % (gender, name, age, name, color, animal)

print mad_lib
