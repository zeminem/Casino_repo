import random

# Глобална променлива която присъства във всяка функция и следи настоящия баланс в играта.
money = 0

# Тесте за Pick a Card
deck = [
    'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace',
    2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace', 2, 3, 4,
    5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace', 2, 3, 4, 5, 6, 7,
    8, 9, 10, 'Jack', 'Queen', 'King']
# Обхват за играта на рулетка
roulette_numbers = range(37)
smaller_deck = [2, 2, 3]


# Главната функция, която стартира казиното и изисква въвеждане на началаен баланс. Изисква мин баланс от $20.00.
def cashier():
    global money

    try:
        money = float(input(""" 
                
               █░░ ▄▀█ █▀   ▀█▀ █▀█ ▄▀█ █▀ ▀█▀ █ █▄▀ ▄▀█ █▀  
               █▄▄ █▀█ ▄█   ░█░ █▀▄ █▀█ ▄█ ░█░ █ █░█ █▀█ ▄█ 
                                                      
                    🅆🄴🄻🄲🄾🄼🄴 🅃🄾 🄾🅄🅁 🄲🄰🅂🄸🄽🄾❕
          
          
        Read the instructions before every game to understand the rules.
                Chose the amount that you want to start with: 
                                    """))
    except ValueError:
        print("Choose an amount!")
        cashier()
    # print("\n        Your credit is now - $%.2f." % money)

    if money < 20:
        print("You need at least $20.00 to enter the casino.")
        cashier()
    else:
        game_menu()


def flip_a_coin():
    print("""\n       <𝗙𝗹𝗶𝗽 𝗮 𝗰𝗼𝗶𝗻>     
Choose a side, before the coin is tossed. Heads or Tails will get you the winnings against our casino.

    You and the casino bet equal amounts. The winner gets everything            
          """)
    input("Press Enter↵ to continue...")

    global money
    # Изисква въвеждането на залог, преди всяка игра и проверява дали стойността е десетично число в противен случай рестартира функцията.
    try:
        bet = float(input("""\n
Your balance is $%.2f.
Chose the amount that you want to bet: """ % money))
    except ValueError:
        print("""\nＩｎｖａｌｉｄ ｉｎｐｕｔ！ 
                Ｃｈｏｏｓｅ ａｎ ａｍｏｕｎｔ．""")
        flip_a_coin()
    # Проверява дали наличността в баланса е достатъчна, за да бъде покрит залога. Ако не е вика функция за презареждане.
    # Проверява и дали се опитваме да заложим негативна сума и срестартира функцията, ако е така.
    if 0 < bet > money:
        reload_money()
    if bet <= 0:
        print("Ｙｏｕ ｃａｎ＇ｔ ｂｅｔ ａ ｎｅｇａｔｉｖｅ ａｍｏｕｎｔ．")
        flip_a_coin()

    heads = 1
    tails = 2
    call = [heads, tails]
    winnings = bet * 2
    flip = random.choice(call)
    # Иска въвеждане на залог в случая трябва да се избере 1 или 2 в противен случай функцията се рестартира.
    try:
        choice = int(input("Chose a bet - [1] Heads / [2] Tails: "))
    except ValueError:
        print("Ｃｈｏｏｓｅ ａ ｖａｌｉｄ ｉｎｐｕｔ [1] or [２]！")
        flip_a_coin()
    if choice != heads and choice != tails:
        print("Ｃｈｏｏｓｅ ａ ｖａｌｉｄ ｉｎｐｕｔ [1] or [２]！")
        flip_a_coin()
    # Следната част проверява дали избора съответства на резултата и определя дали играча печели или губи.
    if flip == heads:
        print(
            "\nThe coin landed on Heads!\n"
        )
        if choice == heads:
            print("You won $%.2f! with Heads!" % bet)
            money += winnings - bet
        else:
            print("You lost $%.2f! with Tails!" % bet)
            money = money - bet
    if flip == tails:
        print(
            "\nThe coin landed on Tails!\n"
        )
        if choice == tails:
            print("You won $%.2f! with Tails!" % bet)
            money += winnings - bet
        else:
            print("You lost $%.2f! with Heads!" % bet)
            money = money - bet

    print("Your active is now $%.2f." % money)  # Принтира обновената стойност на баланса.
    anykey = input("\nPress Enter↵ to return to Game Menu...")
    game_menu()
    # Връща обновена стойност на баланса, след играта и я актуализира в глбалната функция.
    return money


