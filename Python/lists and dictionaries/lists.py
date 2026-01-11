# List is a datatype in python that can store any values of different datatype unlike arrays
# list can hold int, str, bool, float in one place.

l1 = [1, 2, 3, 4, 5] # example of single type valued list
l2 = [1, 23, True, "Ripon", 69.69, False] # example of multiple valued list


# we can iterate through list using python and print the values of it.
movies = ["Avengers", "Tenet", "openheimer", "Shawshank Redemption"]

# this is one and easy way to iterate through list
for movie in movies:
    print(movie)

# this is another way of iterate and showing values of a list using index 
for i in range(len(movies)):
    print(movies[i])

# we can also add the index number using "i" in the output
for i in range(len(movies)):
    print(f"{i + 1}. {movies[i]}")