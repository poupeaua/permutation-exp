"""
    Program to make permutation simulation and estimate probabilities.
    (such as proba to obtain k fixed points in a permutation from a length n
    object)
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt


class PermSimulation:


    def __init__(self, n, nb_sim):
        """
            Initialize a PermSimulation object
        """
        self.n = n
        self.nb_sim = nb_sim
        # you cannot choose the original array values
        self.original = np.linspace(0, n-1, n, dtype=int)



    def countFixedPts(self, perm_sim_matrix):
        """
            Arguments:
                original (array) : [0, 1, 2, ..., n-1]
                perm_sim_matrix (array) : matrix of shape (n, nb_sim)

            Returns:
                count_fixed_pts_array (array) : it is a (n+1) length array.
                    The value at index i counts the number of permutations that
                    have i fixed points. Different possibilities 0 -> n.
        """
        count_fixed_pts_array = np.zeros(shape=(self.n+1), dtype=int)
        for permutation in perm_sim_matrix:
            # iterate over the simulations
            nb_fixed_pts = 0
            for index, value in enumerate(permutation):
                # iterate over value to check fixed point
                if index == value:
                    nb_fixed_pts += 1
            count_fixed_pts_array[nb_fixed_pts] += 1
        return count_fixed_pts_array



    def runSimulation(self):
        """
            Function that runs the simulation.

            Returns:
                perm_sim_matrix (array) : shape (nb_sim, n)
        """
        perm_sim_matrix = np.zeros(shape=(self.nb_sim, self.n), dtype=int)
        for cur_sim in range(0, self.nb_sim):
            # iteration on simulations
            unused_indexes = [i for i in range(0, self.n)]
            for value in range(0, self.n):
                # make one random permutation
                cur_idx = np.random.choice(unused_indexes)
                unused_indexes.remove(cur_idx)
                perm_sim_matrix[cur_sim, cur_idx] = value
        return perm_sim_matrix



def main():
    """
        Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=20)
    parser.add_argument("-k", type=int, default=1)
    parser.add_argument("-nb_sim", type=int, default=10000)
    args = parser.parse_args()

    # run simulation
    psim = PermSimulation(n=args.n, nb_sim=args.nb_sim)
    perm_sim_matrix = psim.runSimulation()
    result = psim.countFixedPts(perm_sim_matrix=perm_sim_matrix)
    print(result)
    # print(result/args.nb_sim)



if __name__ == "__main__":
    main()
