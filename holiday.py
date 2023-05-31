'''This code for calculation a user's holiday cost including the plane cost, hotel cost and rental car cost'''

def hotel_cost(num_nights, h_cost = 95): # # Declaring a function for total cost of number of nights in the hotel
    return  num_nights * h_cost 
     

def plane_cost(city_flight): # # Declaring a function for total cost of flight cost

    ticket = 0    
    while city_flight: #While loop trough chooses of city flight: 4 options

        if city_flight == "London":
            ticket = 345
            break
        elif city_flight == "Manchester":
            ticket = 200
            break
        elif city_flight == "Bristol":
            ticket = 400
            break
        elif city_flight == "Birmingham":
            ticket = 278
            break
        else:
            print("Please choose your city flight")

    return ticket

def car_rental(rental_days, c_cost = 155): # # Declaring a function for total cost of number of days for rental car
    return rental_days * c_cost

def holiday_cost(num_nights, city_flight, rental_days): # # Declaring a function - total amount for holiday cost
    num_nights = hotel_cost(num_nights)  # Call function for each argument
    city_flight = plane_cost(city_flight)
    rental_days = car_rental(rental_days)
    return num_nights + city_flight + rental_days #returning sum

city_flight = input(" Enter the city you want to fly to: \nLondon \nManchester \nBristol, \nBirmingham \nChoose your flight direction : ")
num_nights = int(input("Enter numbers of nights you are planing to stay in the hotel : "))
rental_days = int(input("Enter the number of days that you will be hiring a car for : "))


total = holiday_cost(num_nights, city_flight, rental_days) # Result
print(total)

