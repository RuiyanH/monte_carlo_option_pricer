import numpy as np

class MonteCarloOptionPricer:
    def __init__(self, S0, K, T, r, sigma, num_paths=100000, seed=42):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.num_paths = num_paths
        self.seed = seed

    def simulate_price_paths(self):
        np.random.seed(self.seed)
        Z = np.random.standard_normal(self.num_paths)
        ST = self.S0 * np.exp((self.r - 0.5 * self.sigma**2) * self.T +
                              self.sigma * np.sqrt(self.T) * Z)
        return ST

    def price_european_call(self):
        ST = self.simulate_price_paths()
        payoffs = np.maximum(ST - self.K, 0)
        return np.exp(-self.r * self.T) * np.mean(payoffs)

    def price_european_put(self):
        ST = self.simulate_price_paths()
        payoffs = np.maximum(self.K - ST, 0)
        return np.exp(-self.r * self.T) * np.mean(payoffs)
