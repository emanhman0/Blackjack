import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(list_of_cards):
    score = 0
    for num in list_of_cards:
        score += num
        if list_of_cards[0] + list_of_cards[1] == 21:
            return 0
        elif cards[0] in list_of_cards and score > 21:
            cards.remove(11)
            cards.insert(0, 1)
            score -= 10
    else:
        return score

def compare(user_score1, cpu_score2):
    scores = {"User": user_score1, "Computer": cpu_score2}
    highest_score = max(scores, key=scores.get)
    if user_score1 == cpu_score2:
        return print("It's a draw")
    elif cpu_score2 == 0:
        return print("Opponent scored a blackjack. You lose.")
    elif user_score1 == 0:
        return print("Blackjack! You win.")
    elif user_score1 > 21:
        return print("You went over. You lose")
    elif cpu_score2 > 21:
        return print("Opponent went over. You win")
    else:
        return print(f"{highest_score} wins. ")

new_game = True
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == 'y':
    new_game = True
else:
    print("Exiting game")
    new_game = False

while new_game:
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    play_blackjack = True
    while play_blackjack:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 21 or user_score == 0:
            print("You win")
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            play_blackjack = False
        elif user_score > 21:
                print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                print("You went over. You lose")
                play_blackjack = False
        else:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == "y":
                user_cards.append(deal_card())
                play_blackjack = True
            else:
                draw_card = "n"
                computer_play = True
                while computer_play:
                    cpu_score = calculate_score(computer_cards)
                    if cpu_score < 17:
                        computer_cards.append(deal_card())
                        computer_play = True
                    else:
                        computer_play = False
                        play_blackjack = False
                        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                        compare(user_score, cpu_score)
    restart_game = input("Would you like to play again? 'y' or 'n'")
    if restart_game == "y":
        print("\n" * 100)
        new_game = True
    else:
        print("Thanks for playing!"):
            new_game = False


