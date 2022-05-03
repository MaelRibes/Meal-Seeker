from Meal import *

print("""\n=============================== MEAL SEEKER  ================================ \n\nDo you want to choose un ingredient or a country ? \n""")

loop = True

while loop:
    resp = input("1. Ingredient\n2. Country\n\nAnswer : ")
    if resp == "1":
        loop = False
        make_choice_ingredient()
    if resp == "2":
        loop = False
        make_choice_area()
    else:
        print("\nPlease input a valid answer")
