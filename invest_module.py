""" 
********************************************************************** 
Description: Invesment Module for reading Stock and Bond data from CSV
             files, Json files and Write txt files.
             
Author: Victor Robles 

Project: Assigment 10
 
Revision: 08/23/2020
********************************************************************** 
"""
import json
from datetime import datetime
from investment import Stock, Bond, Investor
from Stocks import Stocks
from file_module import get_report_data, get_json_data
from Header import Header
from database_module import *

#current date declaration
current_date =  datetime.now().strftime("%m/%d/%Y")

def get_stock_data(data):
    """	Create Stock Class Objects"""
    stock_data_list = []
    headers = []

    for line in data:
        if data.index(line) == 0:
            headers.append(line.rstrip())
        else:
            line_whole = line.rstrip().replace('\n', '')
            line_split = line.split(',')
            stock_symbol = str(line_split[symbol_index])
            number_shares = int(line_split[shares_index])
            purchase_price = float(line_split[purchase_price_index])
            current_price = float(line_split[current_price_index])
            purchase_date = str(line_split[purchase_date_index].replace('\n', ''))
            stock_data = Stock(data.index(line),stock_symbol,number_shares,
                               purchase_price,current_price,purchase_date,
                               current_date)
            stock_data_list.append(stock_data)
        headers_split = headers[0].split(',')
        symbol_index = headers_split.index('SYMBOL')
        shares_index = headers_split.index('NO_SHARES')
        purchase_price_index = headers_split.index('PURCHASE_PRICE')
        current_price_index = headers_split.index('CURRENT_VALUE')
        purchase_date_index = headers_split.index('PURCHASE_DATE')
    
    return stock_data_list

def get_stock_report_text(stocks, owner, filename_write):
    """	Output Stock Report to text file specified"""
    gains_list = []
    stocks_list = []
    table = []
    
    #Declare uniform title for print report and determine the lenght
    title = f"Stock ownership for {owner.name}"
    address = f"{owner.address}"
    phone = f"{owner.phone}"
    #String heades for print report
    headers = ["Stock", "Share #", "Earnings/Loss", "Yearly Earning/Loss"]

    #Find width for table based on headers and title
    table.append(Header(headers, title))
    #Return values for print table
    j, k, m, n = table[0].header_width()
    
    with open(filename_write, 'w') as file_object:
        file_object.write("-"*(j+4))
        file_object.write(f"\n|{title:^{j+3}}|\n")
        file_object.write("-"*(j+4))
        file_object.write(f"\n|{address:^{j+3}}|\n")
        file_object.write("-"*(j+4))
        file_object.write(f"\n|{phone:^{j+3}}|\n")
        file_object.write("-"*(j+4))
        file_object.write(f"\n|{headers[0]:^{k}}|{headers[1]:^{k}}" )
        file_object.write(f"|{headers[2]:^{k}}|{headers[3]:^{k}}|\n" )
        file_object.write("-"*(j+4))

    for stock in stocks:
        
        index = stocks.index(stock)

        stock_symbol = stocks[index].symbol
        number_shares = stocks[index].number_shares
        number_shares_str = number_shares
    
        gain = stocks[index].gain()
        gain_str = "$" + str(round(gain,2))
    
        yearly_gain = stocks[index].yearly_percent_gain()
        yearly_gain_str = str(round(yearly_gain,2)) + "%"

        gains_list.append(gain/number_shares)
        stocks_list.append(stock_symbol)
    
        typ = get_report_data(filename_write)
        with open(filename_write, typ) as file_object:
            file_object.write(f"\n|{stock_symbol:^{k}}|{number_shares_str:^{k}}|")
            file_object.write(f"{gain_str:^{k}}|{yearly_gain_str:^{k}}|\n")
            file_object.write("-"*(j+4))
    
    #determine the index of the stock with max gain per-share basis 
    i = gains_list.index(max(gains_list))

    if max(gains_list) < 0:
        typ = get_report_data(filename_write)
        with open(filename_write, typ) as file_object:
            file_object.write("\nThe Stock with the least decrease in value in your portfolio")
            file_object.write(" on a per-share basis is: " + stocks_list[i] + "\n")
    else:
        typ = get_report_data(filename_write)
        with open(filename_write, typ) as file_object:
            file_object.write("\nThe Stock with the highest increase in value in your portfolio")
            file_object.write(" on a per-share basis is: " + stocks_list[i] + "\n")
    print(f'File {filename_write} created successfully... Check directory ')

