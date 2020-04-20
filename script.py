
movies = [
    ('Avengers: Endgame', 400000000),
    ('Pirates of the Caribbean: On Stranger Tides', 379000000),
    ('Avengers: Age of Ultron', 365000000),
    ('Star Wars: Ep. VII: The Force Awakens', 306000000),
    ('Avengers: Infinity War', 300000000)
]
over_budget_movies = []
total_budget = 0

for movie in movies:
    total_budget += movie[1]

average_budget = int(total_budget / len(movies))

for movie in movies:
    if movie[1] > average_budget:
        over_budget_movies.append(movie)
        over_average_cost = movie[1] - average_budget
        print(f"{movie[0]} was ${movie[1]} over average.")

print(
    f"There were {len(over_budget_movies)} movies with budgets that were over average.")
