Menu={'Appetizers':[('Pizza Fries', 250),('Salad',250),('Honey Wings', 380),('Garlic Bread', 200),\
('Boneless Wings', 220),('Nachos', 180),('Fries', 80),('Fish Crackers',200),('Shrimps', 350),('Cheesy Dip', 220),\
('Korean Fried Wings', 550),('Crispy Fish',450),('Chips And Dips', 450)],\
'Desi Dishes':[('Jeera Rice', 200),('Biryani', 300),('Neehari', 350),('Keema', 350),\
('Karahi', 350),('Paneer Handi', 350),('Reshmi Handi', 350),('Tandoori Chicken', 400),('Palak Paneer', 350),\
('Tikka', 350),('Malai Boti', 350),('Bihari Boti', 350)], 'Chinese':[('Chicken Manchurian', 350),('Chicken Lime', 250),\
('Prawns', 700),('Chicken Chowmein', 300),('Veg Chowmein', 250),('Hot And Sour Soup',350),('Sizzling Garlic',450),\
('Dry Chilli', 500),('Chinese Rice', 320),('Hot Sizzler', 500)],'Fast Foods':[('Zinger Burger',250),\
('Beef Burger',300),('Chicken Chatni Roll', 250),('Fajita Pizza', 400),('Arabic Pizza', 500),('Sisalian Pizza', 450),\
('Chicken Cheese Sandwich', 280),('Club Sandwich', 225),('Zinger Roll', 140),('Broast', 200),('Chicken Garlic Mayo Roll', 300),\
('Veggie Burger', 300),('Veggie Pizza', 400),('Cheese Pizza', 400),('Crispy Sandwich', 350)],\
'Beverages':[('Cococola', 100),('Hot Chocolate', 400),('Cocktail', 350),\
('Pina Colata', 350),('Mocha', 350),('Frappe', 350),('Blueberry Slush', 400),('Soft Drink', 100),('Fresh Lime', 200),\
('Mango Shake', 200),('Chocolate Shake', 250),('Kitkat Shake', 250),('Oreo Shake', 220),('Strawberry Shake', 250)],\
'Desserts':[('Kheer', 300),('Caramel Puding', 400),('Chocolate Icecream', 250),('Mango Icecream', 250),\
('Pista Icecream', 200),('Bunty Icecream', 250),('Brownie', 80),('Chocolate Cake', 300),('Cupcake', 80),('Cookie', 80)]}



print('Hello!')
print('Welcome to "The food world wants" restaurant. \nThankyou for choosing our restaurant.\n')
print('Please tell your name')
name=input()
print('This is our menu:\n')
for key, value in Menu.items():
     print(key, ':')
     for j in value:
         print(j)
     print()


def push(lst, item):
    lst.append(item)
    return lst


# Recommendation for the most ordered dish
def orders(filename):
    d={}
    with open("Customers_Record.txt") as f:
        for line in f:
            key, val = line.split(":")
            s = val.replace("\n","")
            li=list(s[1:-1].split(','))
            d[key]=li
    return (d)
print(orders('Customers_Record.txt'))

d=orders(('Customers_Record.txt'))
freq=dict()
for i in d.keys():
    for j in d[i]:
        if j not in freq:
            freq[j]=1
        else:
            freq[j]+=1
# print(freq)

values=list(freq.values())
def recommendation(values):
    a=max(values)
    kv={}
    for k,v in freq.items():
        if a==v:
            kv[k]=v
    print(kv)
    print('This is the most ordered dish of our restaurant, would uou like to have it?')
    inp=input()
    if inp=='Yes' or inp=='yes':
        print('Please add this in your dishes')
    else:
        print('Okay:), Please provide your order!')
(recommendation(values))

##Recommending previous customers their previous dishes.
d=orders(('Customers_Record.txt'))
def recommend_previous_dishes(d):
    for key in d:
        if name == key:
            print(d[key])
            print('These are the dishes you ordered last time.\n We recommend you to order them again:)')
(recommend_previous_dishes(d))

#Food ordering
lst=[]
total=[]
def Order_processing(Menu):
    price=0
    while True:
        keys=list(Menu.keys())
        key=','.join(keys)
        print('Please select your cuisine among', str(key))
        cuisine = input()
        Dishes=Menu[cuisine]
        print('select your dishes from the chosen cuisine')
        list_of_dishes = []
        dish = input()
        push(list_of_dishes, dish)
        for i in list_of_dishes:
            for j in i.split(','):
                push(lst, j)
                # lst+=j
        for j in lst:
            for i in Dishes:
                if i[0]==j:
                    print('How much quantity do you want for', j)
                    quantity_of_j = int(input())
                    price = quantity_of_j * i[1]
                    push(total, price)
        print('Do you want to select some other cuisine?')
        b = input()
        if b =='Yes' or b == 'yes':
            Order_processing(Menu)
        else:
            if b=='No' or b=='no':
                # lst=lst.replace(' ','')
                print('This is your order:', lst) 
                print('Thankyou for your order, you will recieve your order soon!')
        break
(Order_processing(Menu))


# Billing
def Counting_price(total):
    count=0
    for i in total:
        count+=i
    Total=count
    print('Hello, your total bill is: ',Total)
    while True:
        Total_money= int(input('Please pay the bill:'))
        if Total_money == (Total):
            print('Thank you for visiting!\n Hope to see you again:)')
            break
        elif Total_money > Total:
            change = Total_money - (Total)
        
            print('Thank you for visiting, here is the change', change,'\nHope to see you again:)')
            break
        else:
            c=(Total)-Total_money
            print('Sorry, but you need to pay ',c,'more\nThank you for visiting\n Hope to see you again:)')
            break
Counting_price(total)


#Saving data
data=name+':'+str(lst)+'\n'
def saving_data(data):
    with open("Customers_Record.txt", "r+") as f:
        text=(f.read())
        f.write(data)
saving_data(data)



#Adding dishes
key='Beverages'
value=('Pomegranate Juice', 250)
def add_dishes(Menu, key, value):
    # We are making this function to help the admin to add dishes as per their convenience.
    Keys=list(Menu.keys())
    for i in Keys:
        if i==key:
            push(Menu[key], value)
    return Menu
# print(add_dishes(Menu, key, value))

# Removing dishes
def remove(lst, value):
    for i in lst:
        if i[0] == value:
            lst.remove(i)
    return(lst)

##Deleting dishes 
key='Desi Dishes'
dish_to_delete='Bihari Boti'
def delete_dishes(Menu, key, dish_to_delete):
    # We are making this function to help the admin to delete dishes as per their convenience.
    Keys=list(Menu.keys())
    for i in Keys:
        if i==key:
            (remove(Menu[key], dish_to_delete)) #using the remove code.
            # print(Menu)
# print(delete_dishes(Menu, key, dish_to_delete))









