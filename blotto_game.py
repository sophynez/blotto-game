"""
to-do :
1- fct to get input N ; nbr of soldiers for both players ✅
2- fct to generate the strategies based of the input value ✅
3- fct to calculate the gain of each strategy and create a matrix of the game ✅

4- fct for :
    4.1- dominance ❌ --pas de dominance dans ce jeu
    4.2- nash equilibrium ✅
    4.3- pareto
    4.4- security level
"""
import numpy as np
from operator import itemgetter

# profits of each field
F1 = 4
F2 = 2
F3 = 6
total = F1 + F2 + F3


def get_nbr_soldiers():
    n = int(input())
    return n


def get_strategies(n):
    for i in range(0, n + 1):
        sum_left = n - i
        for j in range(0, sum_left + 1):
            yield i, j, sum_left - j


def create_map(strats, nbr):
    map = zip([i for i in range(nbr)], strats)
    return map


def get_profits(strats):
    profit_lst = []
    for j1 in strats:
        lst = []
        for j2 in strats:
            profit1 = profit2 = profit3 = 0
            # field 1
            if j1[0] > j2[0]:
                profit1 += F1
            elif j1[0] == j2[0]:
                profit1 = F1 / 2
            # field 2
            if j1[1] > j2[1]:
                profit2 += F2
            elif j1[1] == j2[1]:
                profit2 = F2 / 2
            # field 3
            if j1[2] > j2[2]:
                profit3 += F3
            elif j1[2] == j2[2]:
                profit3 = F3 / 2
            profit = profit1 + profit2 + profit3
            lst.append((profit, total - profit))
        profit_lst.append(lst)

    return profit_lst


def best_shots_and_strategies(profits, player, mapped_strats, itr):
    best_gains = []
    best_strats = []
    secure_strats = []
    if player == 1:  # treating the 1st player :: working with columns
        for column in range(itr):  # iterate over all the existing strategies, in this case get the columns each time
            gains = profits[:, column]  # got the strategies
            best = max(gains, key=itemgetter(0))
            best_gains.append(best)  # keep the best gains in a list
            nash_indexes = np.unique(np.where(gains == best)[0])  # get the index of the strat corr to the best gain
            for ind in nash_indexes:
                best_strats.append(mapped_strats[ind])  # most important thing : keep the best strategies in a list

            # this part is for the security level
            min_gain = min(gains, key=itemgetter(0))
            secure_strats.append((min_gain, ()))
        print(secure_strats)
        secure_strategies = max(secure_strats, key=itemgetter(0))
        print(secure_strategies)
    if player == 2:
        for line in range(itr):
            best = max(profits[line], key=itemgetter(1))
            best_gains.append(best)
            list_of_indexes = np.unique(np.where(profits[line] == best)[0])  # get the index of the strat corr to the best gain
            print(list_of_indexes)
            for ind in list_of_indexes:
                print(mapped_strats[ind])
                best_strats.append(mapped_strats[ind])  # most important thing : keep the best strategies in a list
    best_strats = list(set(best_strats))
    return best_strats, secure_strats


def security_level(secure_strats, mapped):
    secure_strategies = max(secure_strats, key=itemgetter(0))

    pass


def pareto():
    pass


soldiers = get_nbr_soldiers()
strategies = list(get_strategies(soldiers))
profits_matrix = (get_profits(strategies))
strategies_dict = dict(create_map(strategies, len(strategies)))
nash_equilibrium = best_shots_and_strategies(np.array(profits_matrix), 1, strategies_dict, len(strategies))

# FOR TESTING PURPOSES ONLY
for i in range(10):
    print(profits_matrix[i])
print("Strategies : \n", strategies)


