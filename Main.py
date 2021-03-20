"""Meal Planner with Recipes"""
__author__ = "Kristopher Marlow"
# Program is intended to plan out meals for the day and perform
# arithmetic on differing potential values within the recipes

# Created 20210201 for use within COP 1500.  Finished 2021----.
import time  # import time for slowing down the program's progression


def insert_separator(times):
    """Creates a separator line as needed throughout the program. The 'times' parameter is passed to change the
    length of the separator as needed. Function also slows down the progression of the program"""
    print("---" * times)
    time.sleep(1)


def main():
    repeat = True
    run_count = 1
    while repeat:
        for number in range(5, 0, -1):
            print(number, end="\n")
            time.sleep(1)
        if run_count > 1:
            print("Let's Continue!")
        else:
            print("Let's Begin!")
        insert_separator(10)
        print("Hello!  I am here to assist you with your meal choices today.", end="\n")
        print("Up first is selecting which meal options you would like for today", end="\n")
        insert_separator(10)
        print(
            "Breakfast Options:")
        # I would like to alter the way this functions.  Currently I plan to import modules with
        # the recipe information and variables, but there has to be a better method.
        print("1. Eggs, Bacon, and Toast")
        print("2. French Toast")
        breakfast_choice = int(input(
            "Which option would you like for breakfast? (Choose by Number): "))  # Storing breakfast choice for later
        insert_separator(10)
        print("Lunch Options:")
        print("1. Grilled Cheese and Tomato Soup")
        print("2. Grilled Chicken Salad")
        lunch_choice = int(
            input("Which option would you like for lunch? (Choose by Number): "))  # Storing lunch choice for later
        insert_separator(10)
        print("Dinner Options:")
        print("1. Grilled Chicken with Rice and Vegetables")
        print("2. Beef Stew")
        dinner_choice = int(
            input("Which option would you like for dinner? (Choose by Number): "))  # Storing dinner choice for later
        insert_separator(10)
        print("Your choices for meals are: ")
        insert_separator(10)
        print("Breakfast:")
        breakfast_calories = 0  # set to have a baseline for the variable.
        lunch_calories = 0  # set to have a baseline for the variable.
        dinner_calories = 0  # set to have a baseline for the variable.
        if breakfast_choice == 1:
            print("Eggs, Bacon, and Toast")
            breakfast_calories = (90 * 2) + (45 * 5) + (75 * 2)
            # Calories for each of the ingredients * pieces for 1 serving size.
            # Parentheses unnecessary, but it makes it easier to differentiate to me.
            print("Calories: " + str(breakfast_calories) + " per serving")  # concat text and str of a numeric variable
        elif breakfast_choice == 2:
            print("French Toast")
            breakfast_calories = 149 * 2
            print("Calories: " + str(breakfast_calories) + " per serving")  # concat text and str of a numeric variable
        elif breakfast_choice < 1:
            print("No selection was entered")
        else:
            print("Selected choice not within list")
        insert_separator(10)
        print("Lunch:")
        if lunch_choice == 1:
            print("Grilled Cheese and Tomato Soup")
            lunch_calories = (75 * 2) + (104 * 2) + (217 * 1)
            # Calories for each of the ingredients * pieces for 1 serving size.  Parentheses unnecessary,
            # but it makes it easier to differentiate to me.
            print("Calories: " + str(lunch_calories) + " per serving")  # concat txt with the str of a numeric variable
        elif lunch_choice == 2:
            print("Grilled Chicken Salad")
            lunch_calories = (68 * 4) + (5 * 1) + (26 * 1) + (73 * 2)
            # Calories for each of the ingredients * pieces for 1 serving size.  Parentheses unnecessary,
            # but it makes it easier to differentiate to
            print("Calories: " + str(lunch_calories) + " per serving")  # concat txt with the str of a numeric variable
        elif lunch_choice < 1:
            print("No selection was entered")
        else:
            print("Selected choice not within list")
        insert_separator(10)
        print("Dinner:")
        if dinner_choice == 1:
            print("Grilled Chicken with Rice and Vegetables")
            dinner_calories = 0  # Test Number.  To be adjusted.
            print("Calories: " + str(dinner_calories) + " per serving")  # concat txt with the str of a numeric variable
        elif dinner_choice == 2:
            print("Beef Stew")
            dinner_calories = 0  # Test Number.  To be adjusted.
            print("Calories: " + str(dinner_calories) + " per serving")  # concat txt with the str of a numeric variable
        elif dinner_choice < 1:
            print("No selection was entered")
        else:
            print("Selected choice not within list")
        total_calories = breakfast_calories + lunch_calories + dinner_calories
        print("Total calories for today: " + str(total_calories) + " per serving")  # Sum of each meal's calories
        insert_separator(10)
        print(
            "Thank you for your selections.  Please answer the following questions regarding your meals")
        # used to break up input sections and explain the clarifying questions of the user.
        breakfast_serving_size = 0  # set to have a baseline for the variable.
        lunch_serving_size = 0  # set to have a baseline for the variable.
        dinner_serving_size = 0  # set to have a baseline for the variable.
        if breakfast_choice >= 1:
            breakfast_serving_size = int(input(
                "How many people will be partaking in breakfast?: "))  # used to see how to adjust per serving size
        else:
            ''
        if lunch_choice >= 1:
            lunch_serving_size = int(input(
                "How many people will be partaking in lunch?: "))  # used to see how to adjust per serving size
        else:
            ''
        if dinner_choice >= 1:
            dinner_serving_size = int(input(
                "How many people will be partaking in dinner?: "))  # used to see how to adjust per serving size
        else:
            ''
        daily_calories = (
                (breakfast_calories * breakfast_serving_size) +
                (lunch_calories * lunch_serving_size) +
                (dinner_calories * dinner_serving_size)
        )
        print("Total calories for today's meals: ", daily_calories, sep='')  # Sum of each meal's calories
        insert_separator(10)
        insert_separator(10)
        print("Recipes")  # This section should list out the selected recipes
        insert_separator(10)
        if breakfast_choice == 1:
            import egg_bacon_toast  # set the import of the recipes

            # I would like to find a better way than the below
            print(str(int(egg_bacon_toast.breakfast_ingredient_1_num) * breakfast_serving_size)
                  + " " + egg_bacon_toast.breakfast_ingredient_1)
            print(str(int(egg_bacon_toast.breakfast_ingredient_2_num) * breakfast_serving_size)
                  + " " + egg_bacon_toast.breakfast_ingredient_2)
            print(str(int(egg_bacon_toast.breakfast_ingredient_3_num) * breakfast_serving_size)
                  + " " + egg_bacon_toast.breakfast_ingredient_3)
            print(str(int(egg_bacon_toast.breakfast_ingredient_4_num) * breakfast_serving_size)
                  + " " + egg_bacon_toast.breakfast_ingredient_4)
            insert_separator(5)
            print(egg_bacon_toast.breakfast_recipe)
        elif breakfast_choice == 2:
            import french_toast  # set the import of the recipes
            print(str(int(french_toast.breakfast_ingredient_1_num) * breakfast_serving_size)
                  + " " + french_toast.breakfast_ingredient_1)
            print(str(int(french_toast.breakfast_ingredient_2_num) * breakfast_serving_size)
                  + " " + french_toast.breakfast_ingredient_2)
            print(str(int(french_toast.breakfast_ingredient_3_num) * breakfast_serving_size)
                  + " " + french_toast.breakfast_ingredient_3)
            print(str(int(french_toast.breakfast_ingredient_4_num) * breakfast_serving_size)
                  + " " + french_toast.breakfast_ingredient_4)
            insert_separator(5)
            print(french_toast.breakfast_recipe)
        else:
            print("No valid breakfast selected.")
        insert_separator(10)
        print("Lunch:")
        if lunch_choice == 1:
            import grilled_cheese_with_tomato_soup  # set the import of the recipes
            print(str(int(grilled_cheese_with_tomato_soup.lunch_ingredient_1_num) * lunch_serving_size)
                  + " " + grilled_cheese_with_tomato_soup.lunch_ingredient_1)
            print(str(int(grilled_cheese_with_tomato_soup.lunch_ingredient_2_num) * lunch_serving_size)
                  + " " + grilled_cheese_with_tomato_soup.lunch_ingredient_2)
            print(str(int(grilled_cheese_with_tomato_soup.lunch_ingredient_3_num) * lunch_serving_size)
                  + " " + grilled_cheese_with_tomato_soup.lunch_ingredient_3)
            print(str(int(grilled_cheese_with_tomato_soup.lunch_ingredient_4_num) * lunch_serving_size)
                  + " " + grilled_cheese_with_tomato_soup.lunch_ingredient_4)
            insert_separator(5)
            print(grilled_cheese_with_tomato_soup.lunch_recipe)
        elif lunch_choice == 2:
            import grilled_chicken_salad  # set the import of the recipes
            print(str(int(grilled_chicken_salad.lunch_ingredient_1_num) * lunch_serving_size)
                  + " " + grilled_chicken_salad.lunch_ingredient_1)
            print(str(int(grilled_chicken_salad.lunch_ingredient_2_num) * lunch_serving_size)
                  + " " + grilled_chicken_salad.lunch_ingredient_2)
            print(str(int(grilled_chicken_salad.lunch_ingredient_3_num) * lunch_serving_size)
                  + " " + grilled_chicken_salad.lunch_ingredient_3)
            print(str(int(grilled_chicken_salad.lunch_ingredient_4_num) * lunch_serving_size)
                  + " " + grilled_chicken_salad.lunch_ingredient_4)
            insert_separator(5)
            print(grilled_chicken_salad.lunch_recipe)
        else:
            print("No valid lunch selected.")
        insert_separator(10)
        # Commenting out Dinner for sprint 2
        # print("Dinner:")
        # if dinner_choice == 1:
        # 	import chicken_rice_vegetables  # set the import of the recipes
        #
        # 	print(chicken_rice_vegetables.dinner_ingredients)
        # 	insert_separator(5)
        # 	print(chicken_rice_vegetables.dinner_recipe)
        # elif dinner_choice == 2:
        # 	import beef_stew  # set the import of the recipes

        # 	print(beef_stew.dinner_ingredients)
        # 	insert_separator(5)
        # 	print(beef_stew.dinner_recipe)
        # else:
        # 	print("No valid dinner selected.")
        # insert_separator(10)
        # insert_separator(10)
        repeat_program = input("Would you like to rerun the program? Y/N ")
        if (
            repeat_program == "N"
            or repeat_program == "n"
            or repeat_program == "No"
            or repeat_program == "no"
            or repeat_program == "NO"
            or repeat_program == "nO"
        ):
            repeat = False
        else:
            run_count += 1

    print("This program was run", run_count, "time(s)", sep=' ')


main()
# Citations:
# Textbook: "thinkpython2"
# Site: https://www.w3schools.com/python/
# Site: https://www.allrecipes.com
# Site: https://docs.python.org/3/tutorial/
