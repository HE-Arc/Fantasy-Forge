import random

def get_proficiency(level):
    return int((level - 1) / 4) + 2

def generate_ability_score():
    rolls = sorted([random.randint(1, 6) for _ in range(4)])
    return sum(rolls[1:])

def generate_ability_scores():
    return sorted([generate_ability_score() for _ in range(6)], reverse=True)

def get_modifier(ability):
    return (ability - 10) // 2

scores = generate_ability_scores()
for score in scores:
    print(f'{score} ({get_modifier(score)})')