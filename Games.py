"""
Created on Sat Mar 27 

@author: ktk
"""
import pyttsx3,random,os,re,itertools
from tkinter import *
from tkinter import messagebox
from random import randint
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def sub(x):
    speak(x)
    print(x)
affirm=["yes","y","Y","Yes"]
def magicball():
    while True:
        speak("What do you want to ask the Magic 8 ball?")
        question =input("Ask the magic 8 ball a question: \n(press enter to quit) ")
        answers = random.randint(1,8)
        if question == "":
            break
        elif answers == 1:
            sub ("It is certain")
        elif answers == 2:
            sub ("Outlook good")
        elif answers == 3:
            sub ("You may rely on it")
        elif answers == 4:
            sub ("Ask again later")
        elif answers == 5:
            sub ("Concentrate and ask again")
        elif answers == 6:
            sub ("Reply hazy, try again")
        elif answers == 7:
            sub ("My reply is no")
        elif answers == 8:
            sub ("My sources say no")
def dice():
    while True:
        speak("How many die do you want to roll")
        choice=(input('''Do you want to roll \n1) 1 die \n2) 2 dice \n(press enter to quit) \n'''))
        if choice=="":
            break
        elif choice==1:
            min = 1
            max = 6
            roll_again = "yes"
            affirm=["yes","y","Y","Yes"]
            while roll_again in affirm:
                speak ("Rolling the die...")
                sub ("The value is....")
                sub (random.randint(min, max))
                roll_again =input("Roll the die again? ")
                print("")
        elif choice==2:
            min = 1
            max = 6
            roll_again = "yes"
            affirm=["yes","y","Y","Yes"]
            while roll_again in affirm:
                speak ("Rolling the dices...")
                sub ("The values are....")
                sub (random.randint(min, max))
                sub (random.randint(min, max))
                roll_again =input("Roll the dices again? ")
                print("")
def janken():
    os.system('cls' if os.name=='nt' else 'clear')
    on=True
    while on:
        print ("")
        sub ("Rock, Paper, Scissors - Shoot!")
        userChoice =input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
        if not re.match("[SsRrPp]", userChoice):
            sub ("Please choose a letter:")
            print ("[R]ock, [S]cissors or [P]aper.")
            continue
        sub (f"You chose: {userChoice}")
        choices = ['R', 'P', 'S']
        opponenetChoice = random.choice(choices)
        sub (f"I chose: {opponenetChoice}")
        if opponenetChoice == str.upper(userChoice):
            sub ("Tie! ")
        elif opponenetChoice == 'R' and userChoice.upper() == 'S':      
            sub ("Scissors beats rock, I win! ")
        elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
            sub ("Scissors beats paper! I win! ")
        elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
            sub ("Paper beat rock, I win! ")
        else:       
            sub ("You win!")
        play_on=input("Do you want to play again? ")
        if play_on in affirm:
            continue
        else:
            break
def tictactoe():
    while True:
        board=[i for i in range(0,9)]
        player, computer = '',''
        moves=((1,7,3,9),(5,),(2,4,6,8))
        winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        tab=range(1,10)
        def print_board():
            x=1
            for i in board:
                end = ' | '
                if x%3 == 0:
                    end = ' \n'
                    if i != 1: end+='---------\n';
                char=' '
                if i in ('X','O'): char=i;
                x+=1
                print(char,end=end)
        def select_char():
            chars=('X','O')
            if random.randint(0,1) == 0:
                return chars[::-1]
            return chars
        def can_move(brd, player, move):
            if move in tab and brd[move-1] == move-1:
                return True
            return False
        def can_win(brd, player, move):
            places=[]
            x=0
            for i in brd:
                if i == player: places.append(x);
                x+=1
            win=True
            for tup in winners:
                win=True
                for ix in tup:
                    if brd[ix] != player:
                        win=False
                        break
                if win == True:
                    break
            return win
        def make_move(brd, player, move, undo=False):
            if can_move(brd, player, move):
                brd[move-1] = player
                win=can_win(brd, player, move)
                if undo:
                    brd[move-1] = move-1
                return (True, win)
            return (False, False)
        def computer_move():
            move=-1
            for i in range(1,10):
                if make_move(board, computer, i, True)[1]:
                    move=i
                    break
            if move == -1:
                for i in range(1,10):
                    if make_move(board, player, i, True)[1]:
                        move=i
                        break
            if move == -1:
                for tup in moves:
                    for mv in tup:
                        if move == -1 and can_move(board, computer, mv):
                            move=mv
                            break
            return make_move(board, computer, move)
        def space_exist():
            return board.count('X') + board.count('O') != 9
        player, computer = select_char()
        sub('Player is [%s] and computer is [%s]' % (player, computer))
        result='Draw !!!'
        while space_exist():
            print_board()
            print('#Make your move !! [1-9] : ', end='')
            move = int(input())
            moved, won = make_move(board, player, move)
            if not moved:
                sub('Invalid number !! Try again !!')
                continue
            if won:
                result='*** Congratulations !! You won the game !! ***'
                break
            elif computer_move()[1]:
                result="I'm sorry, you lost the game."
                break;
        print_board()
        sub(result)
        choice=input("Do you want to play again? ")
        if choice in affirm:
            continue
        else:
            break