def cho_han():
    print("""\n       <𝗖𝗵𝗼 𝗛𝗮𝗻>   
The game uses two standard six-sided dice, which are shaken in a bamboo cup or bowl by a dealer. 
Players place their wagers on whether the sum total of numbers showing on the two dice will be "Chō" (even) or "Han" (odd). 

    You and the casino bet equal amounts. The winner gets everything            
              """)
    input("Press Enter↵ to continue...")

    global money

    try:
        bet = float(input("""\n
Your balance is $%.2f.
Chose the amount that you want to bet: """ % money))
    except ValueError:
        print("""\nＩｎｖａｌｉｄ ｉｎｐｕｔ！ 
                    Ｃｈｏｏｓｅ ａｎ ａｍｏｕｎｔ．""")
        cho_han()

    if 0 < bet > money:
        reload_money()
    if bet <= 0:
        print("Ｙｏｕ ｃａｎ＇ｔ ｂｅｔ ａ ｎｅｇａｔｉｖｅ ａｍｏｕｎｔ．")
        cho_han()

    winnings = bet * 2
    even = 2
    odd = 1
    roll = random.randint(1, 12)

    try:
        choice = int(input("Chose a bet - [1] Odd / [2] Even: "))
    except ValueError:
        print("Ｃｈｏｏｓｅ ａ ｖａｌｉｄ ｉｎｐｕｔ [1] or [２]！")
        cho_han()

    if choice != even and choice != odd:
        print("Ｃｈｏｏｓｅ ａ ｖａｌｉｄ ｉｎｐｕｔ [1] or [２]！")
        cho_han()

    if roll % 2 != 0:
        result = odd
        print("\nDices roll equals " + str(roll))
        if choice == odd and result == odd:
            print(
                "You won $%.2f with Odd!"
                % winnings)
            money += winnings - bet
        else:
            choice != result
            print(
                "You lost $%.2f with Even."
                % (bet))
            money = money - bet
    elif roll % 2 == 0:
        result = even
        print("\nDices roll equals " + str(roll))
        if choice == even and result == even:
            print(
                "You won $%.2f with Even!"
                % winnings)
            money += winnings - bet
        else:
            choice != result
            print(
                "You lost $%.2f with Odd."
                % (bet))
            money = money - bet
    print("Your active is now $%.2f." % money)
    anykey = input("\nPress Enter↵ to return to Game Menu...")
    game_menu()
    return money


def pick_a_card():
    print("""\n       <𝗣𝗶𝗰𝗸 𝗮 𝗰𝗮𝗿𝗱>   
You and the dealer draw cards from a standard deck. The stronger card wins.

        You and the casino bet equal amounts. The winner gets everything            
                  """)
    input("Press Enter↵ to continue...")

    global money

    try:
        bet = float(input("""\n
Your balance is $%.2f.
Chose the amount that you want to bet: """ % money))
    except ValueError:
        print("""\nＩｎｖａｌｉｄ ｉｎｐｕｔ！ 
                    Ｃｈｏｏｓｅ ａｎ ａｍｏｕｎｔ．""")
        pick_a_card()

    if 0 < bet > money:
        reload_money()
    if bet <= 0:
        print("Ｙｏｕ ｃａｎ＇ｔ ｂｅｔ ａ ｎｅｇａｔｉｖｅ ａｍｏｕｎｔ．")
        pick_a_card()

    print("\nBoth players are drawing cards ...")
    winnings = bet * 2
    player1_draw = random.choice(deck)
    print("\nYou drew a " + str(player1_draw) + ".")
    # Принтира индекса на картата в тестето
    # print(str(deck.index(player1_draw)))
    player2_draw = random.choice(deck)
    print("The dealer drew a " + str(player2_draw) + "." + "\n")
    # Принтира индекса на картата в тестето
    # print(str(deck.index(player2_draw)) + "\n")

    if player1_draw == player2_draw:
        print("Its a draw! \nBoth players keep their bets.")
    elif deck.index(player1_draw) > deck.index(player2_draw):
        print(
            "You won $%.2f with %s!"
            % (winnings, player1_draw))
        print(
            "The casino  lost $%.2f with %s."
            % (bet, player2_draw))
        money += winnings - bet
    elif deck.index(player1_draw) < deck.index(player2_draw):
        print(
            "The casino won $%.2f with %s!"
            % (winnings, player2_draw))
        print(
            "You lost $%.2f with %s."
            % (bet, player1_draw))
        money = money - bet
    print("Your active is now $%.2f." % money)
    anykey = input("\nPress Enter↵ to return to Game Menu...")
    game_menu()
    return money


