""" 
********************************************************************** 
Description: Investment file containing the Stock, Bond and Investor
             Classes. Calculate gain, yearly return percent
             
Author: Victor Robles 

Project: Assigment 10
 
Revision: 08/23/2020
********************************************************************** 
"""
from datetime import datetime

#current date declaration
current_date =  datetime.now().strftime("%m/%d/%Y")

class Stock():
	
	"""information about the stock symbol, number of shares, purchase price
	, current price, purchase date, current date and purchase ID"""

	def __init__(self, purchase_ID, symbol, number_shares, purchase_price, 
				current_price, purchase_date, present_date=current_date):
		"""Initialize stock attributes"""
		self.purchase_ID = purchase_ID
		self.symbol = symbol
		self.number_shares = number_shares
		self.purchase_price = purchase_price
		self.current_price = current_price
		self.purchase_date = purchase_date
		self.current_date = present_date

	def gain(self):
		"""
			Function to calculate the positive or negative gain of a stock
			input should be a stock dictionary
			search for current price, purchase price and number of shares
		"""
		gain = ((self.current_price - self.purchase_price )	*	
						self.number_shares )
		#return gain
		return gain
		
	def percent_gain(self):
		"""
			Function to calculate the percent gain of a stock
			input should be a stock dictionary
			search for current price and purchase price
		"""
		percent_gain = ((self.current_price - self.purchase_price ) /
					  self.purchase_price )*100
		#return the percent gain back
		return percent_gain

	def yearly_percent_gain(self):
		"""
			Function to calculate the percent yearli +/- gain of a stock
			input should be a stock dictionary
			percent gain float, and current date datetime
			search for purchase price
		"""
		percent_gain = self.percent_gain()
		purchase_date = datetime.strptime(self.purchase_date, "%m/%d/%Y")
		current_date =  datetime.strptime(self.current_date, "%m/%d/%Y")
		date_duration = ((current_date - purchase_date).days)/365
		yearly_percent_gain = (percent_gain/date_duration)
		#return yearly percent gain
		return yearly_percent_gain

class Bond(Stock):
	"""information about the inherited class of Stock attributes plus 
		coupon number and yiled percent"""

	def __init__(self, purchase_ID, symbol, number_shares, purchase_price, 
				current_price, purchase_date, coupon, yield_percent):
		"""Initialize Bonds attributes from the parent class Stock"""
		super().__init__(purchase_ID, symbol, number_shares, purchase_price,
							current_price, purchase_date, current_date)
		#unique attributes to the Bonds class: coupon and yield
		self.coupon = coupon
		self.yield_percent = yield_percent

class Investor():
	"""information about the inherited class of Stock attributes plus 
		coupon number and yiled percent"""

	def __init__(self, investor_ID, name, address, phone):
		"""Initialization investor class"""
		self.investor_ID = investor_ID
		self.address = address
		self.name = name
		self.phone = phone
