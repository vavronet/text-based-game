import time
import config
import random
import functions

def run():
    second_boss_intro()

    params = {
        'tries': config.tries['second_boss'],
        'boss_health': config.health['second_boss'],
        'boss_attack_points': config.points['second_boss'],
        'boss': 'second',
        'player_health': config.health['player'],
        'player_attack_points': config.points['player']
    }

    return functions.do_fight(params)

def second_boss_intro():
    print("You coninue your journey along the Hairline... Watch out! Fadora blocks the way!\n")
    time.sleep(1.5)
    print('You have {} health points.'.format(config.health['player']))
    print('This boss has {} health points!'.format(config.health['second_boss']))
    print('You have {} tries to defeat her!\n'.format(config.tries['second_boss']))
