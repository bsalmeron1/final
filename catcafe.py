
# Jacqueline sandwichhis. Breanna Tepetongo, Adrian Marqetequigluesias
drink = {'boba': 3,
          'smoothie pee' :7,
          'jackie diarrhea' : 1 }
chiraw = ['mr Q', 'King V' , 'Chief K', 'MLK']
pastries ={'fish tentacle':  10
            , 'pompri placenta' : 12
            , 'konguru pickled ramble': 2}
total=0
name = input( "~~~~~~~~What's your name Senpai ^-^ ?: ~~~~~~~~~" ) #f string so we have to put it in parenthesis but before quotes when referencing it
def nowantdrink(answer):
    global total #global for something outside the function to be able to refer to it and change it in the function    
    if answer == "yes":
        print(f" Awesome {name}-chan!")
        print(f"The drink options are:", str(drink)  )
        print()
        drinks = input(f" What would you like {name}-chan? ^-^:")
        if drinks in drink:
            price = drink[drinks]
            total += price
        print(f"Okay {name}-chan, your {drinks} is coming right up!")
        print()
        print()
        print()
        print(f"Here's your {drinks}, {name}-chan! ")
        print(f"Enjoy your drink! ^-^")
        return drinks
        
    elif answer == "no":
        print(f"No... {name}-chan, dom't starve yourself, but ok!: ")  #f infront in order to refer to the name in the output of the 
        


def nowantpastries(answers):
    if answers == "yes": 
        global total
        print(f" Okie, {name}-chan!")
        print(f"The pastries are : " ,str(pastries) )
        print()
        pastriest = input(f"Choose your pastries,{name}-chan ")
        if pastriest in pastries:
            price = pastries[pastriest]
            total += price #adds price to list named total so we can refer to it later when we ask if they want a receipt
        print(f"Okay {name}-chan , your {pastriest} is coming right up!")
        print()
        print()
        print()
        print(f"Here's your {pastriest}, {name}-chan! Enjoy! ^-^")
        return pastriest
    elif answers == "no":
        print(f"No... {name}-chan, dont starve yourself, but ok!: ")  #f infront in order to refer to the name in the output of the 


def listen(an):
    if an == "yes":
        print(f"The artists avaiable to listen to are ", str(chiraw))
        ccc = input( f"Who do you like to jam to? ... ")
        print()
        print()
        print(f"Now playing..  .{ccc}")
    elif an == "no":
        print("Suit yourself")



print(f"Welcome {name}-Chan, welcome to the Cat Cafe! ^-^") #were gunna make two of these one being  drink one and patry to refer to their seperate lists easier
while True: 
    answer= input("Do you want a drink?:  ")

    drinks= nowantdrink(answer) 
    answers= input("Do you want a pastries ?:  ")#performs the first loop of asking drink question
    pastriest= nowantpastries(answers)
    an= input("Do you want to listen to art?")
    listen(an) #performs the second iteration of what tolistern tok
    again = input("Would you like to order again? (yes or no): ")
    if again == "no":
        break

receipt = input("Do you want your receipt? (yes/no)")
if receipt == "yes":
    print(f" Receipt for {name}-chan")
    print(f"Total spent: ${total}")
    money = input( "How would be you paying? (cash or card) ")
    if money == "cash":
        print(f"Okay {name}-chan, please pay the cashier! ")
        print(f"Payment successful! Thank you for your purchase, {name}-chan! ")
    elif money == "card":
        print(f"Okay {name}-chan, please swipe your card! ")
        print(f"Payment successful! Thank you for your purchase, {name}-chan! ")
    print(f"Thank you for coming to the Cat Cafe! Please come again soon.^-^")