def survivalgame():
    while True:
        commands = { 
                "i" : "see inventory", 
                "c" : "see crafting options", 
                "craft [item]" : "craft something from inventory items", 
           } 
        items = { 
                    "flint" : 50, 
                    "grass" : 100, 
                    "hay" : 0, 
                    "tree" : 100, 
                    "log" : 0, 
                    "sapling" : 100, 
                    "twig" : 0, 
                    "boulder" : 30, 
                    "rock" : 0, 
                    "pickaxe" : 0, 
                    "axe" : 0, 
                    "firepit" : 0, 
                    "tent" : 0, 
                    "torch" : 0, 
                } 
        craft = { 
                    "hay" : { "grass" : 1 }, 
                    "twig" : { "sapling" : 1 }, 
                    "log" : { "axe" : 1, "tree" : 1 }, 
                    "axe" : { "twig" : 3, "flint" : 1 }, 
                    "tent" : { "twig" : 10, "hay" : 15 }, 
                    "firepit" : { "boulder" : 5, "log" : 3, "twig" : 1, "torch" : 1 }, 
                    "torch" : { "flint" : 1, "grass" : 1, "twig" : 1 }, 
                    "pickaxe" : { "flint" : 2, "twig" : 1 } 
                } 
         
        sub("'Crafting Challenge' Game") 
        print("-----------------------------------------\n")
        sub("TRY TO SURVIVE BY CRAFTING A TENT AND A FIREPIT!") 
        sub("type '?' for help") 
        while True: 
            command = input(">").split() 
            if len(command) == 0: 
                continue 
            if len(command) > 0: 
                verb = command[0].lower() 
            if len(command) > 1: 
                item = command[1].lower() 
            if verb == "?": 
                for key in commands: 
                    print(key + " : " + commands[key]) 
                print("\n") 
            elif verb == "i": 
                for key in items: 
                    print(key + " : " + str(items[key])) 
                print("\n") 
            elif verb == "c": 
                for key in craft: 
                    sub(f"{key} can be made with:") 
                    for i in craft[key]: 
                        print(str(craft[key][i]) + " " + i) 
                    print("\n")
            elif verb == "craft": 
                sub(f"making {item}:")  
                if item in craft: 
                    for i in craft[item]: 
                        sub(f"  you need : {(str(craft[item][i]))}  {i} and you have {(str(items[i]))}") 
                    canBeMade = True 
                    for i in craft[item]: 
                        if craft[item][i] > items[i]: 
                            sub("item cannot be crafted\n") 
                            canBeMade = False 
                            break 
                    if canBeMade == True: 
                        for i in craft[item]: 
                            items[i] -= craft[item][i] 
                        items[item] += 1 
                        sub("item crafted\n")
                    if items["tent"] >= 1 and items["firepit"] >= 1: 
                        sub("\n**YOU HAVE MANAGED TO SURVIVE!\nWELL DONE!") 
                        break 
                else: 
                    sub("you can't") 
            else: 
                sub("you can't")
        play=input("Do you want to play again? ")
        if play in affirm:
            continue
        else:
            break
def hangman():
    speak("Enter your name challenger")
    name = input("Enter your name: ")
    while True:
        sub(f"Hello, {name}. Let's play hangman!")
        sub("So what's your first guess?")
        words='''abruptly askew awkward axiom azure bagpipes bandwagon banjo beekeeper bikini blitz blizzard boggle bookworm boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness crypt curacao cycle disavow dizzying duplex dwarves embezzle equip espionage exodus faking fishhook fixable flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak keyhole khaki kilobyte kiosk kiwifruit klutz knapsack larynx lengths lucky luxury lymph matrix megahertz microwave mnemonic mystify nightclub nowadays numbskull nymph onyx ovary oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch stronghold stymied subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz wave wavy waxy wellspring wheezy whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch wyvern xylophone yachtsman yippee yoked youthful yummy zephyr zigzag zigzagging zilch zipper zodiac zombie'''
        a=words.split(" ")
        word=random.choice(a)
        guesses = ''
        turns = 10
        while turns > 0:
            failed = 0              
            for char in word:      
                if char in guesses:    
                  print(char)
                else:
                    print("_")
                    failed += 1    
            if failed == 0:        
                sub("You won")
                break              
            print()
            guess = input("guess a character:") 
            guesses += guess
            if guess not in word:
                turns -= 1        
                sub("Wrong Guess")
                sub(f"You have {turns} more guesses")
                if turns == 0:
                    sub ("You Lose")
        play_again=input("Do you want to play again? ")
        if play_again in affirm:
            continue
        else:
            break
def guessthenumber():
    while True:
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        sub("Try to guess a number between 0 to 100.")
        x=random.randint(0,100)
        sub("You have only 7 chances to guess the number.")
        count=0
        while count<=7:
            count +=1
            guess=int(input("Guess a number: "))
            if x==guess:
                sub(f"Congratulations, you did it in {ordinal(count)} try.")
                break
            elif x>guess:
                sub("You guessed under the value.")
            elif x<guess:
                sub("You guessed above the value.")
        if count>7:
            sub(f"The number is {x}")
            sub("Better luck next time!!")
        play_again=input("Do you want to try guessing another number? ")
        if play_again in affirm:
            continue
        else:
            break
