def add (x,y):
    result = x+y
    return result

def substract (x,y):
    result = x-y
    return result

def divide (x,y):
    result = x/y
    return result

def multiply (x,y):
    result = x*y
    return result

def remainder (x,y):
    result = x%y
    return result

def powerof (x,y):
    result = x**y
    return result


def sum(*numbers):
    total = 0
    for number in numbers:
        total+=number
        return total

def multiply_many(*numbers):
    product =1
    for number in numbers:
        product*=number
        return product
    



def insert_value_at_position(array, index, value):
    array.insert(index, value)

# Example usage:
my_list = [1, 2, 4, 5]
index = 2
new_value = 3

insert_value_at_position(my_list, index, new_value)

print(my_list)  # Output: [1, 2, 3, 4, 5]




def calculate_final_price(purchase_amount, discount_percentage):
    if 0 < discount_percentage <= 100:
        discount_amount = (purchase_amount * discount_percentage) / 100
        final_price = purchase_amount - discount_amount
    else:
        final_price = purchase_amount  # No discount applied
    return final_price
# Example usage:
purchase_amount = 1000
discount_percentage = 20
final_price = calculate_final_price(purchase_amount, discount_percentage)
print("Final price:", final_price)
