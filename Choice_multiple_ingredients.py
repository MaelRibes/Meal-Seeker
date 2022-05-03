from Meal import *

def make_choice_ingredients():
    inter = True
    list_ingredients = get_list_ingredients()
    choice = []

    while inter:
        index = 1
        print("""\nChoose 3 or fewer ingredients (input the ingredient number, 0 if you choose nothing)\n""")
        print("0. Nothing")
        for i in list_ingredients:
            print(str(index) + ". " + i)
            index += 1
        list_ingredients.append("Nothing")
        print("")
        for c in range(1, 4):
            value = int(input("Choice n°" + str(c) + " : "))
            if value == 0:
                value = 575
            choice.append(list_ingredients[value-1])

        print("\nYou choose : " + choice[0] + ", " + choice[1] + " and " + choice[2])
        choice = set(choice)

        commut = False
        for c in choice:
            if c == "Nothing":
                commut = True

        if commut:
            choice.remove("Nothing")

        print(len(choice))
        json = get_json("https://www.themealdb.com/api/json/v1/1/filter.php?i=chicken_breast,garlic,salt")
        print(json)
        ans = input("What would you like to do? ")
        if ans == "1":

            inter = False
        elif ans == "2":

            inter = False
        elif ans == "3":
            print("\n Goodbye")
            ans = None
            inter = False
        else:
            print("\n Not Valid Choice Try again \n")

