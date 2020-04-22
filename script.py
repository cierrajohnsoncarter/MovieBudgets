
# List of movies and their budgets
movies = [
    ('Avengers: Endgame', 400000000),
    ('Pirates of the Caribbean: On Stranger Tides', 379000000),
    ('Avengers: Age of Ultron', 365000000),
    ('Star Wars: Ep. VII: The Force Awakens', 306000000),
    ('Avengers: Infinity War', 300000000)
]

# Allows user to input how many movies they want to add to the list
add_new_movie = int(input('How many movies do you want to add? '))

# Takes the name and budget of the movie the user entered and add the movie to the list
for _ in range(add_new_movie):
    name = input('Enter movie name: ')
    budget = input('Enter movie budget: ')
    new_movie = (name, int(budget))
    movies.append(new_movie)

# List representing over budget movies and counter to keep track of the total budget of all the movies in the list
over_budget_movies = []
total_budget = 0

# Adds together the budget of each movie
for movie in movies:
    total_budget += movie[1]

# Calculates the average cost of all movies in the list
average_budget = int(total_budget / len(movies))

# If the movie budget is over the average budget, how much the movies are over budget will be calculated and added to the over budget list
for movie in movies:
    if movie[1] > average_budget:
        over_budget_movies.append(movie)
        over_average_cost = movie[1] - average_budget
        print(
            f"{movie[0]} was ${movie[1]:,}: ${over_average_cost:,} over average.")
        print()

# Prints how many movies were over the average budget
print(
    f"There were {len(over_budget_movies)} movies with budgets that were over average.")
