""" 
********************************************************************** 
Description: Charting Module to create graphs with Pygal and matplolib
             save files in .svg and .png
             
Author: Victor Robles 

Project: Assigment 10
 
Revision: 08/23/2020
********************************************************************** 
"""

import pygal
import matplotlib.pyplot as plt

def dates_range_list(date_list):
	'''	Create a date list range and sort it from lowest to highest'''
	range_list = []
	#iterate throuhg the dates of each list to create a range list
	for dates in date_list:
		for date in dates:
			if date not in range_list:
				range_list.append(date)
	return range_list

def price_date_normalize(dates, prices, list_range):
	'''	Find a price number for each year, add zero to the price list 
		when no value exists'''
	prices_normalized = []
	#iterate through the date range and date & weigh list for each Stock
	for date, price in zip(dates, prices):
		temp_prices = []
		for check in list_range:
			if check not in date:
				temp_prices.insert(0,None)
			else:
				temp_prices.append(price.pop(0))
		prices_normalized.append(temp_prices)
	return prices_normalized

def get_charting_inputs(stock_dictionary):
	"""" Organize graphs inputs for graphing"""
	#iterate throu each object 
	for key, stock in stock_dictionary.items():
		items_len = len(stock_dictionary)
		last_item = items_len - 1
		#On first iteration, create lists for storing data values 
		if key == list(stock_dictionary)[0]:
			items_name_list = []
			items_date_list = []
			items_price_list = []
			list_range = []
		
		#names list of each object
		items_name_list.append(stock.symbol)
		
		#dates list for each object
		temp_dates = []
		for date in stock.date_priced:
			#print(date)
			temp_dates.append(date)
		items_date_list.append(temp_dates)

		temp_prices = []
		for price in stock.price_list:
			temp_prices.append(price)
		items_price_list.append(temp_prices)
	
		#On last iteration, find range list, normalize prices and create graph
		if key == list(stock_dictionary)[last_item]:
			list_range = dates_range_list(items_date_list)
			list_prices_normalized = price_date_normalize(items_date_list, 
										items_price_list, list_range)
			return list_range, items_name_list, list_prices_normalized

def get_line_chart(title, file_in, list_range, names, prices):
	'''	Graph a pygal Bar graph for each Stock list'''
	title_name = str(title)
	file_name = str(file_in) + '.svg'   
	line_chart = pygal.Line()
	line_chart.title = title
	line_chart.x_labels = map(str, list_range)
	for name, price in zip(names, prices):
		line_chart.add(name, price)
	line_chart.render_to_file(file_name)
	print(str(file_name) + ' created.....')	

def get_line_plot(title, x_label, y_label, file_in, list_range, names, prices):
	''' plot matplotlib.pyplot '''
	file_name = str(title) + '.png' 
	for name, price in zip(names, prices):
		plt.plot(list_range, price, label = name)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.legend()
	plt.savefig(file_name)
	print(str(file_name) + ' created.....')	
	plt.show()
