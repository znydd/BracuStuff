import random 


class Mortal_Kombat:
    def __init__(self, starting_player: int):
        self.starting_player = starting_player  
        self.round_winners = []  
    

    def alpha_beta(self, depth, max_player, alpha, beta):
        if depth == 5: 
            return random.choice([-1, 1])

        if max_player == True:
            state_alpha = float('-inf')
            for _ in range(2):
                util_val = self.alpha_beta(depth+1, False, alpha, beta)
                state_alpha = max(state_alpha, util_val)
                alpha = max(alpha, util_val)
                if alpha >= beta:
                    break  # Beta cut-off
            return state_alpha
        else:  # min_player
            state_beta = float('inf')
            for _ in range(2):
                util_val = self.alpha_beta(depth+1, True, alpha, beta)
                state_beta = min(state_beta, util_val)
                beta = min(beta, util_val)
                if alpha >= beta:
                    break  # Alpha cut-off
            return state_beta

    def simulate(self):
        if self.starting_player == 0:   # 0 for Scorpion, 1 for Sub-Zero
            turn = [False, True, False]
        else:
            turn = [True, False, True]

        for i in range(3):
            result = self.alpha_beta(0, turn[i], float('-inf'), float('inf'))
            self.round_winners.append("Scorpion" if result == -1 else "Sub-Zero")
            
        return self.round_winners


def mortalkombat():
    starting_player = int(input("Choose starting player for 1st round (0 for Scorpion, 1 for Sub-Zero): "))
    game = Mortal_Kombat(starting_player)
    round_winners = game.simulate()

    game_winner = 'Scorpion' if round_winners.count('Scorpion') > round_winners.count('Sub-Zero') else "Sub-Zero"

    result =f"""Game Winner: {game_winner}
    Total Rounds Played: 3
    Winner of Round 1: {round_winners[0]}
    Winner of Round 2: {round_winners[1]}
    Winner of Round 3: {round_winners[2]}""" 
    print(result)


# ** Part-2 **

ouput_lst_norm = [3, 6, 2, 3, 7, 1, 2, 0]

def alpha_beta_norm( depth, max_player, alpha, beta):
    if depth == 3: 
        return ouput_lst_norm.pop(0)
    
    if max_player == True:
        state_alpha = float('-inf')
        for _ in range(2):
            util_val = alpha_beta_norm(depth+1, False, alpha, beta)
            state_alpha = max(state_alpha, util_val)
            alpha = max(alpha, util_val)
            if alpha >= beta:
                break  # Beta cut-off
        return state_alpha
    else:  # min_player
        state_beta = float('inf')
        for _ in range(2):
            util_val = alpha_beta_norm(depth+1, True, alpha, beta)
            state_beta = min(state_beta, util_val)
            beta = min(beta, util_val)
            if alpha >= beta:
                break  # Alpha cut-off
        return state_beta

ouput_lst_dark = [3, 6, 2, 3, 7, 1, 2, 0]

def alpha_beta_moded(depth, max_player, alpha, beta):
    if depth == 3: 
        return ouput_lst_dark.pop(0)
    if max_player == True:
        state_alpha = float('-inf')
        for _ in range(2):
            util_val = alpha_beta_moded(depth+1, False, alpha, beta)
            state_alpha = max(state_alpha, util_val)
            alpha = max(alpha, util_val)
            if alpha >= beta:
                break  # Beta cut-off
        return state_alpha
    else:  # min_player
        state_beta = float('-inf')
        for _ in range(2):
            util_val = alpha_beta_moded(depth+1, True, alpha, beta)
            state_beta = max(state_beta, util_val)
            beta = max(beta, util_val)
            if alpha >= beta:
                break  # Alpha cut-off
        return state_beta

def pacman():
    dark_magic = int(input("Insert dark magic cost: "))
    no_dark_magic_out = alpha_beta_norm(0, True, float('-inf'), float('inf'))
    dark_magic_out = alpha_beta_moded(0, True, float('-inf'), float('inf')) - dark_magic

    if no_dark_magic_out > dark_magic_out:
        print(f"The minmax value is {no_dark_magic_out}. Pacman does not use dark magic")
    else:
        print(f"The new minmax value is {dark_magic_out}. Pacman goes right and uses dark magic")


game_choice = int(input("(0)Mortal-Kombat or (1)Pacman: "))
game_choice = 0 if game_choice > 1 else game_choice
if game_choice == 0:
    mortalkombat()
else:
    pacman()
