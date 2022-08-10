from random import randint

def check_win(lst: list[int]) -> bool:
    """
    Returns whether the position consist of a winning pos

    Precondition: not a winning hand before the last pos
    """
    all_winning_pos = [{i, i + 1, i + 2} for i in range(0, 8, 3)] + \
                      [{i, i + 3, i + 6} for i in range(0, 3)] + \
                      [{0, 4, 8}, {2, 4, 6}]

    last_pos = lst[-1]
    for i in range(1, len(lst) - 1):
        for j in range(i):
            if {lst[j], lst[i], last_pos} in all_winning_pos:
                return True

    return False


def minimax(A,B,move=True,depth=0):
    """
    Returns the move that returns the best utility based on minimax
    and the state of the game
    """
    # end of game tie
    if len(A) + len(B) == 9 and not check_win(A) and not check_win(B):
        return 0, None

    elif len(A) ==0 or len(B)==0:
        random_pos = randint(0,8)
        while random_pos in A + B:
            random_pos = randint(0, 8)
        return 0, random_pos

    # player's turn to make a move
    if move:
        # check if opp won in previous
        if check_win(B):
            return -10 + depth, None

        max_utility = -1 * float('inf')
        max_pos = None
        for i in [i for i in range(9) if i not in A + B]:
            u1,_ = minimax(A + [i], B, False, depth+1)
            if u1 > max_utility:
                max_utility = u1
                max_pos = i
        return max_utility, max_pos

    # move that bot thinks oppo would make
    else:
        # check if player won
        if check_win(A):
            return 10 - depth, None

        min_utility = float('inf')
        for i in [i for i in range(9) if i not in A + B]:
            u2, _ = minimax(A, B + [i], True, depth+1)
            min_utility = min(u2, min_utility)
        return min_utility, None

