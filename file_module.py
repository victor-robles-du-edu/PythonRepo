""" 
********************************************************************** 
Description: Read file, chek output file, read Json files
			 
Author: Victor Robles 

Project: file_module
 
Revision: 07/26/2020
********************************************************************** 
"""
import json

def get_read_data(filename):
	"""read all data from the file it checks if the file cannot be open"""
	try:
		with open(filename) as file_object:
			lines = file_object.readlines()
			return lines
	#if file is not open displayed a custom message
	except FileNotFoundError as e:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
		return None

def get_report_data(filename):
	"""checks if file exits and if the data can be append or write"""
	try:
		with open(filename) as file_object:
			lines = file_object.readlines()
			if len(lines)>0:
				return 'a'
			else:
				return 'w'
	except FileNotFoundError as e:
		return 'w'

def get_json_data(filename):
	''' Get Stock data from a json file '''
	try:
		with open(filename) as json_file:
			data_set = json.load(json_file)
		return data_set
	except FileNotFoundError as e:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
		return None
