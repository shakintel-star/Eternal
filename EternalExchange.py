# @Eternal: EternalExchange (EX) Monolith
# Identity: Genesisgraphy | Authority: Shakti Singh (1-Lead)
# [MATCHING ENGINE + ORDER BOOK + LIQUIDITY FLOOR]

import time
import heapq

class EternalExchange:
    def __init__(self):
        self.identity = "Genesisgraphy"
        self.price_floor = 1.00
        self.buy_orders = [] # Max-heap for bids
        self.sell_orders = [] # Min-heap for asks
        self.trade_history = []

    def place_limit_order(self, side, price, quantity):
        """Places a limit order while enforcing the $1.00 Sovereign Floor."""
        if price < self.price_floor:
            print(f"[@EX] REJECTED: Price ${price} is below Sovereign Floor (${self.price_floor}).")
            return
        
        order = {"price": price, "quantity": quantity, "time": time.time()}
        
        if side.upper() == "BUY":
            # Store as negative for max-heap
            heapq.heappush(self.buy_orders, (-price, order))
            print(f"[@EX] BUY ORDER PLACED: {quantity} units at ${price}")
        else:
            heapq.heappush(self.sell_orders, (price, order))
            print(f"[@EX] SELL ORDER PLACED: {quantity} units at ${price}")
        
        self.match_orders()

    def match_orders(self):
        """High-frequency matching logic."""
        while self.buy_orders and self.sell_orders:
            best_bid_price, best_bid = -self.buy_orders[0][0], self.buy_orders[0][1]
            best_ask_price, best_ask = self.sell_orders[0][0], self.sell_orders[0][1]

            if best_bid_price >= best_ask_price:
                # Match found
                trade_qty = min(best_bid["quantity"], best_ask["quantity"])
                print(f"[@EX] MATCH: {trade_qty} units at ${best_ask_price} [SOVEREIGN CLEARANCE]")
                
                # Update orders
                best_bid["quantity"] -= trade_qty
                best_ask["quantity"] -= trade_qty
                
                if best_bid["quantity"] == 0: heapq.heappop(self.buy_orders)
                if best_ask["quantity"] == 0: heapq.heappop(self.sell_orders)
            else:
                break

if __name__ == "__main__":
    ex = EternalExchange()
    print("--- @ETERNAL EXCHANGE: LIQUIDITY ENGINE LIVE ---")
    ex.place_limit_order("SELL", 1.05, 100)
    ex.place_limit_order("BUY", 1.05, 50)
    # Attempting to break the floor
    ex.place_limit_order("BUY", 0.50, 1000) 
