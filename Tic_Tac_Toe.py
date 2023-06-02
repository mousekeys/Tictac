
tictac={'TOP-L':' ','TOP-M':' ','TOP-R':' ','MID-L':' ','MID-M':' ','MID-R':' ', 'LOW-L':' ','LOW-M':' ','LOW-R':' '}
#Makin a tutorial

def tutorial():
    print("To provide the location, read the locations given below \n")
    print('TOP-L' +' | '+ 'TOP-M' +' | '+ 'TOP-R')
    print('------+-------+------')
    print('MID-L' +' | '+ 'MID-M' +' | '+ 'MID-R')
    print('------+-------+------')
    print('LOW-L' +' | '+ 'LOW-M' +' | ' +'LOW-R')

    print("\n The locations are not case-sensitive.")





#Makin a tictactoe board.
def printboard():
    print(tictac['TOP-L'] + ' | '+ tictac['TOP-M'] +' | '+ tictac['TOP-R'])
    print('--+---+--')
    print(tictac['MID-L'] +' | '+ tictac['MID-M'] +' | '+ tictac['MID-R'])
    print('--+---+--')
    print(tictac['LOW-L'] +' | '+ tictac['LOW-M'] +' | ' + tictac['LOW-R'])

# Chechin if the win condn has been reached.
# probably can make it better.
def cwin():
    if tictac['TOP-R']==tictac['TOP-M'] and  tictac['TOP-L']==tictac['TOP-M'] and tictac['TOP-R']!=' ' and tictac['TOP-L']!=' ':
        print("You have won.")  
        exit(0) 

    if tictac['MID-R']==tictac['MID-M'] and  tictac['MID-L']==tictac['MID-M'] and tictac['MID-R']!=' ' and tictac['MID-L']!=' ':
        print("You have won.")
        exit(0)
    
    if tictac['LOW-R']==tictac['LOW-M'] and  tictac['LOW-L']==tictac['LOW-M'] and tictac['LOW-R']!=' ' and tictac['LOW-L']!=' ':
        print("You have won.")
        exit(0)

    if tictac['TOP-R']==tictac['MID-M'] and  tictac['LOW-L']==tictac['MID-M'] and tictac['TOP-R']!=' ' and tictac['MID-L']!=' ':
        print("You have won.")
        exit(0)

    if tictac['TOP-L']==tictac['MID-M'] and  tictac['LOW-R']==tictac['MID-M'] and tictac['LOW-R']!=' ' and tictac['TOP-L']!=' ':
        print("You have won.")
        exit(0)


# PLays the actual game 

def play():
    Turn='X'
# 9 as there are max 9 moves
    for i in range(9):
        tutorial()
        print()
        printboard()

        print("For turn of "+ Turn +". Where would it be placed :")
        name=input().upper()

    #This will see that the X and O done get overwritten.
        while tictac[name]=='X' or tictac[name]=='O':  
            print("That place has already been filled.Try another unfilled place: ")
            printboard()
            print("For turn of "+ Turn +". Where would it be placed :")
            name=input().upper()

        tictac[name]=Turn

        if Turn=='X':
            Turn='O'
        else:
            Turn='X'

        cwin()


play()
