from random import shuffle # to shuffle the deck
from rich.console import Console # to format coloured text on command line

console = Console()

suits = [
	'♡',
	'♢',
	'♤',
	'♧'
]
ranks = [
	'2',
	'3', 
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'10',
	'J',
	'Q',
	'K',
	'A'
]
values = {
	'2':2,
	'3':3,
	'4':4,
	'5':5,
	'6':6,
	'7':7,
	'8':8,
	'9':9,
	'10':10,
	'J':10,
    'Q':10,
	'K':10,
	'A':11
}
playing = True


# classses for gameplay
class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

class Deck():
	def __init__(self):
		self.deck = [] # holds the cards in a deck

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank)) # builds a card

	def shuffle_deck(self): # shuffles the deck
		shuffle(self.deck)

	def deal_card(self): # removes a card fro deck
		return self.deck.pop()

class Player():
	def __init__(self, isDealer):
		# isDealer attrib is being used to distinguish between human player and computer player
		self.isDealer = isDealer # boolean value is expected for isDealer attrib
		self.cards = [] # holds the cards dealt to the player/dealer
		self.value = 0 # total value of player/dealer's hand
		self.aces = 0 # total number of aces in player/dealer's hand (useful to adjust the value of aces)

	def add_card(self, new_card): # adds one card to player/dealer's hand
		self.cards.append(new_card)
		self.value += values[new_card.rank]
		if new_card.rank == 'A':
			self.aces += 1  # add to self.aces

	def adjust_for_ace (self): # to adjust the value of ace to 1 instead of 11
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

class Chips():
	def __init__(self):
		self.total_chips = 100 # deafult number of chips a player has
		self.bet = 0
	
	def win_bet(self):
		self.total_chips += self.bet

	def lose_bet(self):
		self.total_chips -= self.bet

def take_bet(chips): # prompt the player for their bet
	while True:
		try:
			chips.bet = int(console.input(
				f'\n[bold]How many chips would you like to bet?(Total Chips :point_right: - {chips.total_chips})[/]: '
				))
		except ValueError:
			console.print('Sorry, your bet should be an [bold underline violet]integer[/].')
		else:
			if chips.bet > chips.total_chips:
				console.print(f'Your bet cannot exceed [bold green]{chips.total_chips}[/] chips')
			else:
				break

def hit(deck, player):
	player.add_card(deck.deal_card())
	player.adjust_for_ace()

def hit_or_stand(deck, player): # asks the player whether to hit_or_stand()
	global playing

	while True:
		x = console.input(
			'Would you like to [bold underline]HIT[/] or [bold underline]STAND[/]? Enter H or S: '
			)

		if x[0].lower() == 'h':
			hit(deck, player)
		elif x[0].lower() == 's':
			console.print('[bold green]Player decides to stand[/]. Dealer is playing...')
			playing = False

		else:
			console.print('Sorry! Please try again.', style = 'bold red')
			continue
		
		break

def show_some(player, dealer): # shows some cards of dealer and all cards of player
	# Dealer's Hand
	console.print("[bold green]Dealer's[/] cards:")
	all_cards = [['┌───────┐', '|-------|','|-------|','|-------|','|-------|','|-------|','└───────┘']]
    
	for card in dealer.cards[1:]:
		lines = ['┌───────┐',
				f'| {card.rank:6}|',
				'|       |',
				f'|   {card.suit:4}|',
				'|       |',
				f'|     {card.rank:2}|',
				'└───────┘']

		all_cards.append(lines)

	zipped = zip(*all_cards)
	for tup in zipped:
		print(*tup)

	# Player's Hand
	console.print("[bold green]Player's[/] cards:")
    
	all_cards = []
	for card in player.cards:
		lines = ['┌───────┐',
				f'| {card.rank:6}|',
				'|       |',
				f'|   {card.suit:4}|',
				'|       |',
				f'|     {card.rank:2}|',
				'└───────┘']
		all_cards.append(lines)

	zipped = zip(*all_cards)
	for tup in zipped:
		print(*tup)

