import random
import matplotlib.pyplot as plt
import numpy as np

class Action():

    def __init__(self, move):       #initierer en ny instans av klassen, alle oop trenger sånne i python
        self.move = move

    def __str__(self):              #tekstlig rapportering
        if(self.move == "p"):
            return "Paper"
        if(self.move == "s"):
            return "Scissors"
        if(self.move == "r"):
            return "Rock"

    def __eq__(self, other):        #equal operator
        return self.move == other.move

    def __gt__(self, other):        #greater than operator
        return ((self.move == "p" and other.move == "r") or (self.move == "s" and other.move == "p") or (self.move == "r" and other.move == "s"))


class Player():
#spillerklassen. vil ved default velge tilfeldig om stein saks eller papir

    possible_moves = ["r", "p", "s"]

    def __init__(self):
        self.name = "Random"
        self.points = 0.0
        self.opponent_move = ""

    #velg akssjon: velger hvilken aksjon sm skal utføres
    #aka spille stein saks eller papir og returnere dette
    def choose_action(self):
        return random.choice(self.possible_moves)       #velger tilfeldig handling her

    #motte resultat: etter at enkeltspill er over får vi vite hva som ble valgt av begge spillerne
    #og hvem som vant
    def receive_result(self, won, opponent_move):
        self.opponent_move = opponent_move
        if(won == 2):
            self.points += 1
        elif(won == 1):
            self.points += .5

    def __str__(self):
        return str(self.name)

class Seq(Player):      #sequential player, går igjennom fast rekkefølge uansett

    def __init__(self):
        Player.__init__(self)
        self.name = "Sequential"
        self.counter = 0

    def choose_action(self):
        self.counter = (self.counter + 1) % 3       #bruker heltallsdiv for å
        return self.possible_moves[self.counter]


class Most_Common(Player):
#ser på moststanderens valg over tid, velger random på det første valget tho

    plays = {"r" : 0, "p" : 0, "s": 0}

    def __init__(self):
        Player.__init__(self)
        self.name = "Most Common"

    def receive_result(self, won, opponent_move):
        Player.receive_result(self, won, opponent_move)
        self.plays[opponent_move] += 1

    def choose_action(self):
        if (not(self.opponent_move == "")):
            highest = 0
            mov = ""
            for move, freq in self.plays.items():
                if (freq > highest):
                    highest = freq
                    mov = move
            if(not mov ==  ""):
                return self.possible_moves[(self.possible_moves.index(mov) +1 ) % 3]
        return Player.choose_action(self)


class Historian(Player):
#ser mønsteret i spilleren, ser på hva motspiller liker å spille etter siste trekk. ved trekk der disse ikke eksisterer enda, velges tilfeldig
    moves = []

    def __init__(self, history):
        Player.__init__(self)
        self.history = history
        self.name = "Historian"

    def receive_result(self, won, opponent_move):
        Player.receive_result(self, won, opponent_move)
        self.moves.insert(0, opponent_move)

    def choose_action(self):
        if(len(self.moves) < self.history):
            return Player.choose_action(self)
        following_moves = {"r" : 0, "p" : 0, "s" :0}
        for x in range(1, len(self.moves) - self.history):
            passed = True
            for y in range (0, self.history):
                if(not(self.moves[y] == self.moves[x+y])):
                    passed = False
            if(passed):
                following_moves[self.moves[x-1]] += 1
        highest = 0
        mov = ""
        for move, freq in following_moves.items():
            if (freq > highest):
                highest = freq
                mov = move
        if(not mov ==  ""):
            return self.possible_moves[(self.possible_moves.index(mov)+1)%3]
        return Player.choose_action(self)


class SingleGame():
#simulering av et game

    def __init__(self, p1, p2):         #initierer spilelr 1 og 2
        self.p1 = p1
        self.p2 = p2
        self.victor = ""
        self.move = ""
        self.played = False

    def run_game(self):                 #gjennomfører spillet
        self.played = True
        a1 = Action(self.p1.choose_action())    #spillerne velger handling
        a2 = Action(self.p2.choose_action())
        if (a1 > a2):                           #winnerconditions
            self.victor = self.p1
            self.move = a1.move
            self.p1.receive_result(2, a2.move)
            self.p2.receive_result(0, a1.move)
        elif(a1 == a2):
            self.move = a1.move
            self.p1.receive_result(1, a2.move)
            self.p2.receive_result(1, a1.move)
        else:
            self.victor = self.p2
            self.move = a2.move
            self.p1.receive_result(0, a2.move)
            self.p2.receive_result(2, a1.move)

    def __str__(self):
        if(self.victor != ""):
            result = str(str(self.victor) + " won the round between " + str(self.p1) + " and " + str(self.p2) + " using " + str(self.move))
        else:
            result = str(str(self.p1) + " and " + str(self.p2) + " tied as they both used " + str(self.move))
        return result



class ManyGame():
#tar inn spiller, motstander og antall runder

    def __init__(self, p1, p2, rounds):
        self.p1 = p1
        self.p2 = p2
        self.rounds = rounds

    def arrange_game(self):                 #arrangerer et og et game, av klassen singlegames
        game = SingleGame(self.p1, self.p2)
        game.run_game()
        #print(game)                                                    ####print ut rundeinfo

    def arrange_tourney(self):              ##turneringsformatet!
        win = []
        for x in range (1, self.rounds):
            self.arrange_game()
            win.append(round(100*(self.p1.points/(self.p1.points + self.p2.points))))
        print(str(self.p1) +" won " + str(round(100*(self.p1.points/(self.p1.points + self.p2.points)), 1)) + "% of their matches")
        print(str(self.p2) +" won " + str(round(100*(self.p2.points/(self.p1.points + self.p2.points)), 1)) + "% of their matches")
        plt.title(str(self.p1) + " win percentage over rounds")
        plt.xlabel("Number of Rounds")
        plt.ylabel("Win Percentage")
        plt.plot(win)
        plt.axis([0, self.rounds, 0, 100])
        plt.show()


if __name__ == "__main__":
#mainfunksjon


    #s = Most_Common()
    s = Seq()
    h = Historian(2)
    m = ManyGame(s, h, 100)
    m.arrange_tourney()
