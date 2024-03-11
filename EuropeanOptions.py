import math
from scipy.stats import norm

class EuropeanCall:
    def __init__(self, asset_price, volatility, strike_price, time_to_expiration, risk_free_rate):
        self.asset_price = asset_price
        self.volatility = volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = 0
    def call_price(self, asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate):
        b = math.exp(-risk_free_rate*time_to_expiration)
        x1 = math.log(asset_price/(b*strike_price)) + .5*(asset_volatility*asset_volatility)*time_to_expiration
        x1 = x1/(asset_volatility*(time_to_expiration**.5))
        z1 = norm.cdf(x1)
        z1 = z1*asset_price
        x2 = math.log(asset_price/(b*strike_price)) - .5*(asset_volatility*asset_volatility)*time_to_expiration
        x2 = x2/(asset_volatility*(time_to_expiration**.5))
        z2 = norm.cdf(x2)
        z2 = b*strike_price*z2
        return z1 - z2

class EuropeanPut:
    def __init__(self, asset_price, volatility, strike_price, time_to_expiration, risk_free_rate):
        self.asset_price = asset_price
        self.volatility = volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = 0
    def put_price(self, asset_price, asset_volatility, strike_price,time_to_expiration, risk_free_rate):
        b = math.exp(-risk_free_rate*time_to_expiration)
        x1 = math.log((b*strike_price)/asset_price) + .5*(asset_volatility*asset_volatility)*time_to_expiration
        x1 = x1/(asset_volatility*(time_to_expiration**.5))
        z1 = norm.cdf(x1)
        z1 = b*strike_price*z1
        x2 = math.log((b*strike_price)/asset_price) - .5*(asset_volatility*asset_volatility)*time_to_expiration
        x2 = x2/(asset_volatility*(time_to_expiration**.5))
        z2 = norm.cdf(x2)
        z2 = asset_price*z2
        return z1 - z2
    

ec = EuropeanCall(100, .3, 100, 1, .01)

# Call the call_price method with the appropriate parameters to calculate the option price
option_price = ec.call_price(ec.asset_price, ec.volatility, ec.strike_price, ec.time_to_expiration, ec.risk_free_rate)

print(option_price)