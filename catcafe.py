
# Jacqueline Sandoval. Breanna Tepetongo, Adrian Marqetequesias
drink = {'boba': 2.99,
          'breanna pee' :.99,
          'jackie diarrhea' : 10.99 }
chiraw = ['mr Q', 'King V' , 'Chief K', 'MLK']
pastries ={'fish tentacle':  15.00
            , 'pompri placenta' :6.99
            , 'konguru pickled ramble': 10.00}

name = input( "What's your name?: " ) #f string so we have to put it in parenthesis but before quotes when referencing it
def nowantdrink(answer):
    if answer == "yes": 
        print(f" Awesome {name}-chan!")
        print(f"The drinks are:", str(drink)  )
        drinks = input(f"Choose your drink ^-^ {name}-chan  ")
        print(f"Okay {name}-chan, your {drinks} is coming right up!")
        print(f"Here's your {drinks}, {name}-chan! ")
        
    elif answer == "no":
        print(f"No... {name}-chan, dom't starve yourself, but ok!: ")  #f infront in order to refer to the name in the output of the 
        


def nowantpastries(answers):
    if answers == "yes": 
        print(f" Awesome {name}-chan!")
        print(f"The pastries are : " ,str(pastries) )
        pastriest = input(f"Choose your pastries {name}-chan ")
        print(f"Okay {name}-chan , your {pastriest} is coming right up!")
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
nowantdrink(answer) 
answers= input("Do you want a pastries ?:  ")#performs the first loop of asking drink question
nowantpastries(answers)
an= input("Do you want to listen to art?")
listen(an) #performs the second iteration of what tolistern tok




receipt = input("Do you want your recept? (yes/no)")
if reciept == "yes" or "Yes":
    rug= []