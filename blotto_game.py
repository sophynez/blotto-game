"""
to-do :
1- fct to get input N ; nbr of soldiers for both players ✅
2- fct to generate the strategies based of the input value ✅
3- fct to calculate the gain of each strategy and create a matrix of the game ✅

4- fct for :
    4.1- nash equilibrium ✅
    4.2- pareto ✅
    4.3- security level
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
    mapped = zip([i for i in range(nbr)], strats)
    return mapped


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


def nash_equilibrium(profits, mapped_strats, itr):
    best_gains = []
    best_strats = []
    for column in range(itr):  # iterate over all the existing strategies, in this case get the columns each time
        gains = profits[:, column]  # got the strategies
        best = max(gains, key=itemgetter(0))
        best_gains.append(best)  # keep the best gains in a list
        nash_indexes = np.unique(np.where(gains == best)[0])  # get the index of the strat corr to the best gain
        for ind in nash_indexes:
            best_strats.append(mapped_strats[ind])  # most important thing : keep the best strategies in a list
    best_strats = list(set(best_strats))
    return best_strats


def security_level(profits, itr, mapp):
    # starting with the first player
    min_gains_list = []
    for i in range(itr):
        min_gain = min(profits[i], key=itemgetter(0))
        min_gains_list.append(min_gain)
    secure_strategy = max(min_gains_list, key=itemgetter(0))
    secure_strategy = mapp[min_gains_list.index(secure_strategy)]
    return secure_strategy


# testing purposes
soldiers = get_nbr_soldiers()
strategies = list(get_strategies(soldiers))
profits_matrix = (get_profits(strategies))
strategies_dict = dict(create_map(strategies, len(strategies)))
nash_equilibrium = nash_equilibrium(np.array(profits_matrix), strategies_dict, len(strategies))
security_strategy = security_level(profits_matrix, len(strategies), strategies_dict)

print(nash_equilibrium)
print(security_strategy)