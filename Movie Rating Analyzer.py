movies = (
    ("Interstellar", 9.0, 2014),
    ("Inception", 8.8, 2010),
    ("Avatar", 7.8, 2009),
    ("Oppenheimer", 8.6, 2023)
)

print("🎬 Movie List\n")

highest = 0
best_movie = ""

for movie in movies:
    name, rating, year = movie
    
    print("Movie:", name)
    print("Rating:", rating)
    print("Year:", year)
    print("--------------")
    
    if rating > highest:
        highest = rating
        best_movie = name

print("\n⭐ Best Movie:", best_movie)
print("⭐ Rating:", highest)
