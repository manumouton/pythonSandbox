import movie
import website

my_movie = movie.Movie("My movie", "this is my movie", "http://blabla.png", "https://www.youtube.com/watch?v=qvsgGtivCgs")

print(my_movie.storyline)

my_movie.show_trailer()

movies = [my_movie]

website.open_movies_page(movies)