def shopping_categories():
    categories = []
    while True:
        category = input("Enter a category: ")
        categories.append(category)
        another_category = input("Do you have another category to shop? (yes/no): ")
        if another_category.lower() != 'yes':
            break
    return categories

def spend(categories):
    spent_money = []
    for category in categories:
        while True:
            try:
                amount = float(input(f"How much did you spend on {category}? $").strip())
                break  # Break out of the loop if the input is successfully converted to float
            except ValueError:
                print("Invalid input. Please enter a valid numerical value.")

        spent_money.append(amount)
    return spent_money

def spent_categories(categories, spend):
    max_spent_index = spend.index(max(spend))
    
    print("\nLet's see how much you spent on each category:")
    for i in range(len(categories)):
        print(f"How much did you spend on {categories[i]}? ${spend[i]:.2f}")

    most_spent_category = categories[max_spent_index]
    most_spent_amount = spend[max_spent_index]
    print(f"\nYou spent ${most_spent_amount:.2f} on {most_spent_category} the most this year!")
