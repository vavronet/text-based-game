import time
import config
import random

def run():
    second_boss_intro()

    game_over = False
    status = False
    tries = config.tries['second_boss']
    player_health = config.health['player']
    boss_health = config.health['second_boss']

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
                player_points = random.choice(config.points['player'])
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
                    boss_points = random.choice(config.points['second_boss'])
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
            print("You defeated the second boss!\n")

    return status


def second_boss_intro():
    print("You coninue your journey along the Hairline... Watch out! Fadora blocks the way!\n")
    time.sleep(1.5)
    print('You have {} health points.'.format(config.health['player']))
    print('This boss has {} health points!'.format(config.health['second_boss']))
    print('You have {} tries to defeat her!\n'.format(config.tries['second_boss']))
