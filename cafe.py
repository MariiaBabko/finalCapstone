'''This code calculate total stock worth in the cafe '''

menu_list = ["Cookie", "Cupcake", "Vanila cake", "Pestry", "Ice-cream"]
stock = {"Cookie": 40,
        "Cupcake": 30,
        "Vanila cake": 10,
        "Pestry": 15,
        "Ice-cream": 60
        }
price = {"Cookie": 1,
        "Cupcake": 1.5,
        "Vanila cake": 3.5,
        "Pestry": 2.5,
        "Ice-cream": 3.4
        }

stock_value = 0 
for item in menu_list:
    stock_value += (stock[item] * price[item])

print(stock_value)
'''for item in (stock.keys() and price.keys()): #loop through dictionaries
    
  stock_value += (stock[item] * price[item]) 
  

print("Your total stock value is : £ " + str(stock_value) )''' 

