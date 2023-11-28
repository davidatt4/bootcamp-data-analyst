#1
my_fav_numbers=[4,8,21,39,30]
my_fav_numbers.append(89)
my_fav_numbers.append(54)
my_fav_numbers.pop()
print(my_fav_numbers)
friends_fav_numbers=[13,2,4,0,67]
our_fav_numbers=my_fav_numbers+friends_fav_numbers
print(our_fav_numbers)

#2



#3
basket=["Banana","Apples","Oranges","Blueberries"]
basket.pop(0)
print(basket)
basket.pop(2)
print(basket)
basket.append("Kiwi")
print(basket)
basket[2]="Oranges"
basket[1]="Apples"
print(basket.count("Apples"))
basket.clear()
print(basket)
#4



#5
num_list=range(1,21)
for number in num_list:
    print(number)

for num in range(1,21):
    if num%2!=0:
        continue
    print(num)

#6
my_name="David"

while True:
    user_name=input("Please enter your name:")
    print(user_name)

    if user_name is my_name:
       print("Hello David!Nice to see you")
       break
    # else:
    #     print("Please enter a name:")

#7
