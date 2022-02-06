movie_name = "The Martian"
author_name = "Andy Weir"
movie_rating = 4.5

""" String concatenation"""

# plus operator
print(movie_name + " is a novel written by " + author_name + ". It has a " + str(movie_rating) + " star rating on Amazon.")

# F-string.
print(f"{movie_name} is a novel written by {author_name}. It has a {movie_rating} star rating on Amazon.")

# Format-string.
print("{} is a novel written by {}. It has a {} star rating on Amazon.".format(movie_name, author_name, movie_rating))