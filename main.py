import game_intro
import first_boss
import second_boss
import final_boss
import game_over
import game_won

# Run game intro
game_intro.run()

#Run first boss module
first_boss_result = first_boss.run()

if first_boss_result == True:
    #Run second boss module
    second_boss_result = second_boss.run()

    if second_boss_result == True:
        final_boss_result = final_boss.run()

        if final_boss_result == True:
            game_won.run()
        else:
            game_over.run()
    else:
        game_over.run()
else:
    game_over.run()
