# 10 . Movie Collection - Dictionary
# 📌 You are maintaining a movie collection where each movie has a rating (out of 10). Write a
# program to add movies, update ratings, and display all movies with their ratings.

movies = {}  
while True:
    print("1. Add Movie, 2. Display Movies, 3. Exit")
    choice = int(input("Enter your choice  "))

    if choice == 1:
        movie = input("Enter movie name: ").strip()
        rating = int(input("Enter rating (out of 10): "))
        movies[movie] = rating
        print("Add movie ", movie, "updated with rating ", rating)

    elif choice == 2:
        if not movies:
            print("no movies in the collection.")
        else:
            print("movie Collection:")
            for movie, rating in movies.items():
                print(f"{movie}: {rating}/10")

    elif choice == 3:
        print("exiting")
        break
