import sys

menu = ["술","삼겹살","베이징코야","참치회","성게알밥","장어곰탕"]

for food in menu:
    print(food, end=" ")

for i in sys.stdin:
    print(i, end="")
