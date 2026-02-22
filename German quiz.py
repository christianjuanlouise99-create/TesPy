import random

words = {
    "tisch": "table",
    "stuhl": "chair",
    "fenster": "window",
    "tür": "door",
    "buch": "book",
    "lampe": "lamp",
    "computer": "computer",
    "telefon": "telephone",
    "uhr": "clock",
    "bett": "bed"
}

articles = {
    "tisch": "der",
    "stuhl": "der",
    "fenster": "das",
    "tür": "die",
    "buch": "das",
    "lampe": "die",
    "computer": "der",
    "telefon": "das",
    "uhr": "die",
    "bett": "das"
}

score = 0
score_article = 0
total = len(words)
total_articles = len(articles)

for i in random.sample(list(words), len(words)):
    answer = input(f"what is the translations of {i} in english : ").lower().strip()
    correct_answer = words[i].lower()

    article_answers = input(f"what is the article from {i} in german (der/ die / das) : ").lower().strip()
    correct_article = articles[i].lower()

    if answer == correct_answer:
        score += 1

    if article_answers == correct_article:
        score_article += 1

    if correct_article == article_answers and answer == correct_answer:
        print("Correct! Both translation and article are right.")
    elif answer == correct_answer:
        print("""you've got the translation right!
but the article is wrong!""")
    elif article_answers == correct_article:
        print("""you've got the article right!
but the translation is wrong""")
    else:
        print("you've got both wrong!")


print(f"your total score for translations is {score} out of {total}")
print(f"your total score for articles is {score_article} out of {total_articles}")