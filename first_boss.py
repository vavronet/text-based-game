import time
import config
import random
import functions

def run():
    first_boss_intro()

    params = {
        'tries': config.tries['first_boss'],
        'boss_health': config.health['first_boss'],
        'boss_attack_points': config.points['first_boss'],
        'boss': 'first',
        'player_health': config.health['player'],
        'player_attack_points': config.points['player']
    }

    return functions.do_fight(params)

def first_boss_intro():
    print("You've entered the Hair Zone... Watch out! Beanie blocks the way!\n")
    time.sleep(1.5)
    print('You have {} health points.'.format(config.health['player']))
    print('This boss has {} health points!'.format(config.health['first_boss']))
    print('You have {} tries to defeat him!\n'.format(config.tries['first_boss']))