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



    def expectedProbasFixedPts(self):
        """
            Compute the theorical probability to obtain each possible number
            of fixed points.

            Returns:
                expected_proba_fixed_pts_array (array) : length (n+1).
                    Contains the theorical probability to obtain k fixed points
                    (k:0->n).
        """
        expected_proba = np.zeros(shape=(self.n+1), dtype=float)
        for k in range(self.n, -1, -1):
            expected_proba[:k] += (-1)**((self.n-k)%2)/np.math.factorial(self.n-k)
            if (self.n-k) > 1:
                expected_proba[(self.n-k):] /= (self.n-k)
        return expected_proba



    def countFixedPts(self, perm_sim_matrix):
        """
            Arguments:
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
                proba_fixed_pts_array (array) : length (n+1). Contains the
                    simulated probability to obtain k fixed points (k:0->n)
                expected_proba (array) : length (n+1).
                    Contains the theorical probability to obtain k fixed points
                    (k:0->n).
        """
        # compute the permutation simulations matrix
        perm_sim_matrix = np.zeros(shape=(self.nb_sim, self.n), dtype=int)
        for cur_sim in range(0, self.nb_sim):
            # iteration on simulations
            perm_sim_matrix[cur_sim, :] = np.random.permutation(self.original)

        # calculate the empirical probabilities of fixed points
        count_fixed_pts_array = self.countFixedPts(perm_sim_matrix)
        proba_fixed_pts_array = count_fixed_pts_array/self.nb_sim

        # compute the theorical probabilities
        # expected_proba = self.expectedProbasFixedPts()
        expected_proba = []
        return perm_sim_matrix, proba_fixed_pts_array, expected_proba


def simnfixed(n, nb_sim):
    _, experiment, theory = PermSimulation(n=n, nb_sim=nb_sim).runSimulation()
    print(experiment, theory)
    plt.plot(np.linspace(0, n+1, n+1), experiment, label="Experiment")
    plt.legend()
    plt.title("Probability of having k fixed points as a function of k - n="+str(n)+" fixed")
    plt.xlabel("k")
    plt.ylabel("p_k,n")
    plt.show()


def simkfixed(n_max, k, nb_sim, step):
    stock = list()
    i = 0
    for cur_n in range(k, n_max, step):
        _, experiment, theory = PermSimulation(n=cur_n, nb_sim=nb_sim).runSimulation()
        stock.append(experiment[k])
        i += 1
    plt.plot(np.linspace(k, k+i*step, i), stock, label="Experiment")
    plt.hlines(np.exp(-1)/np.math.factorial(k), xmin=k, xmax=k+i*step, label="e^(-1)/k!")
    plt.legend()
    plt.title("Probability of having k fixed points as a function of n - k="+str(k)+" fixed")
    plt.xlabel("n")
    plt.ylabel("p_k,n")
    plt.show()




def main():
    """
        Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=10)
    parser.add_argument("-k", type=int, default=4)
    parser.add_argument("-nb_sim", type=int, default=1000)
    args = parser.parse_args()

    # --------------- run simulations (n fixed) --------------------
    # simnfixed(n=10, nb_sim=1000)


    # ---------------- run simulation (k fixed) -----------------------
    simkfixed(n_max=500000, k=2, nb_sim=50, step=5000)


if __name__ == "__main__":
    main()
