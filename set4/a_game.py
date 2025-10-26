import random

def last_coin_bot(coins):
    return 1 if coins % 4 == 1 else (coins % 4 or 1)

def play_last_coin():
    coins = 15
    print(f"Starting with {coins} coins")
    
    while coins > 0:
        bot_move = last_coin_bot(coins)
        coins -= bot_move
        print(f"Bot takes {bot_move}, {coins} left")
        
        if coins == 0:
            print("Bot wins!")
            break
        
        human = int(input(f"Take 1-3 coins ({coins} left): "))
        human = min(max(human, 1), min(3, coins))
        coins -= human
        print(f"You took {human}, {coins} left")
        
        if coins == 0:
            print("You win!")
            break

play_last_coin()