def show_all(player, dealer): # shows all the cards of player and the dealer
	# Dealer's hand
	console.print("[bold green]Dealer's[/] cards:")
    
	all_cards = []
	for card in dealer.cards:
		lines = ['┌───────┐',
				f'| {card.rank:6}|',
				'|       |',
				f'|   {card.suit:4}|',
				'|       |',
				f'|     {card.rank:2}|',
				'└───────┘']
		all_cards.append(lines)

	zipped = zip(*all_cards)
	for tup in zipped:
		print(*tup)

	# Player's Hand
	console.print("[bold green]Player's[/] cards:")
    
	all_cards = []
	for card in player.cards:
		lines = ['┌───────┐',
				f'| {card.rank:6}|',
				'|       |',
				f'|   {card.suit:4}|',
				'|       |',
				f'|     {card.rank:2}|',
				'└───────┘']
		all_cards.append(lines)

	zipped = zip(*all_cards)
	for tup in zipped:
		print(*tup)

# funcs to declare win/lose
def player_busts(player,dealer,chips):
	console.print("[bold]Player [violet]busts[/]![/]")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	console.print("[bold]Player [cyan]wins[/]![/]")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	console.print("[bold]Dealer [violet]busts[/]![/]")
	chips.win_bet()
    
def dealer_wins(player,dealer,chips):
	console.print("[bold]Dealer [cyan]wins[/]![/]")
	chips.lose_bet()
    
def push(player,dealer):
	console.print("[bold][green]Dealer[/] and [green]Player[/] tie! It's a [blue]PUSH[/].[/]")

def replay():
	return console.input(
		"\n[bold magenta]Wanna play another hand?[/] Enter [bold blue]Y[/] or [bold blue]N[/]: "
		).lower().startswith("y")

# Set up the Player's chips
player_chips = Chips()  # remember the default value is 100 

while True:
	# if player has no Chips:
		# player lost the game
	if player_chips.total_chips == 0:
		console.print("\n[bold][green]Player[/] out of chips...can't play anymore![/]")
		break
    
	# Print an opening statement
	console.print('[bold]Welcome to BlackJack! Get as close to [blue]21[/] as you can without going over!\n\
	Dealer hits until she reaches [blue]17[/]. Aces count as [blue]1[/] or [blue]11[/].[/]')
    
    # Create & shuffle the deck, deal two cards to each player
	deck = Deck()
	deck.shuffle_deck()

	# creating an instance of player and dealer
	player_hand = Player(False) # Player
	dealer_hand = Player(True)  # Dealer

	# dealing cards to player and dealer
	for x in range(2):
		player_hand.add_card(deck.deal_card())
		dealer_hand.add_card(deck.deal_card())

    
    # Prompt the Player for their bet
	take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
	show_some(player_hand,dealer_hand)
    
	while playing:
        
		# Prompt for Player to Hit or Stand
		hit_or_stand(deck,player_hand) 
        
		# Show cards (but keep one dealer card hidden)
		show_some(player_hand,dealer_hand)  
        
		# If player's hand exceeds 21, run player_busts() and break out of loop
		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			break        


	# If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
	if player_hand.value <= 21:
        
		while dealer_hand.value < 17:
			hit(deck,dealer_hand)    
    
		# Show all cards
		show_all(player_hand,dealer_hand)
        
		# Run different winning scenarios
		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)

		else:
			push(player_hand,dealer_hand)        
    
	# Inform Player of their chips total 
	console.print(f"\nPlayer's total chips are at [bold turquoise]{player_chips.total_chips}[/]")
    
	# Ask to play again
	user_choice = replay()
	if  user_choice== True:
		playing = True
    
	elif not user_choice:
		console.print('Thanks for playing!', style = 'bold purple')
		break
