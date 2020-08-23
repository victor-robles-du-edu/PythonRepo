""" 
********************************************************************** 
Description: Stocks Class for stocks prices movements

Author: Victor Robles 

Project: Assigment 10
 
Revision: 08/09/2020
********************************************************************** 
"""

class Stocks():
	def __init__(self, symbol, date_price, open_price, high_price, low_price, close_price, volume):
		"""Initialize the stock."""
		self.symbol = symbol.upper()
		self.date_price = date_price
		self.open_price = open_price
		self.high_price = high_price
		self.low_price = low_price
		self.close_price = close_price
		self.volume = volume
		self.price_list = []
		self.date_priced = []
	
	def add_price(self, price, date, shares):
		"""Add information to the class"""
		value = price * shares
		self.price_list.append(value)
		self.date_priced.append(date)