def game2048():
    while True:
        class Board:
            bg_color={
                '2': '#eee4da',
                '4': '#ede0c8',
                '8': '#edc850',
                '16': '#edc53f',
                '32': '#f67c5f',
                '64': '#f65e3b',
                '128': '#edcf72',
                '256': '#edcc61',
                '512': '#f2b179',
                '1024': '#f59563',
                '2048': '#edc22e',
            }
            color={
                 '2': '#776e65',
                '4': '#f9f6f2',
                '8': '#f9f6f2',
                '16': '#f9f6f2',
                '32': '#f9f6f2',
                '64': '#f9f6f2',
                '128': '#f9f6f2',
                '256': '#f9f6f2',
                '512': '#776e65',
                '1024': '#f9f6f2',
                '2048': '#f9f6f2',
            }
            def __init__(self):
                self.n=4
                self.window=Tk()
                self.window.title('ProjectGurukul 2048 Game')
                self.gameArea=Frame(self.window,bg= 'azure3')
                self.board=[]
                self.gridCell=[[0]*4 for i in range(4)]
                self.compress=False
                self.merge=False
                self.moved=False
                self.score=0
                for i in range(4):
                    rows=[]
                    for j in range(4):
                        l=Label(self.gameArea,text='',bg='azure4',
                        font=('arial',22,'bold'),width=4,height=2)
                        l.grid(row=i,column=j,padx=7,pady=7)
                        rows.append(l);
                    self.board.append(rows)
                self.gameArea.grid()
            def reverse(self):
                for ind in range(4):
                    i=0
                    j=3
                    while(i<j):
                        self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                        i+=1
                        j-=1
            def transpose(self):
                self.gridCell=[list(t)for t in zip(*self.gridCell)]
            def compressGrid(self):
                self.compress=False
                temp=[[0] *4 for i in range(4)]
                for i in range(4):
                    cnt=0
                    for j in range(4):
                        if self.gridCell[i][j]!=0:
                            temp[i][cnt]=self.gridCell[i][j]
                            if cnt!=j:
                                self.compress=True
                            cnt+=1
                self.gridCell=temp
            def mergeGrid(self):
                self.merge=False
                for i in range(4):
                    for j in range(4 - 1):
                        if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                            self.gridCell[i][j] *= 2
                            self.gridCell[i][j + 1] = 0
                            self.score += self.gridCell[i][j]
                            self.merge = True
            def random_cell(self):
                cells=[]
                for i in range(4):
                    for j in range(4):
                        if self.gridCell[i][j] == 0:
                            cells.append((i, j))
                curr=random.choice(cells)
                i=curr[0]
                j=curr[1]
                self.gridCell[i][j]=2
            
            def can_merge(self):
                for i in range(4):
                    for j in range(3):
                        if self.gridCell[i][j] == self.gridCell[i][j+1]:
                            return True
                
                for i in range(3):
                    for j in range(4):
                        if self.gridCell[i+1][j] == self.gridCell[i][j]:
                            return True
                return False
            def paintGrid(self):
                for i in range(4):
                    for j in range(4):
                        if self.gridCell[i][j]==0:
                            self.board[i][j].config(text='',bg='azure4')
                        else:
                            self.board[i][j].config(text=str(self.gridCell[i][j]),
                            bg=self.bg_color.get(str(self.gridCell[i][j])),
                            fg=self.color.get(str(self.gridCell[i][j])))
        class Game:
            def __init__(self,gamepanel):
                self.gamepanel=gamepanel
                self.end=False
                self.won=False
            def start(self):
                self.gamepanel.random_cell()
                self.gamepanel.random_cell()
                self.gamepanel.paintGrid()
                self.gamepanel.window.bind('<Key>', self.link_keys)
                self.gamepanel.window.mainloop()
            
            def link_keys(self,event):
                if self.end or self.won:
                    return
                self.gamepanel.compress = False
                self.gamepanel.merge = False
                self.gamepanel.moved = False
                presed_key=event.keysym
                if presed_key=='Up':
                    self.gamepanel.transpose()
                    self.gamepanel.compressGrid()
                    self.gamepanel.mergeGrid()
                    self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                    self.gamepanel.compressGrid()
                    self.gamepanel.transpose()
                elif presed_key=='Down':
                    self.gamepanel.transpose()
                    self.gamepanel.reverse()
                    self.gamepanel.compressGrid()
                    self.gamepanel.mergeGrid()
                    self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                    self.gamepanel.compressGrid()
                    self.gamepanel.reverse()
                    self.gamepanel.transpose()
                elif presed_key=='Left':
                    self.gamepanel.compressGrid()
                    self.gamepanel.mergeGrid()
                    self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                    self.gamepanel.compressGrid()
                elif presed_key=='Right':
                    self.gamepanel.reverse()
                    self.gamepanel.compressGrid()
                    self.gamepanel.mergeGrid()
                    self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                    self.gamepanel.compressGrid()
                    self.gamepanel.reverse()
                else:
                    pass
                self.gamepanel.paintGrid()
                print(self.gamepanel.score)
                flag=0
                for i in range(4):
                    for j in range(4):
                        if(self.gamepanel.gridCell[i][j]==2048):
                            flag=1
                            break
                if(flag==1): #found 2048
                    self.won=True
                    messagebox.showinfo('2048', message='You Wonnn!!')
                    print("won")
                    return
                for i in range(4):
                    for j in range(4):
                        if self.gamepanel.gridCell[i][j]==0:
                            flag=1
                            break
                if not (flag or self.gamepanel.can_merge()):
                    self.end=True
                    messagebox.showinfo('2048','Game Over!!!')
                    print("Over")
                if self.gamepanel.moved:
                    self.gamepanel.random_cell()
                
                self.gamepanel.paintGrid()
            
        gamepanel =Board()
        game2048 = Game( gamepanel)
        game2048.start()
        play_again=input("Do you want to play it again? ")
        if play_again in affirm:
            continue
        else:
            break
