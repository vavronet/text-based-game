import time
import config
import random
import functions

def run():
    final_boss_intro()

    params = {
        'tries': config.tries['final_boss'],
        'boss_health': config.health['final_boss'],
        'boss_attack_points': config.points['final_boss'],
        'boss': 'final',
        'player_health': config.health['player'],
        'player_attack_points': config.points['player']
    }

    return functions.do_fight(params)

def final_boss_intro():
    print("You've entered the final stage... Watch out! The Evil Wizard blocks the way!\n")
    time.sleep(1.5)
    print('You have {} health points.'.format(config.health['player']))
    print('This boss has {} health points!'.format(config.health['final_boss']))
    print('You have {} tries to defeat him!\n'.format(config.tries['final_boss']))