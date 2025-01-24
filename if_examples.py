from random import choice

# Predefined lists of drinks and mixers
drinks = ["whiskey", "rum", "vodka"]
mixers = ["Fanta", "Fanta Limón", "Dr Pepper"]

print("I am the virtual bartender, welcome!")
name = input("How should I call you? ")

try:
    # Fixed typo in "imput" to "input"
    age = input("How old are you? ")
    age = int(age)  # Convert to integer

    legal = None  # Initialize legal drinking status
    country = input("Where are you from? ")

    # Determine legality based on age and country
    if age < 14:
        legal = False
    elif age < 16:
        if country == "Austria":
            legal = True
        else:
            legal = False
    elif age < 18:
        if country in ["Austria", "Luxemburg"]:
            legal = True
        else:
            legal = False
    elif age < 21:
        if country in ["USA", "UAE"]:
            legal = False
        else:
            legal = True
    else:  # Age is 21 or older
        legal = True

    # Serve a drink if legal
    if legal:
        print(f"{name}, here is your drink: {choice(drinks)} with {choice(mixers)}!")
    else:
        print(f"Sorry {name}, I cannot serve you alcohol.")

except ValueError:
    print("I don't have time for your games! Please provide a valid age.")