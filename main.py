def main():
    foods = []  # Initialize an empty list for storing food items

    while True:
        # Prompt the user for input
        temp = input(f"Enter a food you like or 'q' to quit #{len(foods) + 1}: ")

        # Check for the quit condition
        if temp.lower() == "q":
            break
        else:
            foods.append(temp)  # Dynamically add the input to the list

    print("You like the following food:")

    # Print all elements in the list
    for food in foods:
        print(food)

if __name__ == "__main__":
    main()
