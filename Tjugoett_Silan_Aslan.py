
"""Individuell Inlämningsuppgift. Silan Aslan / DevOps24 / Programmering1
Tjugoett! 
Enligt följande regler:
Spelet går till så att spelaren får ett kort i taget och efter varje kort får avgöra om han vill ha ytterligare kort eller inte. 
Det gäller för spelaren att försöka få summan av kortens valörer så nära 21 som möjligt utan att överskrida detta tal. 
Ess räknas som antingen 1 eller 14.
Om spelaren får över 21 förlorar hen och datorn vinner.
Om spelaren stannar under 21 får också datorn dra ett kort i taget och efter varje kort avgöra om den skall fortsätta eller inte. 
Om datorn får mer än 21 poäng eller lägre poäng än användaren vinner användaren, annars vinner datorn.
Datorn vinner alltså på samma poäng.
"""
import random


class Deck():
    """Kortlek för spelet"""
    def __init__ (self):
        """Skapar kortlek med värden enligt spelregler"""
        self.cards = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
   

    def shuffle(self) -> None:
        """Blandar kortleken"""
        random.shuffle(self.cards)
        
    def deal_card(self) -> int:
        """Delar ut ett kort från toppen av kortleken."""
        return self.cards.pop()

class Player:
    """Spelare i spelet."""
    def __init__(self, name: str):
        self.name = name
        self.cards: list[int] = []
    
    def take_card(self, card: int) -> None:
        """Lägger till ett kort i spelarens hand"""
        self.cards.append(card)

    def get_score(self) -> int:
        """ Beräknar spelarens poäng och returnerar totala poängen. 
        Om ess (14) finns och summan överstiger 21, räknas esset som 1 poäng."""
        if 14 in self.cards and sum(self.cards) > 21:
            return sum(self.cards) - 13

        return sum(self.cards)


    

def compare(p_score: int, c_score: int) -> str:
    """Jämför spelarens och datorns poäng och returnerar resultatet""" 
    if p_score > 21 and c_score > 21:
        return "Både har spruckit! Datorn vinner."
    elif p_score == c_score:
        return "Lika! Datorn vinner."
    elif c_score == 21:
        return "Datorn har 21. Du förlorar!"
    elif p_score == 21:
        return "Du vinner med 21!"
    elif p_score > 21:
        return "Du har spruckit! Datorn vinner!"
    elif c_score >21:
        return "Datorn har spruckit! Du vinner!"
    elif p_score > c_score:
        return "Du vinner!"
    else:
        return "Du förlorar!"


def play_game() -> None: 
    """Huvudfunktion för att spela en omgång av spelet"""

    print(r"""
            .------.                  
            |A_  _ |.                         
            |( \/ ).-----.               
            | \  /|K /\  |                      
            |  \/ | /  \ |
            `-----| \  / |                
                  |  \/ K|              
                  `------'  

╔═══════════════════════════════════╗           
║           T J U G O E T T         ║
╚═══════════════════════════════════╝     


""")

    deck = Deck()
    deck.shuffle()

    player = Player("Spelaren")
    computer = Player ("Datorn")

    


   
    # Delar ut första kortet till spelaren
    player.take_card(deck.deal_card())


    is_game_over: bool = False
    while not is_game_over:
        player_score = player.get_score()
        computer_score = computer.get_score()

        print(f"\nDu: \n{player.cards} \nSumma: {player_score}\n")

        if player_score > 21:
            is_game_over = True
        elif player_score == 21 or computer_score == 21:
            is_game_over = True
        else:
            user_should_deal = input("Skriv 'j' för ett till kort, skriv 'n' för att stanna:  ").lower()
            if user_should_deal == "j":
                player.take_card(deck.deal_card())
            else:
                is_game_over = True

    # Datorns tur att dra kort
    while computer_score != 21 and computer_score < 17:
        computer.take_card(deck.deal_card())
        computer_score = computer.get_score()

    # Visar resultat och vinnare
    print(f"\nDatorn: \n{computer.cards} \nSumma: {computer_score}\n")
    print(compare(player_score, computer_score))

# Huvudloop för att starta nya spel
while input("""\nVill du spela en omgång Tjugoett? Skriv 'j' för ja eller 'n' för nej: """).lower() == "j":
    print("\n" * 20) # Rensa
    play_game()

# Avslutningsmeddelande
print("\nTack! Ha en fin dag.\n")