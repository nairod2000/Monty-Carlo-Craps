import numpy as np
from typing import List, Tuple
np.random.seed(5)

def roll_dice(sides: int, rolls: int) -> np.ndarray:
    ''' Simulate N number dice rolls

    Parameters
    ----------
    sides
        how many sides the dice has
    rolls
        how many dice rolls to put into array

    Return
    ----------
    numpy array of int values representing dice rolls
    '''
    return np.random.randint(sides, size=rolls) + 1

def check_condition(condition: int, array: np.ndarray, idx_list: List[int]) -> int:
    ''' Check array for values that match condition 
    
    idx_list is updated with the matched indecies

    Parameters
    ----------
    condition
        what to look for in the array
    array
        The array to look for condition in 
    idx_list
        List of indcies that have been accounted for 

    Return
    ----------
        The number of times the condition found in array
    '''
    cur_idx = np.where(array == condition)

    # cur_idx[0] is list of indecies that match condition
    idx_list.extend(cur_idx[0])
    return len(cur_idx[0])

def craps(games: int) -> Tuple[int, int]:
    '''
    Parameters
    ----------
    games
        number of games to play

    Return
    ----------
        tuple with number of wins and losses respectivly
    '''
    DICE_RANGE = 6
    total_wins = 0
    total_losses = 0
    wins = 0
    losses = 0
    finished_games = list()

    # roll dice
    result = roll_dice(DICE_RANGE, games) + roll_dice(DICE_RANGE, games)

    ## Inital game winning conditions
    wins += check_condition(7, result, finished_games)
    wins += check_condition(11, result, finished_games)

    ## Inital game losing conditions
    losses += check_condition(2, result, finished_games)
    losses += check_condition(3, result, finished_games)
    losses += check_condition(12, result, finished_games)

    ## Update game
    games -= wins
    games -= losses
    total_wins += wins
    total_losses += losses
    
    # set wins and losses to -1
    result[finished_games] = -1 
    # get rid of all indecies where result == -1
    result = result[result != -1]

    ## rest of game
    while games > 0:
        # reset variables
        wins = 0
        losses = 0
        finished_games.clear()

        # roll dice
        roll = roll_dice(DICE_RANGE, games) + roll_dice(DICE_RANGE, games)

        losses += check_condition(7, roll, finished_games)
        wins += check_condition(True, np.equal(result, roll), finished_games)

        # Update game
        total_wins += wins
        total_losses += losses
        games -= wins
        games -= losses

        # set wins and losses to -1
        result[finished_games] = -1
        # get rid of all indecies where result == -1
        result = result[result != -1]
    
    return (total_wins, total_losses)


if __name__ == "__main__":
    from time import time

    start_time = time()
    wins, losses = craps(1000000)

    print(wins / 1000000)
    print(f'time: {time() - start_time}')