def guesstheanimal():
    tree = [0,"QIs it a mammal","QDoes it spend all of its time on land","QIs it a bird","QIs it feline","QDoes it ever leave the water","QCan it fly","QIs it an insect","QIs it a domestic pet","QCan it be milked","Aseal","QDoes it have conical teeth and a single blowhole","Asparrow","QDoes it swim","QDoes it sting","QHas it got eight limbs","Acat","QDoes it have stripes","QDoes it produce wool","QIs it traditionally ridden",20,21,"Adolphin","Awhale",24,25,"Apenguin","Aostrich","QDoes it produce honey","QDoes it have a narrow waist","QDoes it live in water","Asquid",32,33,"Atiger","Alion","Asheep","Acow","Ahorse","QIs it farmed",40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,"Abee","Awasp","Aant","Atermite","Aoctopus","Aspider",62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,"Apig","Adog"]
    current = 1
    print("Answer the questions to identify an animal from the following list: horse, cow, sheep, pig, dog, cat, lion, tiger, whale, dolphin, seal, penguin, ostrich, sparrow, spider, ant, bee, wasp, termite, octopus, squid\n")
    while tree[current][0] == "Q":
      answer = input(tree[current][1:] + "? [Y/N] ").lower()
      if answer in ("y","yes","ye","yeah"):
        current = current * 2
      else:
        current = current * 2 + 1
    sub(f"My guess would be...{tree[current][1:]}")
def spinayarn():
   while True:
        when=["About 100 years ago","In the 47 BC","Once upon a time","A long time ago","Yesterday","Long before you were born","In the far future","A decade after Thanos decimated earth","On 14th March"]
        who=["a rabbit","an elephant","a mouse","a tiger","a turtle","a lonely stormtrooper","an old sage","Iron Man","Blackbeard, the pirate,"]
        where=["Arkham Asylum","Stark Tower","King's fall","California","Barclona","Venice"]
        what = ['to eat a lot of cakes', 'to fight for justice', 'to steal ice cream', 'to dance']
        sub(f"{random.choice(when)} {random.choice(who)} went to {random.choice(where)} {random.choice(what)}")
        play_again=input("Do you want to try creating another story? ")
        if play_again in affirm:
            continue
        else:
            break