def get_stock_report_display(stocks, owner, filename_write):
    """	Output Stock Report to text file specified"""
    gains_list = []
    stocks_list = []
    table = []
    
    #Declare uniform title for print report and determine the lenght
    title = f"Stock ownership for {owner.name}"
    address = f"{owner.address}"
    phone = f"{owner.phone}"
    #String heades for print report
    headers = ["Stock", "Share #", "Earnings/Loss", "Yearly Earning/Loss"]

    #Find width for table based on headers and title
    table.append(Header(headers, title))
    #Return values for print table
    j, k, m, n = table[0].header_width()
    
    print("-"*(j+4))
    print(f"|{title:^{j+3}}|")
    print("-"*(j+4))
    print(f"|{address:^{j+3}}|")
    print("-"*(j+4))
    print(f"|{phone:^{j+3}}|")
    print("-"*(j+4))
    print(f"|{headers[0]:^{k}}|{headers[1]:^{k}}" +
          f"|{headers[2]:^{k}}|{headers[3]:^{k}}|" )
    print("-"*(j+4))

    for stock in stocks:
        
        index = stocks.index(stock)

        stock_symbol = stocks[index].symbol
        number_shares = stocks[index].number_shares
        number_shares_str = number_shares
    
        gain = stocks[index].gain()
        gain_str = "$" + str(round(gain,2))
    
        yearly_gain = stocks[index].yearly_percent_gain()
        yearly_gain_str = str(round(yearly_gain,2)) + "%"

        gains_list.append(gain/number_shares)
        stocks_list.append(stock_symbol)
    
        print(f"|{stock_symbol:^{k}}|{number_shares_str:^{k}}|" + 
                    f"{gain_str:^{k}}|{yearly_gain_str:^{k}}|")
        print("-"*(j+4))
    
    #determine the index of the stock with max gain per-share basis 
    i = gains_list.index(max(gains_list))

    if max(gains_list) < 0:
        print("\nThe Stock with the least decrease in value in your portfolio" + 
             " on a per-share basis is: " + stocks_list[i] + "\n")
    else:
        print("\nThe Stock with the highest increase in value in your portfolio" +
             " on a per-share basis is: " + stocks_list[i] + "\n")

def get_bond_data(data):
    """	Create Bond Class Objects"""
    bond_data_list = []
    headers = []

    for line in data:
        if data.index(line) == 0:
            headers.append(line.rstrip())
        else:
            line_whole = line.rstrip().replace('\n', '')
            line_split = line.split(',')
            bond_symbol = str(line_split[symbol_index])
            number_shares = int(line_split[shares_index])
            purchase_price = float(line_split[purchase_price_index])
            current_price = float(line_split[current_price_index])
            purchase_date = str(line_split[purchase_date_index])
            coupon = float(line_split[coupon_index])
            yield_percent = float(line_split[yield_index])
            bond_data = Bond(data.index(line),bond_symbol,number_shares,
                               purchase_price,current_price,purchase_date,
                               coupon,yield_percent)
            bond_data_list.append(bond_data)

        headers_split = headers[0].split(',')
        symbol_index = headers_split.index('SYMBOL')
        shares_index = headers_split.index('NO_SHARES')
        purchase_price_index = headers_split.index('PURCHASE_PRICE')
        current_price_index = headers_split.index('CURRENT_VALUE')
        purchase_date_index = headers_split.index('PURCHASE_DATE')
        coupon_index = headers_split.index('Coupon')
        yield_index = headers_split.index('Yield')
        
    
    return bond_data_list

def get_bond_report_text(bonds, owner, filename_write):
    """	Output Bond Report to text file specified"""
    gains_list = []
    bonds_list = []
    table = []

    #Declare uniform title for print report and determine the lenght
    title = f"Bond ownership for {owner.name}"
    address = f"{owner.address}"
    phone = f"{owner.phone}"
    #String heades for print report
    headers = ["Bond", "Quantity","Coupon", "Yield", "Earnings/Loss", "Yearly Earning/Loss"]

    #Find width for table based on headers and title
    table.append(Header(headers, title))
    #Return values for print table
    j, k, m, n = table[0].header_width()
    
    with open(filename_write, 'w') as file_object:
        file_object.write("-"*(j+6))
        file_object.write(f"\n|{title:^{j+4}}|\n")
        file_object.write("-"*(j+6))
        file_object.write(f"\n|{address:^{j+4}}|\n")
        file_object.write("-"*(j+6))
        file_object.write(f"\n|{phone:^{j+4}}|\n")
        file_object.write("-"*(j+6))
        file_object.write(f"\n|{headers[0]:^{k}}|{headers[1]:^{k}}" )
        file_object.write(f"|{headers[2]:^{k}}|{headers[3]:^{k}}" )
        file_object.write(f"|{headers[4]:^{k}}|{headers[5]:^{k}}|\n" )
        file_object.write("-"*(j+6))


    for bond in bonds:
        
        index = bonds.index(bond)

        bond_symbol = bonds[index].symbol
        number_shares = bonds[index].number_shares
        number_shares_str = number_shares

        bond_symbol = bonds[index].symbol
        
        number_shares = bonds[index].number_shares
        number_shares_str = number_shares
    
        coupon = bonds[index].coupon
        coupon_str = str(coupon)
    
        yield_percent = bonds[index].yield_percent
        yield_percent_str = str(yield_percent) + "%"
     
        gain = bonds[index].gain()
        gain_str = "$" + str(round(gain,2))
    
        yearly_gain = bonds[index].yearly_percent_gain()
        yearly_gain_str = str(round(yearly_gain,2)) + "%"

        gains_list.append(gain/number_shares)
        bonds_list.append(bond_symbol)
        
        typ = get_report_data(filename_write)
        with open(filename_write, typ) as file_object:
            file_object.write(f"\n|{bond_symbol:^{k}}|{number_shares_str:^{k}}|")
            file_object.write(f"{coupon_str:^{k}}|{yield_percent_str:^{k}}|")
            file_object.write(f"{gain_str:^{k}}|{yearly_gain_str:^{k}} |\n")
            file_object.write("-"*(j+6))
    
    
    #determine the index of the stock with max gain per-share basis 
    i = gains_list.index(max(gains_list))

    if max(gains_list) < 0:
        typ = get_report_data(filename_write)
        with open(filename_write, typ) as file_object:
            file_object.write("\nThe Stock with the least decrease in value in your portfolio")
            file_object.write(" on a per-share basis is: " + bonds_list[i] + "\n")
    else:
        typ = get_report_data(filename_write)
        with open(filename_write, typ) as file_object:
            file_object.write("\nThe Stock with the highest increase in value in your portfolio")
            file_object.write(" on a per-share basis is: " + bonds_list[i] + "\n")
    print(f'File {filename_write} created successfully... Check directory ')

