""" 
********************************************************************** 
Description: Database Module to create database, tables and read from 
             database and tables

Author: Victor Robles 

Project: Assigment 10
 
Revision: 08/23/2020
********************************************************************** 
"""

import sqlite3
from investment import Stock, Bond

def create_invesment_table(database_name):
    '''	Function to create the database and the tables (Investor, Stock &
        Bond)'''
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS investor")
        cursor.execute('''CREATE TABLE IF NOT EXISTS investor(
                            investor_ID text PRIMARY KEY,
                            name text NOT NULL,
                            address text NOT NULL,
                            phone text NOT NULL
                            )''')
        cursor.execute("DROP TABLE IF EXISTS stock")
        cursor.execute('''CREATE TABLE IF NOT EXISTS stock (
                            investor_ID text NOT NULL,
                            stock_id text PRIMARY KEY,
                            symbol text NOT NULL,
                            number_shares integer NOT NULL,
                            purchase_price real NOT NULL,
                            current_price real NOT NULL,
                            purchase_date text NOT NULL
                            )''')
        cursor.execute("DROP TABLE IF EXISTS bond")
        cursor.execute('''CREATE TABLE IF NOT EXISTS bond (
                            investor_ID text NOT NULL,
                            bond_id text PRIMARY KEY,
                            symbol text NOT NULL,
                            number_shares integer NOT NULL,
                            purchase_price real NOT NULL,
                            current_price real NOT NULL,
                            purchase_date text NOT NULL,
                            yield_percent real NOT NULL,
                            coupon real
                            )''')


    except sqlite3.OperationalError:
        print('Error creating the database and tables, check again')
    conn.commit()
    print(f'Database {database_name} created successfully...')
    print(f'{database_name} database tables Stock, Bond and Investor created successfully...')
    conn.close()

def create_stock_prices_table(database_name):
    '''	Function to create a table for storing the stocks prices history'''
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS stock_prices")
    cursor.execute('''CREATE TABLE IF NOT EXISTS stock_prices(
                symbol text PRIMARY KEY,
                date_price text NOT NULL,
                open_price real NOT NULL,
                high_price real NOT NULL,
                low_price real NOT NULL,
                close_price real NOT NULL,
                volume integer NOT NULL
              )''')
    conn.commit()
    print(f'{database_name} database table stock_prices created successfully...')
    conn.close()

def write_investor_to_database(investor, database_name):
    """	Function to write Investor Data to the database"""

    #conection
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    #iterate trhough stocks
    cursor.execute("INSERT INTO investor VALUES(?, ?, ?, ?)", (investor.investor_ID,
                                                                    investor.name,
                                                                    investor.address,
                                                                    investor.phone))
    conn.commit()
    print('Investors entered into database...')
    conn.close()

def write_stocks_to_database(investor, stocks, database_name):
    """	Function to write Stocks Data to the database"""

    #conection
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    #iterate trhough stocks
    for stock in stocks:
        cursor.execute("INSERT INTO stock VALUES(?, ?, ?, ?, ?, ?, ?)", 
                                                                (investor.investor_ID,
                                                                    stock.purchase_ID,
                                                                    stock.symbol,
                                                                    stock.number_shares,
                                                                    stock.purchase_price,
                                                                    stock.current_price,
                                                                    stock.purchase_date))
        conn.commit()
    print('Stocks entered into database...')
    conn.close()

def write_bonds_to_database(investor, bonds, database_name):
    """	Function to write Bonds Data to the database"""

    #conection
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    #iterate trhough stocks
    for bond in bonds:
        cursor.execute("INSERT INTO bond VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                                                                (investor.investor_ID,
                                                                    bond.purchase_ID,
                                                                    bond.symbol,
                                                                    bond.number_shares,
                                                                    bond.purchase_price,
                                                                    bond.current_price,
                                                                    bond.purchase_date,
                                                                    bond.yield_percent,
                                                                    bond.coupon))
        conn.commit()
    print('Bonds entered into database...')
    conn.close()

def write_stock_prices_to_database(stocks, database_name):
    """	Function to write stock prices to the database"""

    #conection
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    #iterate trhough stocks
    for key, stock in stocks.items():
        cursor.execute("INSERT INTO stock_prices VALUES(?, ?, ?, ?, ?, ?, ?)", 
                                                                (stock.symbol,
                                                                    stock.date_price,
                                                                    stock.open_price,
                                                                    stock.high_price,
                                                                    stock.low_price,
                                                                    stock.close_price,
                                                                    stock.volume))
        conn.commit()
    conn.close()

def read_stock_table(database_name):
    """ Read from Stock table"""

    stock_data_list = []
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock")
    items = cursor.fetchall()
    
    for item in items:
        stock_data = Stock(item[1],item[2],item[3],item[4],item[5],item[6])
        stock_data_list.append(stock_data)
        
    conn.close()
    return stock_data_list

def read_bond_table(database_name):
    """ Read from Bond table"""

    bond_data_list = []
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bond")
    items = cursor.fetchall()

    for item in items:
        bond_data = Bond(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8])
        bond_data_list.append(bond_data)
        
    conn.close()
    return bond_data_list

def read_stock_prices_table(database_name):
    """ Read from stock prices table"""

    stocks = []
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock_prices")
    items = cursor.fetchall()
    
    for item in items:
        stocks.append(item)
        
    conn.close()

    return stocks

