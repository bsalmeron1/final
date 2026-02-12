
# Jacqueline Sandoval. Breanna Tepetongo, Adrian Marqetequesias
drink = ['boba', 'breanna pee', 'jackie diarrhea']
chiraw = ['mr Q', 'King V' , 'Chief K', 'MLK']
pastries=['fish tentacle', 'pompri placenta', 'konguru pickled ramble']

name = input( "What's your name?: " ) #f string so we have to put it in parenthesis but before quotes when referencing it
def nowantdrink(answer):
    if answer == "yes": 
        print(f" Awesome {name}-chan!")
        print(f"The drinks are:", str(drink)  )
        drinks = input(f"Choose your drink ^-^ {name}")
        print(f"Okay {name}, your {drinks} is coming right up!")
        print(f"Here's your {drinks}, {name}! ")
        
    elif answer == "no":
        print(f"No... {name}-chan, dom't starve yourself, but ok!: ")  #f infront in order to refer to the name in the output of the 
        


def nowantpastries(answer):
    if answer == "yes": 
        print(f" Awesome {name}-chan!")
        print(f"The pastries are ",str(pastries) + ":" )
        pastries = input(f"Choose your pastries {name}  ")
        print(f"Okay {name}, your {pastries} is coming right up!")
    elif answer == "no":
        print(f"No... {name}-chan, dom't starve yourself, but ok!: ")  #f infront in order to refer to the name in the output of the 


def listen(answer):
    print(f"Choose an artist to listen to",str(chiraw))
    ccc= input(": ")


print(f"Welcome {name}-Chan, welcome to the Cat Cafe! ^-^") #were gunna make two of these one being  drink one and patry to refer to their seperate lists easier
answer= input("Do you want a drink?:  ")

nowantdrink(answer)
listen(answer)

