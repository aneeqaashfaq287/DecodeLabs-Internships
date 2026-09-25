items = [
    {
        "name": "Avengers",
        "category": "action",
        "language": "english"
    },
    {
        "name": "Inception",
        "category": "sci-fi",
        "language": "english"
    },
    {
        "name": "3 Idiots",
        "category": "comedy",
        "language": "hindi"
    },
    {
        "name": "Dangal",
        "category": "drama",
        "language": "hindi"
    },
    {
        "name": "Interstellar",
        "category": "sci-fi",
        "language": "english"
    },
    {
        "name": "PK",
        "category": "comedy",
        "language": "hindi"
    },
    {
        "name": "The Dark Knight",
        "category": "action",
        "language": "english"
    }
]


print("===== AI Recommendation System =====")

print("\nAvailable Categories:")
print("action")
print("sci-fi")
print("comedy")
print("drama")

print("\nAvailable Languages:")
print("english")
print("hindi")


category = input("\nEnter your favorite category: ").lower().strip()
language = input("Enter your preferred language: ").lower().strip()


recommendations = []


for item in items:

    score = 0

    if item["category"] == category:
        score = score + 1

    if item["language"] == language:
        score = score + 1

    if score > 0:
        recommendations.append((item["name"], score))


print("\n===== Recommended Items =====")


if len(recommendations) == 0:

    print("Sorry, no matching recommendations found.")

else:

    recommendations.sort(key=lambda x: x[1], reverse=True)

    for name, score in recommendations:

        if score == 2:
            print(name, "- Strong Match")

        else:
            print(name, "- Partial Match")