def main():
    # Create a list with a fixed size for storing food items
    foods = [""] * 5  # Placeholder list with a size of 5

    size = len(foods)
    
    for i in range(size):
        temp = input(f"Enter a food you like or 'q' to quit #{i + 1}: ")
        
        # Check for the quit condition
        if temp.lower() == "q":
            break
        else:
            foods[i] = temp  # Assign the input to the list

    print("You like the following food:")

    # Iterate and print only non-empty elements of the list
    for food in foods:
        if food:  # Skip empty strings
            print(food)

if __name__ == "__main__":
    main()
