def hello():
    print('Hello User')

hello()


x = "clothes"
y = "shoes"
z = "food"

def pack(x, y, z):
    
    return(x, y, z)
pack_list = pack(x, y, z)
print(pack_list)

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)

my_lunch_food = ["sandwhich", "apple","banana","chips","pudding"]
print(eat_lunch(my_lunch_food))