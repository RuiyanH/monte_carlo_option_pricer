from pricers.monte_carlo import MonteCarloOptionPricer

if __name__ == "__main__":
    pricer = MonteCarloOptionPricer(S0=100, K=105, T=1, r=0.05, sigma=0.2)
    call_price = pricer.price_european_call()
    put_price = pricer.price_european_put()

    print(f"Monte Carlo Estimated Call Price: ${call_price:.4f}")
    print(f"Monte Carlo Estimated Put Price:  ${put_price:.4f}")
