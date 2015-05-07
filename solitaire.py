import random

#clarify deck and order

class Deck:
	def __init__(self, size, a_loc, b_loc):

		self.joker_value = 53 if size=='full' else 27 if size=='half' else 0

		self.deck = range(1,53) if size=='full' else range(1,27) if size=='half' else 0
		random.shuffle(self.deck)
		
		# insert joker A before card at a_loc
		a = self.deck.index(a_loc)
		self.deck = self.deck[:a] + ['A'] + self.deck[a:len(self.deck)]

		# insert joker B before card at b_loc
		b = self.deck.index(b_loc)
		self.deck = self.deck[:b] + ['B'] + self.deck[b:len(self.deck)]

	def move_jokers(self):
		# move joker A 1 card up
		a = self.deck.index('A')
		if a != 0:
			self.deck[a], self.deck[a-1] = self.deck[a-1], self.deck[a]
		#edge case
		else:
			self.deck.remove('A')
			self.deck.append('A')

		#move joker B 2 cards up
		b = self.deck.index('B')
		
		if b > 1:
			self.deck.remove('B')
			self.deck = self.deck[:b-2] + ['B'] + self.deck[b-2:len(self.deck)]
		#edge cases
		else:
			self.deck.remove('B')
			if b == 1:
				self.deck.append('B')
			elif b == 0:
				self.deck = self.deck[:-1] + ['B'] + self.deck[-1:]

		self.print_deck()


	def joker_cut(self):
		a = self.deck.index('A')
		b = self.deck.index('B')

		if a < b:
			self.deck = self.deck[b+1:] + self.deck[a:b+1] + self.deck[:a]
		else:
			self.deck = self.deck[a+1:] + self.deck[b:a+1] + self.deck[:b]

		self.print_deck()

	def count_cut(self):
		bottom_value = self.deck[-1] if type(self.deck[-1]) is int else self.joker_value
		
		
		# bottom card remains unchanged.
		# count cards from the top of the deck equal to the value of the bottom card. 
		# cut the deck to the card counted, leaving the bottom card in the same place

		self.deck = self.deck[bottom_value:-1] + self.deck[:bottom_value] + self.deck[-1:]

		self.print_deck()
		
	def gen_output(self):
		top_value = self.deck[0] if type(self.deck[0]) is int else self.joker_value

		if type(self.deck[top_value]) is int:
			return self.deck[top_value]

	def gen_cipherstream(self,length):
		stream = []
		for i in range(length):
			self.move_jokers()
			self.joker_cut()
			self.count_cut()
			stream.append(self.gen_output())

		return stream

	def print_deck(self):
		print self.deck