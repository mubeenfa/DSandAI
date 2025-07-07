# -------------- Excercise 3 Dictionary of List

prodDict = dict()
isLoop = True

while isLoop: # Loop starts here
    print("\n********** MENU *************") # Added \n for better spacing
    print("Press 1 to Add Product ")
    print("Press 2 to Show Product ")
    print("Press 3 to Remove Product ")
    print("Press 4 to Purchase Product ")
    print("Press 5 to Exit")

    try:
        inp1 = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue # Go back to the beginning of the loop

    if inp1 == 1:
        prodId = input("Product Id: ")
        if prodId in prodDict:
            print("Product ID already exists. Please choose a unique ID.")
            continue
        prodName = input("Product Name: ")
        try:
            prodPrice = float(input("Price: ")) # Convert to float
            prodStock = int(input("Quantity: ")) # Convert to int
        except ValueError:
            print("Invalid input for Price or Quantity. Please enter numbers.")
            continue
        prodCategory = input("Category: ")


        prodDict[prodId] = [prodName, prodPrice, prodCategory, prodStock] # Changed to List
        print("Product added successfully!")

    elif inp1 == 2:
        if not prodDict:
            print("No products to display.")
        else:
            print("\n--- Current Products ---")
            for p_id, p_details in prodDict.items():
                print(f"ID: {p_id}, Name: {p_details[0]}, Price: {p_details[1]}, Category: {p_details[2]}, Stock: {p_details[3]}")
            print("------------------------")


    elif inp1 == 3:
        prodId = input("Product Id to remove: ")
        if prodId in prodDict:
            del prodDict[prodId] # Using del is also common for removing dictionary items
            print(f"Product with ID '{prodId}' removed.")
        else:
            print("Invalid ID! Product not found.")

    elif inp1 == 4:
        prodId = input("Product Id to purchase: ")
        if prodId in prodDict:
            try:
                pieces = int(input("No# of Pieces: "))
            except ValueError:
                print("Invalid input for pieces. Please enter a number.")
                continue

            # prodDict[prodId][3] is now an integer if input correctly
            current_stock = prodDict[prodId][3]

            if pieces <= 0:
                print("Number of pieces to purchase must be greater than zero.")
            elif current_stock >= pieces: # Check if enough stock
                prodDict[prodId][3] -= pieces # Directly subtract from the integer
                print(f"Purchased {pieces} pieces of '{prodDict[prodId][0]}'. Remaining stock: {prodDict[prodId][3]}")
            else:
                print(f"Insufficient stock. Only {current_stock} available.")
        else:
            print("Invalid ID! Product not found.")

    elif inp1 == 5:
        isLoop = False
        print("Exiting program. Goodbye!")

    else:
        print("Invalid Choice! Please enter a number between 1 and 5.")