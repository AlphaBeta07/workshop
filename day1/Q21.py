# 21. Create a Movie Class
# 📌 Create a class Movie with attributes title, genre, and rating. Add a method to display
# movie details.

class Movie:
    def __init__(self, title, genre , rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def details(self):
        print("title of movie is ", title)
        print("gener is ", genre)
        print("the ratings are ", rating)

title = input("enter the title of movie ")
genre = input("enter the genre of movie ")
rating = int(input("enter ratings "))

movie = Movie(title, genre , rating)
print ("the movie deatils are ")
movie.details()