def guessthequote():
    while True:
        quote={'“If you don’t share someone’s pain, you can never understand them.”':"Nagato",
                '"War brings death. And wounds and pain to both sides. There’s nothing harder to accept, than the deaths of those you love. So you believe they could never die. Especially those who haven’t known war."':"Nagato",
                '“The concept of hope is nothing more than giving up. A word that holds no true meaning.”':"Madara Uchiha",
                '“The longer you live… The more you realize that reality is just made of pain, suffering and emptiness.” ':"Madara Uchiha",
                '“When a man learns to love, he must bear the risk of hatred.”':"Madara Uchiha",
                '“In this world, wherever there is light – there are also shadows. As long as the concept of winners exists, there must also be losers. The selfish desire of wanting to maintain peace causes wars, and hatred is born to protect love.”':"Madara Uchiha",
                '“When people are protecting something truly precious to them. They truly can become…as strong as they need to be!”':"Haku",
                '“Rejection is a part of any man’s life. If you can’t accept and move past rejection, or at least use it as writing material – you’re not a real man.”':"Jiraiya",
                '“A place where someone still thinks about you is a place you can call home.”':"Jiraiya",
                '“When people get hurt, they learn to hate… When people hurt others, they become hated and racked with guilt. But knowing that pain allows people to be kind. Pain allows people to grow… and how you grow is up to you.”':"Jiraiya",
                '“Even I can tell that hatred is spreading. I wanted to do something about it…but I don’t know what. I believe… that someday the day will come when people truly understand one another!”':"Jiraiya",
                '“Because they saved me from myself, they rescued me from my loneliness. They were the first to accept me for who I am. They’re my friends.”':"Naruto Uzamaki",
                '“If you don’t like your destiny, don’t accept it. Instead have the courage to change it the way you want it to be.”':"Naruto Uzamaki",
                '“The pain of being alone is completely out of this world, isn’t it? I don’t know why, but I understand your feelings so much, it actually hurts.”':"Naruto Uzamaki",
                'No one cared who I was until I put on a mask.”':"Obito Uchiha",
                '“Somewhere inside of me? Take a good look, there’s nothing inside of me anymore! I don’t feel pain, I don’t feel anything! You need to let that guilt go. This wind hole wasn’t your doing… It was made by this evil, cruel world.”':"Obito Uchiha",
                'In the ninja world, those who don’t follow the rules are trash. But, those who abandon their friends are even worse than trash.”':"Obito Uchiha",
                '“We are humans, not fish. We don’t know what kind of people we truly are until the moment before our deaths. As death comes to embrace you, you will realize what you are. That’s what death is, don’t you think?”':"Itachi Uchiha",
                '“Love is the reason why there is pain. When we lose someone precious to us, hate is born. Vengeance is the product of that hate and so death follows. But in death there is only more death. This will give rise to more pains. In this cursed world we live in, it is a cycle of hatred that will not cease. You and I seek the same thing that Jiraiya-sensei wanted. Let me ask you this: How will you confront this hatred in order to create peace?”':"Nagato",
                '“If love is just a word, then why does it hurt so much if you realize it isn’t there?”':"Gaara",
                '“The hole in one’s heart gets filled by others around you. Friends won’t flock to someone who abandons the memory of his friends and gives up on the world just because things don’t go the way he wants them to. That won’t help fill the hole in your heart. And people won’t help those who run away and do nothing. As long as you don’t give up, there will always be salvation.”':"Kakashi Hatake",
                "I lost my teacher, so it's not like I don't understand what you're going through. But whining and sulking isn't going to make things better. We're way past that point in our lives. My teacher entrusted me with many things. Some important, some petty. All sorts of things. You too, right? In fact, you must have a ton of stuff. So don't you think it's about time for us to step up? Time for us to become the ones who entrust. It's a pain, but we can't keep complaining. You will eventually be the one treating others to ramen… and you'll be called Naruto-sensei, or something. We can't stay brats forever. If we want to become super cool ninja":"Shikamaru Nara",
                "There, that ending… was a little better. The frog at the bottom of the well drifts off into the great ocean. Heh heh… yep… pretty damn honourable… pretty damn honourable… I guess it's time to put down my pen. Right… I need a title for the next book… let's see… Ah, got it… The Tale of Naruto Uzumaki… perfect.":"Jiraiya",
                "From the First Great Ninja War to the last, shinobi have woundd an come to hate each ohter for the benefit of their own nation and village. That hatred led to a desire for power, and that desire for power created someone like me. In the past, I too was once full of hatred and power. I was a Jinchuriki. I hated this world and all the people in it. I constantly thought of nothing but destroying it. I was no different than what akatsuki is now. However a certain shinobi from Konoha stopped me. He shed tears for me! His enemy! Enevn though I hurt him, he still called me his friend. He saved me. My enemy! My fellow jinchurki! He suffered the same pain as me and yet bore no ill will. The moment we understood each other's pain, our malice will disappear. There are no enemies here. We are all one and it is because we have all been affected by akatsuki. The sand village, Stone Village, Leaf Village, Mist Village, Cloud Village, They no longer exist. We are only shinobi. If you still cannot forgive the sand village then I will give you my head once this war is over. Our enemy is now after the very friend who saved me. If they capture him it will be the end of the world. I want to protect him. I want to protect this world. However I am too young and naive to do so. This is why, I need all of you to give me your strengths. To protect our friends and this world, we will fight as one, until our dying breaths.":"",
                '"When I decided to follow my dream, I had already discarded my life."':"Roronoa Zoro",
                "If I can't even protect my captain's dream, then whatever ambition I have is nothing but talk...":"Roronoa Zoro",
                "You've underestimated me, snow woman. When you thought you couldn't beat me, you should have run. Of course, there are things that I don't wanna cut. But... let me ask you something. Have you ever seen a fierce animal you were sure would never bite? Because I haven't.":"Roronoa Zoro",
                "I don't know. I'm not sure why myself. But if I were to take even one step back, I believe that all those important oaths, promises and many other deals 'til now, will all go to waste and I'll never be able to return before you, ever again.":"Roronoa Zoro",
                '"There is someone that I must meet again. And until that day...not even Death itself can take my life away!"':"Roronoa Zoro",
                "A wound that'd make an ordinary man unconscious... I won't lose to it. A wound that would kill an ordinary person... I won't lose to it! To face one who is extraordinary, Hawk Eyes... I can't allow myself to be ordinary!":"Roronoa Zoro",
                "When you decided to go to the sea, it was your own decision. Whatever happens to you on the sea, it depends on what you've done! Don't blame others!!":"Roronoa Zoro",
                "I'm going to be the world's greatest swordsman! All I have left is my destiny! My name may be infamous...but it's gonna shake the world!!!":"Roronoa Zoro",
                "The world isn't perfect. But it's there for us, doing the best it can....that's what makes it so damn beautiful.":"Roy Mustang",
                "We are all like fireworks: we climb, we shine and always go our separate ways and become further apart. But even when that time comes, let's not disappear like a firework and continue to shine.. forever.":"Hitsugaya Toshiro",
                "Those who stand at the top determine what's wrong and what's right! This very place is neutral ground! Justice will prevail, you say? But of course it will! Whoever wins this war becomes justice!":"Don Quixote Doflamingo",
                "I am the hope of the universe. I am the answer to all living things that cry out for peace. I am protector of the innocent. I am the light in the darkness. I am truth. Ally to good! Nightmare to you!" :"Son Goku",
                "People, who can’t throw something important away, can never hope to change anything.":"Armin Arlert",
                "Power comes in response to a need, not a desire. You have to create that need.":"Son Goku",
                "Fools who don’t respect the past are likely to repeat it.":"Nico Robin",
                'Through action, a man becomes a Hero. Through death, the hero becomes legend. Through time, the legend becomes a Myth. And by learning from the myth, a man takes action.':"Corazon",
                "A man's dream will never die!":"Edward Teach Blackbeard",
                "The true measure of a shinobi is not how he lives but how he dies. It’s not what they do in life but what they did before dying that proves their worth.":"Jiraiya",
                "No, they weren't! It's us who gives meaning to our comrades' lives. The brave fallen! The anguished fallen! The ones who will remember them are us, the living! We die trusting the living who follow to find meaning in our lives! That is the sole method with which we can rebel against this cruel world. My soldiers, rage! My soldiers, scream! My soldiers, fight!":"Erwin Smith",
                '“Maybe there’s only a dark road up ahead. But you still have to believe and keep going. Believe that the stars will light your path, even a little bit. Come on, let’s go on a journey!”':"Kaori Miyazano",
                '"When do you think people die? When they are shot through the heart by the bullet of a pistol? No. When they are ravaged by an incurable disease? No. When they drink a soup made from a poisonous mushroom!? No! It’s when they are forgotten."':"Hiluluk",
                "I'm not here tonight as the son of Touichi Kuroba, your mentor in magic, nor as the second-year high school student you call 'Young Master'. Tonight I'm the one they're all talking about. I'm the villain putting on a show.":"Kaitou Kuroba",
                'Pirates are evil? The marines are righteous? These terms have changed throughout history. Kids who have never seen peace and kids who have never seen war have entirely different values. The ones whp rule are the ones at the top, right now, we stand in neutral terrirory. Justice will prevail? Of course it will, because whoever wins... BECOMES JUSTICE! - DonQuixote Doflamingo.':"Don Quixote Doflamingo",
                'It seems like the small leaves in the Leaf Vilage have inherited that "Will of Fire" you spoke of, Third. The fire on the leaves will eventually burn greater and stronger.... It will flash its light and protect this village.':"Iruka Umino",
                'War does not determine who is right – only who is left':"Riza Hawkeye",
                'Greed may not be good, but it’s not so bad either. You humans think greed is just for money or power, but everyone wants something they can’t have':"Greed"}
        a=random.choice(list(quote.keys()))
        b=quote[a]
        sub(f"Here's a quote: {a}")
        remainguess=7
        n=""
        while remainguess>0:
            guess=input(f"GUESSES REMAINING = {remainguess}\nWho said this quote? ")
            if b in guess:
                sub("Congratulations!! You guessed correctly!!")
                break
            remainguess-=1
            if remainguess==6:
                if len(b)>1:
                    n+=b[0]
                    sub(f"Here's a hint: The speaker's name begins with {b[0]}\n{n}")
                if b in guess:
                    sub("Congratulations!! You guessed correctly!!")
                    break
            elif remainguess==5:
                if len(b)>2:
                    n+=b[1]
                    sub(f"Here's a hint: The next letter in the speaker's name is {b[1]}\n{n}")
                if b in guess:
                    sub("Congratulations!! You guessed correctly!!")
                    break
            elif remainguess==4:
                if len(b)>2:
                    n+=b[2]
                    sub(f"Here's a hint: The next letter in the speaker's name is {b[2]}\n{n}")
                if b in guess:
                    sub("Congratulations!! You guessed correctly!!")
                    break
            elif remainguess==3:
                if len(b)>3:
                    n+=b[3]
                    sub(f"Here's a hint: The next letter in the speaker's name is {b[3]}\n{n}")
                if b in guess:
                    sub("Congratulations!! You guessed correctly!!")
                    break
            elif remainguess==2:
                if len(b)>4:
                    n+=b[4]
                    sub(f"Here's a hint: The next letter in the speaker's name is {b[4]}\n{n}")
                if b in guess:
                    sub("Congratulations!! You guessed correctly!!")
                    break    
            elif remainguess==1:
                if len(b)>5:
                    n+=b[5]
                    sub(f"Here's a hint: The next letter in the speaker's name is {b[5]}\n{n}")
                if b in guess:
                    sub("Congratulations!! You guessed correctly!!")
                    break
            else:
                sub(f"Sorry, you ran out of guesses. The answer was {b}")
        play_again=input("Do you want to try guessing another quote? ")
        if play_again in affirm:
            continue
        else:
            break
