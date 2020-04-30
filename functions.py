import random

def do_fight(params):    
    tries = params['tries']
    boss_health = params['boss_health']
    boss_attack_points = params['boss_attack_points']
    boss = params['boss']
    player_health = params['player_health']
    player_attack_points = params['player_attack_points']
    
    game_over = False
    status = False

    while game_over == False:
        if tries == 0:
            game_over = True
            status = False
        else:
            if player_health <= 0:
                game_over = True
                status = False
            else:
                # get random hit points for player
                player_points = random.choice(player_attack_points)
                # calculate boss health
                boss_health = boss_health - player_points
                # decrease # of tries
                tries = tries - 1
                # print attack details
                player_attack_details = "PLAYER attack: \n--------------\nPoints: {}, Boss health: {}, Tries left: {}"
                print(player_attack_details.format(player_points, boss_health, tries))
                input("Press any key to continue...\n")
                
                if boss_health <= 0:
                    game_over = True
                    status = True
                else:
                    # get random hit points for boss
                    boss_points = random.choice(boss_attack_points)
                    # calculate player health
                    player_health = player_health - boss_points
                    # print boss attack details
                    boss_attack_details = "\nBOSS attack: \n------------\nPoints: {}, Player health: {}"
                    print(boss_attack_details.format(boss_points, player_health))
                    input("Press any key to continue...\n")
    else:
        if status == False:
            print("You Lost!\n")
        else:
            print("You defeated the {} boss!\n".format(boss))

    return status