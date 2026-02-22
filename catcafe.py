
# Jacqueline sandwichhis. Breanna Tepetongo, Adrian Marqetequigluesias
drink = {'boba': 3,
          'breanna pee' :3,
          'jackie diarrhea' : 3 }
chiraw = ['mr Q', 'King V' , 'Chief K', 'MLK']
pastries ={'fish tentacle':  5
            , 'pompri placenta' : 5
            , 'konguru pickled ramble': 5}
total=0
name = input( "What's your name?: " ) #f string so we have to put it in parenthesis but before quotes when referencing it
def nowantdrink(answer):
    if answer == "yes": 
        print(f" Awesome {name}-chan!")
        print(f"The drinks are:", str(drink)  )
        drinks = input(f"Choose your drink ^-^ {name}-chan  ")
        print(f"Okay {name}-chan, your {drinks} is coming right up!")
        print(f"Here's your {drinks}, {name}-chan! ")
        return drinks
        
    elif answer == "no":
        print(f"No... {name}-chan, dom't starve yourself, but ok!: ")  #f infront in order to refer to the name in the output of the 
        


def nowantpastries(answers):
    if answers == "yes": 
        print(f" Awesome {name}-chan!")
        print(f"The pastries are : " ,str(pastries) )
        pastriest = input(f"Choose your pastries {name}-chan ")
        print(f"Okay {name}-chan , your {pastriest} is coming right up!")
        return pastriest
    elif answers == "no":
        print(f"No... {name}-chan, dont starve yourself, but ok!: ")  #f infront in order to refer to the name in the output of the 


def listen(an):
    if an == "yes":
        print(f"The artists avaiable to listen to are ", str(chiraw))
        ccc = input( f"Pick one... ")
        print(f"Now playing..  .{ccc}")
    elif an == "no":
        print("Suit yourself")



print(f"Welcome {name}-Chan, welcome to the Cat Cafe! ^-^") #were gunna make two of these one being  drink one and patry to refer to their seperate lists easier
answer= input("Do you want a drink?:  ")
# while True:
drinks= nowantdrink(answer) 
answers= input("Do you want a pastries ?:  ")#performs the first loop of asking drink question
pastriest= nowantpastries(answers)
an= input("Do you want to listen to art?")
listen(an) #performs the second iteration of what tolistern tok



receipt = input("Do you want your receipt? (yes/no)")
if receipt == "yes" or "Yes":
     drinkcost = drinks
     pastrycost= pastriest
     hun = drinkcost + pastrycost
     print(f"Your total is ${hun} {name}-chan! Thank you for coming to the Cat Cafe! ^-^")