def drawcards():
    while True:
        speak("How many cards do you want to draw?")
        n=int(input("How many cards do you want to draw? "))
        if n>52:
            sub("There are only 52 cards in a deck. Please draw 52 or less cards.")
        else:
            deck = list(itertools.product(range(1,14),['Spades','Hearts','Diamond','Club']))
            random.shuffle(deck)
            sub("You got:")
            for i in range(n):
                if deck[i][0]==1:
                    a="Ace"
                else:
                    a=deck[i][0]
                sub(a, "of", deck[i][1])
        choice=input("Do you want to draw cards again?? ")
        if choice in affirm:
            continue
        else:
            break
def givecards():
    suit = ("♥","♣","♦","♠")
    value = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    pack = []
    hand = []
    for s in suit:
      for v in value:
        pack.insert(randint(0,len(pack)),v+s)
    players = int(input("How many players? "))
    for i in range(players):
      hand.append([])
    for i in range(len(pack)):
      hand[i % players].append(pack[i])
    for i in range(players):
      print("\nPlayer",i+1,"has:\n"+str(hand[i])[1:-1])
def guessthecard():
    def piles():
      global pile
      pile = [[],[],[]]
      for n in range(len(card)):
        pile[n % 3].append(card[n])
    def display():
      print("\npile 1            pile 2            pile 3")
      print("="*53)
      for y in range(7):
        row = ""
        for x in range(3):
          row += pile[x][y]
          if x < 2:
            row += " "*(18-len(pile[x][y]))
        print(row)
    def combine(col):
      global card
      card = []
      for x in range(col+2,col+5):
        card.extend(pile[x % 3])
    suit = ("Hearts", "Clubs", "Diamonds", "Spades")
    number = ("Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King")
    deck, card = [],[]
    pile = [[],[],[]]
    for s in suit:
      for n in number:
        deck.append(n+" of "+s)
    for n in range(21):
      s = randint(0,len(deck)-1)
      card.append(deck[s])
      deck.pop(s)
    print("\nChoose a card from the table below and I will guess\nwhich one it is:")
    for n in range(3):
      piles()
      display()
      p = int(input("\nWhich pile contains your card? "))-1
      combine(p)
    # display the answer
    print("\nThe card you picked is:",card[10])
