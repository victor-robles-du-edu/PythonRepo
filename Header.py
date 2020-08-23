""" 
********************************************************************** 
Description: Header values for tables outputs
			 
Author: Victor Robles 

Project: Header
 
Revision: 07/26/2020
********************************************************************** 
"""


class Header():
    def __init__(self, headers, title, size=2):
        self.headers = headers
        self.title = title
        self.size = size
    
    def header_width(self):
        max_lenght = 0
        for header in self.headers:
            lenght = int(len(header))
            max_lenght += lenght 

        self.j = int(max_lenght*self.size)
        self.k = int(self.j/len(self.headers))
        self.m = int(self.j-len(self.title)+1)
        self.n = self.j + 3
        return self.j, self.k, self.m, self.n

    def return_title(self):
        print_string = f'|{self.title}{"":^{self.m}}|'
        return print_string
        
    def return_header(self):
        print_string = ''
        for header in self.headers:
            print_string = print_string + f'|{header:^{self.k}}'
        print_string = print_string + '|'
        return print_string
