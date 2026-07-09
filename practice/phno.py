import numpy as np


movie_list = np.array(["Stanger Things", "Witcher" , "Money Heist", "Breaking Bad"])

print("Favourite Movies : ")

for movie in movie_list:
    print(movie)

while True: 

    print("Welcome to Movie List!!!!!")

    print("1. To View the Movie list")
    print("2. Edit a movie")
    print("3. Add a movie")
    print("4. Delete a movie")
    print("5. Exit")
    

    choice = int(input("Your choice : "))

    if choice == 1:
        for movie in movie_list:
            print(movie)

    elif choice == 2:
        cho = input("The value you want to edit : ")
        ind = int(input("The index where you want to edit to :"))
        movie_list.insert(ind, cho)

    elif choice == 3:
        cho = input("The value you want to insert : ")
        movie_list.append(cho)

    elif choice == 4 :
        cho = input("The value you want to delete : ")
        movie_list.remove(cho)

    elif choice == 5 :
        print("Thank You for using Movie List.... Exiting...")
        break
    
    else :
        print("Invalid input!!!!! Try again......")








