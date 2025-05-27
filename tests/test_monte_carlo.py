from pricers.monte_carlo import MonteCarloOptionPricer

def test_call_pricing_convergence():
    pricer = MonteCarloOptionPricer(S0=100, K=100, T=1, r=0.05, sigma=0.2, num_paths=500000)
    price = pricer.price_european_call()
    assert 9.5 < price < 11.0  # Ballpark range for validation

def test_put_pricing_convergence():
    pricer = MonteCarloOptionPricer(S0=100, K=100, T=1, r=0.05, sigma=0.2, num_paths=500000)
    price = pricer.price_european_put()
    assert 4.5 < price < 6.5
