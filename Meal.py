from random import randint
import requests


def get_json(url):  # retourne le json d'une page à partir de son url
    response = requests.get(url)
    json = response.json()
    json_content = json['meals']
    return json_content


def get_json_id(idMeal):  # retourne le json d'un plat à partir de son id
    url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + idMeal
    json_recipes = get_json(url)[0]
    return json_recipes


def get_list_ingredients():  # retourne la liste de tous les ingrédients présents sur le site
    list_ingredient = []
    json_ingredient = get_json("https://www.themealdb.com/api/json/v1/1/list.php?i=list")
    for i in json_ingredient:
        list_ingredient.append(i['strIngredient'])
    return list_ingredient


def get_list_area():  # retourne la liste de tous les pays ou régions présents sur le site
    list_area = []
    json_area = get_json("https://www.themealdb.com/api/json/v1/1/list.php?a=list")
    for a in json_area:
        list_area.append(a['strArea'])
    return list_area


def get_list_category():  # retourne la liste de toutes les catégories présentes sur le site
    list_category = []
    json_category = get_json("https://www.themealdb.com/api/json/v1/1/list.php?c=list")
    for c in json_category:
        list_category.append(c['strCategory'])
    return list_category


def get_instruction(json):  # retourne les instructions d'une recette en prenant son json en paramètre
    instructions = json['strInstructions']
    return instructions


def get_ingredients(json):  # retourne les ingrédients et quantités d'une recette en prenant son json en paramètre
    ingredients = {}
    for i in range(1, 21):
        indice_ingr = "strIngredient" + str(i)
        indice_measure = "strMeasure" + str(i)
        ingr = json[indice_ingr]
        measure = json[indice_measure]
        if (ingr != "") or (measure != ""):
            ingredients[ingr] = measure
    return ingredients


def get_meal_name(json):  # retourne le nom d'une recette en prenant son json en paramètre
    name = json["strMeal"]
    return name


def display_meal(idMeal):  # affiche une recette en fonction de son id
    json = get_json_id(idMeal)
    instructions = get_instruction(json)
    ingredients = get_ingredients(json)
    name = get_meal_name(json)

    print("""\n=========================== """ + name + """ ============================ \n\nYou will need : \n""")
    for i in ingredients.items():
        print(i[0] + " : " + i[1])

    print("""\n\nInstructions : \n\n""" + instructions)


def make_choice_ingredient():  # Permet de choisir un ingrédient et d'afficher une recette aléatoire avec cet ingrédient.
    inter = True
    list_ingredients = get_list_ingredients()
    choice = ""

    while inter:
        loop = True
        index = 1
        print("""\nPlease choose a main ingredient (input the ingredient number)\n""")

        for i in list_ingredients:
            print(str(index) + ". " + i)
            index += 1
        print("")
        value = int(input("Choice : "))
        choice = list_ingredients[value-1]
        print("\nYou choose : " + choice + "\n")
        json = get_json("https://www.themealdb.com/api/json/v1/1/filter.php?i=" + choice)
        while loop:
            question = True
            nb = randint(0, len(json)-1)
            meal = json[nb]
            idMeal = meal["idMeal"]
            display_meal(idMeal)

            while question:
                quest = True
                resp = input("\nDo you want to try another meal ?\n\n1. Yes\n2. No\n\nAnswer : ")

                if resp == "2":
                    question = False
                    loop = False
                    inter = False
                    print("Bon appétit !")

                elif resp == "1":
                    question = False

                    while quest:
                        r = input("\nWith the same ingredient ?\n\n1. Yes\n2. No\n\nAnswer : ")
                        if r == "2":
                            loop = False
                            quest = False
                        if r == "1":
                            quest = False
                        else:
                            print("Please input a valid answer")

                else:
                    print("\nPlease input a valid answer")


def make_choice_area():  # Permet de choisir un pays et d'afficher une recette aléatoire provenant de ce pays.
    inter = True
    list_area = get_list_area()
    choice = ""

    while inter:
        loop = True
        index = 1
        print("""\nPlease choose country (input the country number)\n""")

        for i in list_area:
            print(str(index) + ". " + i)
            index += 1
        print("")
        value = int(input("Choice : "))
        choice = list_area[value - 1]
        print("\nYou choose : " + choice + "\n")
        json = get_json("https://www.themealdb.com/api/json/v1/1/filter.php?a=" + choice)
        while loop:
            question = True
            nb = randint(0, len(json) - 1)
            meal = json[nb]
            idMeal = meal["idMeal"]
            display_meal(idMeal)

            while question:
                quest = True
                resp = input("\nDo you want to try another meal ?\n\n1. Yes\n2. No\n\nAnswer : ")

                if resp == "2":
                    question = False
                    loop = False
                    inter = False
                    print("Bon appétit !")

                elif resp == "1":
                    question = False

                    while quest:
                        r = input("\nWith the same country ?\n\n1. Yes\n2. No\n\nAnswer : ")
                        if r == "2":
                            loop = False
                            quest = False
                        if r == "1":
                            quest = False
                        else:
                            print("Please input a valid answer")

                else:
                    print("\nPlease input a valid answer")





