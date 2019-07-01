shopping ='y'
pie_purchases =[]
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
print("welcome to the house of pies! Here are our pies:")
while shopping == "y":

    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")
    pie_choice = input("What would you like?")
    pie_purchases.append(pie_choice)

    print("Great we will have that "+ pie_list[int(pie_choice)-1]+" right out.")
    shopping = input("would you like more?")
    print("You have purchased"+ str(len(pie_purchases))+".")