
##Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")




combined_name = name1 + name2

combined_name_lower = combined_name.lower()

T= combined_name_lower.count("t")
R= combined_name_lower.count("r")
U= combined_name_lower.count("u")
E= combined_name_lower.count("e")

L= combined_name_lower.count("l")
O= combined_name_lower.count("o")
V= combined_name_lower.count("v")
E= combined_name_lower.count("e")

Score1 = T+R+U+E
Score2 = L+O+V+E

Final_Score = str(Score1) + str(Score2)


Final_Score = int(Final_Score)


if Final_Score <10 or Final_Score>90:
    print(f"Your score is {Final_Score}, you go together like coke and mentos.")
elif Final_Score >=40 and Final_Score<=50:
    print(f"Your score is {Final_Score}, you are alright together.")
else:
    print(f"Your score is {Final_Score}.")
