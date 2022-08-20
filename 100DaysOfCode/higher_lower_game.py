import art
from game_data import data
import random

print(art.logo)


def higher_lower_game():
    def random_pick():
        random_number = random.randint(0, len(data))
        random_dic = data[random_number]
        contestant = random_dic["name"] + ", a " + random_dic["description"] + ", from " + random_dic["country"]
        followers = random_dic["follower_count"]
        return contestant, followers

    keep_playing = True
    score = 0
    contestant_one, ones_followers = random_pick()
    while keep_playing:
        print("Compare A: " + contestant_one)
        print(art.vs)
        contestant_two, twos_followers = random_pick()
        print("Against B: " + contestant_two)
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if ones_followers >= twos_followers and answer.lower() == "a":
            score += 1
            contestant_one, ones_followers = contestant_two, twos_followers
            print(f"Correct Answer! You current score is {score}!")
        elif ones_followers < twos_followers and answer.lower() == "b":
            score += 1
            contestant_one, ones_followers = contestant_two, twos_followers
            print(f"Correct Answer! You current score is {score}!")
        else:
            print(f"Wrong Answer! You total score is {score}!")
            keep_playing = False


another_try = True
while another_try:
    higher_lower_game()
    keep_playing = input("Do you want to try again? Yes/No: ")
    if keep_playing.lower() == "no":
        another_try = False