def get_bond_report_display(bonds, owner, filename_write):
    """	Output Bond Report to text file specified"""
    gains_list = []
    bonds_list = []
    table = []

    #Declare uniform title for print report and determine the lenght
    title = f"Bond ownership for {owner.name}"
    address = f"{owner.address}"
    phone = f"{owner.phone}"
    #String heades for print report
    headers = ["Bond", "Quantity","Coupon", "Yield", "Earnings/Loss", "Yearly Earning/Loss"]

    #Find width for table based on headers and title
    table.append(Header(headers, title))
    #Return values for print table
    j, k, m, n = table[0].header_width()
    

    print("-"*(j+6))
    print(f"|{title:^{j+4}}|")
    print("-"*(j+6))
    print(f"|{address:^{j+4}}|")
    print("-"*(j+6))
    print(f"|{phone:^{j+4}}|")
    print("-"*(j+6))
    print(f"|{headers[0]:^{k}}|{headers[1]:^{k}}" +
          f"|{headers[2]:^{k}}|{headers[3]:^{k}}" +
          f"|{headers[4]:^{k}}|{headers[5]:^{k}}|" )
    print("-"*(j+6))


    for bond in bonds:
        
        index = bonds.index(bond)

        bond_symbol = bonds[index].symbol
        number_shares = bonds[index].number_shares
        number_shares_str = number_shares

        bond_symbol = bonds[index].symbol
        
        number_shares = bonds[index].number_shares
        number_shares_str = number_shares
    
        coupon = bonds[index].coupon
        coupon_str = str(coupon)
    
        yield_percent = bonds[index].yield_percent
        yield_percent_str = str(yield_percent) + "%"
     
        gain = bonds[index].gain()
        gain_str = "$" + str(round(gain,2))
    
        yearly_gain = bonds[index].yearly_percent_gain()
        yearly_gain_str = str(round(yearly_gain,2)) + "%"

        gains_list.append(gain/number_shares)
        bonds_list.append(bond_symbol)
        
        print(f"|{bond_symbol:^{k}}|{number_shares_str:^{k}}|" +
              f"{coupon_str:^{k}}|{yield_percent_str:^{k}}|" +
              f"{gain_str:^{k}}|{yearly_gain_str:^{k}} |")
        print("-"*(j+6))
    
    
    #determine the index of the stock with max gain per-share basis 
    i = gains_list.index(max(gains_list))

    if max(gains_list) < 0:
        print("\nThe Stock with the least decrease in value in your portfolio" +
              " on a per-share basis is: " + bonds_list[i] + "\n")
    else:
        print("\nThe Stock with the highest increase in value in your portfolio" +
              " on a per-share basis is: " + bonds_list[i] + "\n")

def get_stock_prices_data(filename, filename_database):
    ''' get Stock prices over a period of time '''
    try:
        with open(filename) as json_file:
            data_set = json.load(json_file)
            data_set.reverse()
            stock_dictionary = {}
            stocks_shares = read_stock_table(filename_database)

            for stock in data_set:
                if stock['Symbol'] not in stock_dictionary:
                    new_stock = Stocks(stock['Symbol'], stock['Date'],
                                      stock['Open'], stock['High'], stock['Low'], 
                                      stock['Close'], stock['Volume'])
                    print(stock['Symbol'] + " added")
                    stock_dictionary[stock['Symbol']] = new_stock
                else:
                    stock_dictionary[stock['Symbol']].open_price = stock['Open']
                    stock_dictionary[stock['Symbol']].high_price = stock['High']
                    stock_dictionary[stock['Symbol']].low_price = stock['Low']
                    stock_dictionary[stock['Symbol']].close_price = stock['Close']
                #iterate to find number of shares 
                for shares in stocks_shares:
                    if stock['Symbol'] == shares.symbol:
                        shares_number = shares.number_shares
                        break
                stock_dictionary[stock['Symbol']].add_price(stock['Close'],
                            datetime.strptime(stock['Date'], '%d-%b-%y'), 
                            shares_number)
    except FileNotFoundError:
        print(str(filename) + ' file not found error')
    else:
        return stock_dictionary