def textadventure():
    def you_died(why):
        print_game_over()
        print("{}. Good job!".format(why))
        exit(0)
    def guard():
        print_guard()
        print("You approach the guard, he's still sleeping.")
        print("Suddenly you knocked a wooden cask with a mug on it... CRASSH!")
        print("\nOi, what you doing 'ere?")
        guard_moved = False
        while True:
            next_action = input("[run | door] > ").lower()
            if next_action == "run" and guard_moved:
                you_died("Guard was faster than he looks and your world goes dark...")
            elif next_action == "run" and not guard_moved:
                print("Guard jumps up and looks the other way, missing you entirely.")
                guard_moved = True
            elif next_action == "door" and guard_moved:
                print("You just slipped through the door before the guard realised it.")
                print("You are now outside, home free! Huzzah!")
                return
            elif next_action == "door" and not guard_moved:
                you_died("Guard was faster than he looks and your world goes dark...")
            else:
                print("Not sure what you meant there... try again.")
    def blissful_ignorance_of_illusion_room():
        treasure_chest = ["diamonds", "gold", "silver", "sword"]
        print("You see a room with a wooden treasure chest on the left, and a sleeping guard on the right in front of the door")
        action = input("What do you do? > ")
        if action.lower() in ["treasure", "chest", "left"]:
            print("Oooh, treasure!") 

            print("Open it? Press '1'")
            print("Leave it alone. Press '2'")
            choice = input("> ")
            if choice == "1":
                print("Let's see what's in here... /grins")
                print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
                print("You find some")
                for treasure in treasure_chest:
                    print(treasure)
                print("What do you want to do?")
                print("Take all {} treasure, press '1'".format(len(treasure_chest)))
                print("Leave it, press '2'")
                treasure_choice = input("> ")
                if treasure_choice == "1":
                    print("\tWoohoo! Bounty and a shiney new sword. /drops your crappy sword in the empty treasure chest.")
                    print("\tYou just received [{}]".format(", ".join(treasure_chest)))
                elif treasure_choice == "2":
                    print("It will still be here (I hope), right after I get past this guard")
                guard()
        else:
            print("The guard is more interesting, let's go that way!")
            guard()
    def painful_truth_of_reality_room():
        print_monster()
        print("There you see the great evil Cthulhu.")
        print("He, it, whatever stares at you and you go insane.")
        print("Do you flee for your life or eat your head?")
        next_move = input("> ")
        if "flee" in next_move:
            start_adventure()
        else:
            you_died("You died. Well, that was tasty!")
    def get_player_name():
        name = input("What's your name? > ")
        alt_name = "Rainbow Unicorn"
        answer = input("Your name is {}, is that correct? [Y|N] > ".format(alt_name.upper()))
        if answer.lower() in ["y", "yes"]:
            name = alt_name
            print("You are fun, {}! Let's begin our adventure!".format(name.upper()))
        elif answer.lower() in ["n", "no"]:
            print("Ok, picky. {} it is. Let's get started on our adventure.".format(name.upper()))
        else:
            print("Trying to be funny? Well, you will now be called {} anyway.".format(alt_name.upper()))
            name = alt_name
        return name
    def start_adventure():
        print_dungeon()
        print("You enter a room, and you see a red door to your left and a blue door to your right.")
        door_picked = input("Do you pick the red door or blue door? > ")
        if door_picked == "red":
            painful_truth_of_reality_room()
        elif door_picked == "blue":
            blissful_ignorance_of_illusion_room()
        else:
              print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")
    def main():
        player_name =  get_player_name()
        start_adventure()
        print("\nThe end\n")
        print("Thanks for playing, {}".format(player_name.upper()))
    def print_dungeon(): 
        print()
        print("   _________________________________________________________")
        print(" /|     -_-                                             _-  |\ ")
        print("/ |_-_- _                                         -_- _-   -| \   ")
        print("  |                            _-  _--                      | ")
        print("  |                            ,                            |")
        print("  |      .-'````````'.        '(`        .-'```````'-.      |")
        print("  |    .` |           `.      `)'      .` |           `.    |          ")
        print("  |   /   |   ()        \      U      /   |    ()       \   |")
        print("  |  |    |    ;         | o   T   o |    |    ;         |  |")
        print("  |  |    |     ;        |  .  |  .  |    |    ;         |  |")
        print("  |  |    |     ;        |   . | .   |    |    ;         |  |")
        print("  |  |    |     ;        |    .|.    |    |    ;         |  |")
        print("  |  |    |____;_________|     |     |    |____;_________|  |  ")
        print("  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |")
        print("  |  |  / __  ()        -|        -  |  /  __--      -   |  |")
        print("  |  | /        __-- _   |   _- _ -  | /        __--_    |  |")
        print("  |__|/__________________|___________|/__________________|__|")
        print(" /                                             _ -        lc \ ")
        print("/   -_- _ -             _- _---                       -_-  -_ \ ")
        print()
    def print_monster():
        print()
        print("                           |                     | ")
        print("                        \     /               \     / ")
        print("                       -= .'> =-             -= <'. =- ")
        print("                          '.'.                 .'.' ")
        print("                            '.'.             .'.' ")
        print("                              '.'.----^----.'.' ")
        print("                               /'==========='\ ")
        print("                           .  /  .-.     .-.  \  . ")
        print("                           :'.\ '.O.') ('.O.' /.':   ")
        print("                           '. |               | .'   ")
        print("                             '|      / \      |' ")
        print("                              \     (o'o)     / ")
        print("                              |\             /| ")
        print("                              \('._________.')/ ")
        print("                               '. \/|_|_|\/ .'                ")
        print("                                /'._______.'\ lc ")
        print()
    def print_chest():
        print()
        print("                      _.--. ")
        print("                  _.-'_:-'|| ")
        print("              _.-'_.-::::'|| ")
        print("         _.-:'_.-::::::'  || ")
        print("       .'`-.-:::::::'     || ")
        print("      /.'`;|:::::::'      ||_ ")
        print("     ||   ||::::::'     _.;._'-._ ")
        print("     ||   ||:::::'  _.-!oo @.!-._'-. ")
        print("     ('.  ||:::::.-!()oo @!()@.-'_.| ")
        print("      '.'-;|:.-'.&$@.& ()$%-'o.'-U|| ")
        print("        `>'-.!@%()@'@_%-'_.-o _.|'|| ")
        print("         ||-._'-.@.-'_.-' _.-o  |'|| ")
        print("         ||=[ '-._.-+U/.-'    o |'|| ")
        print("         || '-.]=|| |'|      o  |'|| ")
        print("         ||      || |'|        _| '; ")
        print("         ||      || |'|    _.-'_.-' ")
        print("         |'-._   || |'|_.-'_.-' ")
        print("          '-._'-.|| |' `_.-' ")
        print("              '-.||_/.-' ")
        print()
    def print_guard():
        print()
        print("                                                  ___I___ ")
        print("                                                 /=  |  #\ ")
        print("                                                /.__-| __ \ ")
        print("                                                |/ _\_/_ \| ")
        print("                                                (( __ \__)) ")
        print("                                             __ ((()))))()) __ ")
        print("                                           ,'  |()))))(((()|# `. ")
        print("                                          /    |^))()))))(^|   =\ ")
        print("                                         /    /^v^(())()()v^;'  .\ ")
        print("                                         |__.'^v^v^))))))^v^v`.__| ")
        print("                                        /_ ' \______(()_____(   | ")
        print("                                   _..-'   _//_____[xxx]_____\.-| ")
        print("                                  /,_#\.=-' /v^v^v^v^v^v^v^v^| _| ")
        print("                                  \)|)      v^v^v^v^v^v^v^v^v| _| ")
        print("                                   ||       :v^v^v^v^v^v`.-' |#  \, ")
        print("                                   ||       v^v^v^v`_/\__,--.|\_=_/ ")
        print("                                   ><       :v^v____|  \_____|_ ")
        print("                                ,  ||       v^      /  \       / ")
        print("                               //\_||_)\    `/_..-._\   )_...__\ ")
        print("                              ||   \/  #|     |_='_(     |  =_(_ ")
        print("                              ||  _/\_  |    /     =\    /  '  =\ ")
        print("                               \\\/ \/ )/ gnv |=____#|    '=....#| ")
        print()
    def print_game_over():
        print()
        print("   _____          __  __ ______    ______      ________ _____  ")
        print("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ")
        print(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |")
        print(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ")
        print(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
        print("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\\")
        print()