# Import necessary libraries
import sys

# Define a dictionary of recipes with ingredients and instructions
recipes = {
    "Pasta Carbonara": {
        "ingredients": ["pasta", "eggs", "parmesan cheese", "bacon", "black pepper"],
        "instructions": "Cook pasta. In a separate pan, cook bacon until crispy. Beat eggs and mix with parmesan cheese. Combine pasta, bacon, and egg mixture. Season with black pepper."
    },
    "Tomato Soup": {
        "ingredients": ["tomatoes", "onion", "garlic", "vegetable broth", "basil"],
        "instructions": "Sauté onion and garlic. Add tomatoes and vegetable broth. Simmer until tomatoes are soft. Blend until smooth. Garnish with basil."
    },
    "Omelette": {
        "ingredients": ["eggs", "milk", "cheese", "bell pepper", "onion"],
        "instructions": "Beat eggs with milk. Pour into a heated pan. Add cheese, bell pepper, and onion. Cook until set."
    }
}

def find_meals(available_ingredients):
    possible_meals =    for meal, details in recipes.items():
        if all(item in available_ingredients for item in details["ingredients"]):
            possible_meals.append(meal)
    return possible_meals

def get_recipe(meal_name):
    if meal_name in recipes:
        return recipes[meal_name]["instructions"]
    else:
        return "Recipe not found."

def main():
    # Get user input for available ingredients
    available_ingredients = input("Enter the ingredients you have, separated by commas: ").lower().split(", ")
    
    # Find possible meals
    meals = find_meals(available_ingredients)
    
    if meals:
        print("You can cook the following meals:")
        for i, meal in enumerate(meals, 1):
            print(f"{i}. {meal}")
        
        # Get user choice for a specific meal
        choice = int(input("Enter the number of the meal you want the recipe for: "))
        if 1 <= choice <= len(meals):
            selected_meal = meals[choice - 1]
            print(f"Recipe for {selected_meal}:")
            print(get_recipe(selected_meal))
        else:
            print("Invalid choice.")
    else:
        print("No meals can be prepared with the available ingredients.")

if __name__ == "__main__":
    main()
