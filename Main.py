"""
Meal Planner with Recipes
Program is intended to plan out meals for the day and perform
arithmetic on differing potential values within the recipes
Created 202101 for use within COP 1500.  Finished 2021.
"""
__author__ = "Kristopher Marlow"

import time  # import time for slowing down the program's progression


def insert_separator(times):
    """
    Creates a separator line as needed throughout the program. The 'times' parameter is passed to change the
    length of the separator as needed. Function also slows down the progression of the program
    :param times: Indicates the size of the desired separator in characters.
    """
    print("---" * times)
    time.sleep(1)


def number_choice(text):
    """
    Method by which user inputs are tested as valid integers.  Function will display text argument,
    and return the input as a number
    :param text: Allows each input to have its own text explanations.
    :return: Brings the numeric choice from the function to the requisite variable assignment.
    """
    while True:
        try:
            choice = int(input(text))
        except ValueError:
            print("Not a valid numeric selection, please try again entering numbers (1,2,3,...)")
            continue
        else:
            return choice


def main():
    """
    This is the body of the program.  Within the function, other functions are called as needed.
    Program is intended to plan out meals for the day and perform
    arithmetic on differing potential values within the recipes
    """
    repeat = True
    run_count = 1
    while repeat:
        for number in range(5, 0, -1):
            print(number)
            time.sleep(1)
        if run_count > 1:
            print("Let's Continue!")
        else:
            print("Let's Begin!")
        insert_separator(10)
        print("Hello!  I am here to assist you with your meal choices today.",
              "Up first is selecting which meal options you would like for today",
              end=" \n")
        insert_separator(10)
        print("Breakfast Options:", "1. Eggs, Bacon, and Toast", "2. French Toast", sep="\n")
        breakfast_choice = number_choice(
            "Which option would you like for breakfast? (Choose by Number): ")  # Storing breakfast choice for later
        insert_separator(10)
        print("Lunch Options:", "1. Grilled Cheese and Tomato Soup", "2. Grilled Chicken Salad", sep="\n")
        lunch_choice = number_choice(
            "Which option would you like for lunch? (Choose by Number): ")  # Storing lunch choice for later
        insert_separator(10)
        print("Dinner Options:", "1. Grilled Chicken with Rice and Vegetables", "2. Beef Stew", sep="\n")
        dinner_choice = number_choice(
            "Which option would you like for dinner? (Choose by Number): ")  # Storing dinner choice for later
        insert_separator(10)
        print("Your choices for meals are: ")
        insert_separator(10)
        breakfast_calories = 0  # set to have a baseline for the variable.
        lunch_calories = 0  # set to have a baseline for the variable.
        dinner_calories = 0  # set to have a baseline for the variable.
        print("Breakfast:")
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
            dinner_calories = 335 + 118 + 206 + 20
            print("Calories: " + str(dinner_calories) + " per serving")  # concat txt with the str of a numeric variable
        elif dinner_choice == 2:
            print("Beef Stew")
            dinner_calories = 614 + 118 + 28 + 70
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
            breakfast_serving_size = number_choice(
                "How many people will be partaking in breakfast?: ")  # used to see how to adjust per serving size
        else:
            ''
        if lunch_choice >= 1:
            lunch_serving_size = number_choice(
                "How many people will be partaking in lunch?: ")  # used to see how to adjust per serving size
        else:
            ''
        if dinner_choice >= 1:
            dinner_serving_size = number_choice(
                "How many people will be partaking in dinner?: ")  # used to see how to adjust per serving size
        else:
            ''
        daily_calories = (
                (breakfast_calories * breakfast_serving_size) +
                (lunch_calories * lunch_serving_size) +
                (dinner_calories * dinner_serving_size)
        )
        print("Total calories for today's meals: ", daily_calories, sep='')  # Sum of each meal's calories
        if (breakfast_choice > 0 and lunch_choice > 0 and dinner_choice > 0
                and breakfast_serving_size > 0 and lunch_serving_size > 0 and dinner_serving_size > 0):
            insert_separator(10)
            print("You have chosen three full meals, that is a fairly balanced meal plan.  Good job!")
        else:  # if (breakfast_choice == 0 or lunch_choice == 0 or dinner_choice == 0
            # or breakfast_serving_size == 0 or lunch_serving_size == 0 or dinner_serving_size == 0):
            insert_separator(10)
            print("You have chosen to skip meals, or made meals that no one is eating.")
            print("You may want consider going through the meal planner again.")
        insert_separator(10)
        insert_separator(10)
        print("Recipes")  # This section should list out the selected recipes
        insert_separator(10)
        print("Breakfast:")
        if breakfast_choice == 1:
            import egg_bacon_toast  # set the import of the recipes
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
        print("Dinner:")
        if dinner_choice == 1:
            import chicken_rice_vegetables  # set the import of the recipes
            print(str(int(chicken_rice_vegetables.dinner_ingredient_1_num) * dinner_serving_size)
                  + " " + chicken_rice_vegetables.dinner_ingredient_1)
            print(str(int(chicken_rice_vegetables.dinner_ingredient_2_num) * dinner_serving_size)
                  + " " + chicken_rice_vegetables.dinner_ingredient_2)
            print(str(int(chicken_rice_vegetables.dinner_ingredient_3_num) * dinner_serving_size)
                  + " " + chicken_rice_vegetables.dinner_ingredient_3)
            print(str(int(chicken_rice_vegetables.dinner_ingredient_4_num) * dinner_serving_size)
                  + " " + chicken_rice_vegetables.dinner_ingredient_4)
            insert_separator(5)
            print(chicken_rice_vegetables.dinner_recipe)
        elif dinner_choice == 2:
            import beef_stew  # set the import of the recipes
            print(str(int(beef_stew.dinner_ingredient_1_num) * dinner_serving_size)
                  + " " + beef_stew.dinner_ingredient_1)
            print(str(int(beef_stew.dinner_ingredient_2_num) * dinner_serving_size)
                  + " " + beef_stew.dinner_ingredient_2)
            print(str(int(beef_stew.dinner_ingredient_3_num) * dinner_serving_size)
                  + " " + beef_stew.dinner_ingredient_3)
            print(str(int(beef_stew.dinner_ingredient_4_num) * dinner_serving_size)
                  + " " + beef_stew.dinner_ingredient_4)
            insert_separator(5)
            print(beef_stew.dinner_recipe)
        else:
            print("No valid dinner selected.")
        insert_separator(10)
        insert_separator(10)
        repeat_program = input("Would you like to rerun the program? Y/N ")
        if (
                repeat_program.upper() == "N"
                or repeat_program.upper() == "NO"
                or repeat_program.upper() == "N0"
        ):
            repeat = False
        else:
            run_count += 1

    print("This program was run ", run_count, " time(s)", sep='')


if __name__ == "__main__":
    main()

# Citations:
# Textbook: "thinkpython2"
# Site: https://www.w3schools.com/python/
# Site: https://www.allrecipes.com
# Site: https://docs.python.org/3/tutorial/
# Site: https://sites.google.com/site/profvanselow/
