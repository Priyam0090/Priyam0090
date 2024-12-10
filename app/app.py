def main():
    # Get user input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate the year when the user will turn 100
    current_year = 2024  # You can use the current year or dynamically get it
    year_when_100 = current_year + (100 - age)

    # Output the result
    print(f"Hello, {name}! You will turn 100 years old in the year {year_when_100}.")

if __name__ == "__main__":
    main()