def turn_the_roulette():
    print("""\n       <𝗥𝗼𝘂𝗹𝗲𝘁𝘁𝗲>   
The most simple roulette game - one ball and thirty six sectors of chance. 
Choose a sector and you can multiply your bet by thirty six.

            Winnings are multiplied by 36.           
                      """)
    input("Press Enter↵ to continue...")

    global money

    try:
        bet = float(input("""\n
Your balance is $%.2f.
Chose the amount that you want to bet: """ % money))
    except ValueError:
        print("""\nＩｎｖａｌｉｄ ｉｎｐｕｔ！ 
                    Ｃｈｏｏｓｅ ａｎ ａｍｏｕｎｔ．""")
        turn_the_roulette()

    if 0 < bet > money:
        reload_money()
    if bet <= 0:
        print("You can't bet a negative amount.")
        turn_the_roulette()

    try:
        number = int(input("Chose the number that you want to bet on [1-36]: "))
        while not (number in roulette_numbers):
            print("Choose a number in the range of 1-36\n")
            turn_the_roulette()
    except ValueError:
        print("Choose a number in the range of 1-36\n")
        turn_the_roulette()

    winnings = bet * 36
    result = random.choice(roulette_numbers)
    print("\nThe roulette turns on ...> " + str(result) + " <...!")

    if number == result:
        print("\nYou won $%.2f with %s!"
              % (winnings, result))
        money += winnings - bet
    if not (number == result):
        print("\nThe casino wins.\n"
              "You loose $%.2f."
              % bet)
        money = money - bet
    print("Your active is now $%.2f." % money)

    anykey = input("\nPress Enter↵ to return to Game Menu...")
    game_menu()
    return money


# Главното меню в казиното със списъка от налични игри.
def game_menu():
    print("""
            𝗖𝗵𝗼𝗼𝘀𝗲 𝗮 𝗴𝗮𝗺𝗲 𝘁𝗼 𝗽𝗹𝗮𝘆
          Your balance is - $%.2f. 
                
    1. <𝗙𝗹𝗶𝗽 𝗮 𝗰𝗼𝗶𝗻>
        Instant coin toss. Heads or Тails?
        
    2. <𝗖𝗵𝗼 𝗛𝗮𝗻>
        Chinese dice game of luck.
        
    3. <𝗣𝗶𝗰𝗸 𝗮 𝗰𝗮𝗿𝗱>
        You and the casino pick cards. The stronger one wins!
        
    4. <𝗥𝗼𝘂𝗹𝗲𝘁𝘁𝗲>
        A simple game of roulette.
        
    5. <𝗟𝗲𝗮𝘃𝗲 𝘁𝗵𝗲 𝗖𝗮𝘀𝗶𝗻𝗼>
        If your're tired of loosing all your monthly savings, just choose this option.
         """ % money)
    # Изисква въвеждане на опция от главното меню и проверява за валидност.
    # Ако опцията не е налична или потребителят въведе невалиден символ рестартира функцията.
    try:
        selection = int(input("\nSelect your choice: "))
    except ValueError:
        print("Invalid choice. Choose an option from the game menu 1-5")
        game_menu()
    if selection == 1:
        flip_a_coin()
    elif selection == 2:
        cho_han()
    elif selection == 3:
        pick_a_card()
    elif selection == 4:
        turn_the_roulette()
    elif selection == 5:
        print("Goodbye looser! It was nice collecting that easy money from you;)")
        exit()
    else:
        print("Invalid choice. Choose an option from the game menu 1-5")
        game_menu()


# Функция за презареждане на баланса.
# потребителят е препратен към нея, когато балансът му е равен на нула или е по-нисък от въведения залог.
def reload_money():
    global money

    print("""
    Your balance is $%.2f, which is not enough to continue
    
            Choose an option
        1. Continue with my current balance. You will be returned to Main Menu.        
        2. Reload balance        
        3. Leave the casino
             """ % money)
    # Изисква въвеждане на опция от главното меню и проверява за валидност.
    # Ако опцията не е налична или потребителят въведе невалиден символ рестартира функцията.
    try:
        selection = int(input("\nSelect your choice: "))
    except ValueError:
        print("Invalid choice. Choose a valid option 1-2!")
        reload_money()

    if selection == 1:
        game_menu()
    # Ако потребителят избере опцията, да презареди баланса си, новата стойност се добавя към настоящия му баланс.
    if selection == 2:
        try:
            fresh_money = int(input(""" 
        Chose the amount that you want to reload in your balance: 
                          """))
        except ValueError:
            print("Choose an amount!")
            reload_money()
        money = money + fresh_money
        game_menu()
    if selection == 3:
        print("Goodbye looser! It was nice collecting that easy money from you;)")
        exit()

    else:
        print("Invalid choice. Choose a valid option 1-3")
        reload_money()
    print("Your balance is now $%.2f." % money)


cashier()

