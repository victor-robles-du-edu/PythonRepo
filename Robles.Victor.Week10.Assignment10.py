""" 
********************************************************************** 
Description: Investments Application
             
Author: Victor Robles 

Project: Assigment 10
 
Revision: 08/23/2020
********************************************************************** 
"""
#import classes and functions
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from investment import Stock, Bond, Investor
from invest_module import *
from database_module import *
from file_module import *
from charting_module import *
    
def main():
    filename_read_stocks = 'Lesson6_Data_Stocks.csv'
    filename_read_bonds = 'Lesson6_Data_Bonds.csv'
    filename_write_stocks = 'Stocks_Data_Report.txt'
    filename_write_bonds = 'Bonds_Data_Report.txt'
    filename_write_db_stocks = 'Db_Stocks_Data_Report.txt'
    filename_write_db_bonds = 'Db_Bonds_Data_Report.txt'
    filename_json = 'AllStocks.json'
    filename_database = 'investors.db'
    investor = Investor("1", "Bob Smith", "978 Magic St. Orlando Fl. 32819", 
                        "407-900-8000")
    #get files from directory
    read_file_stocks = get_read_data(filename_read_stocks)
    read_file_bonds = get_read_data(filename_read_bonds)
    stocks_investment = get_stock_data(read_file_stocks)
    bonds_investment = get_bond_data(read_file_bonds)
                 
    #GUI Interface
    window = Tk()
    window.title("Investments")
    window.geometry('250x100')    
   
    #GUI Options
    def clicked1():
        get_stock_report_display(stocks_investment, investor, filename_write_stocks)
        get_bond_report_display(bonds_investment, investor, filename_write_bonds)
        
    def clicked2():
        get_stock_report_text(stocks_investment, investor, filename_write_stocks)
        get_bond_report_text(bonds_investment, investor, filename_write_bonds)
        
    def clicked3():
        create_invesment_table(filename_database) 
        write_investor_to_database(investor, filename_database)
        write_stocks_to_database(investor, stocks_investment, filename_database)
        write_bonds_to_database(investor, bonds_investment, filename_database)
        db_stocks = read_stock_table(filename_database)
        db_bonds = read_bond_table(filename_database)
        get_stock_report_text(db_stocks, investor, filename_write_db_stocks)
        get_bond_report_text(db_bonds, investor, filename_write_db_bonds)
        get_stock_report_display(stocks_investment, investor, filename_write_db_stocks)
        get_bond_report_display(bonds_investment, investor, filename_write_db_bonds)
    
    def clicked4():
        stock_prices_dict = get_stock_prices_data(filename_json, filename_database)
        list_range, items_name_list, list_prices_normalized = get_charting_inputs(stock_prices_dict)
        get_line_chart('Stocks Prices Movement', 'Stock_Line_Chart', 
                    list_range, items_name_list, list_prices_normalized)
        get_line_plot('Price Movement', 'Time', 'Price $', 'Stock_Results', 
                    list_range, items_name_list, list_prices_normalized)
        #add to the database
        stocks_data_set = get_json_data(filename_json)
        create_stock_prices_table(filename_database)
        write_stock_prices_to_database(stock_prices_dict, filename_database)
        stock_list = read_stock_prices_table(filename_database)
    
    rad1 = Radiobutton(window,text='Display Reports  ', value=1, command=clicked1)
    rad2 = Radiobutton(window,text='Create Reports   ', value=2, command=clicked2)
    rad3 = Radiobutton(window,text='Write Database   ', value=3, command=clicked3)
    rad4 = Radiobutton(window,text='Create Graphs    ', value=4, command=clicked4)

    rad1.grid(column=0, row=0)
    rad2.grid(column=0, row=1)
    rad3.grid(column=0, row=2)
    rad4.grid(column=0, row=3)

    window.mainloop()

if  __name__ == '__main__':
    main()

#end
