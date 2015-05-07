import random

class Deck:
	def __init__(self, order, size):

		self.joker_value = 53 if size=='full' else 27 if size=='half' else 0

		#self.order = range(1,53) if size=='full' else range(1,27) if size=='half' else 0
		#random.shuffle(self.order)
		
		# insert joker A before card at a_loc
		#a = self.order.index(a_loc)
		#self.order = self.order[:a] + ['A'] + self.order[a:len(self.order)]

		# insert joker B before card at b_loc
		#b = self.order.index(b_loc)
		#self.order = self.order[:b] + ['B'] + self.order[b:len(self.order)]

		self.size = size
		self.order = order

	def move_jokers(self):
		# move joker A 1 card up
		a = self.order.index('A')
		if a != 0:
			self.order[a], self.order[a-1] = self.order[a-1], self.order[a]
		#edge case
		else:
			self.order.remove('A')
			self.order.append('A')

		#move joker B 2 cards up
		b = self.order.index('B')
		
		if b > 1:
			self.order.remove('B')
			self.order = self.order[:b-2] + ['B'] + self.order[b-2:len(self.order)]
		#edge cases
		else:
			self.order.remove('B')
			if b == 1:
				self.order.append('B')
			elif b == 0:
				self.order = self.order[:-1] + ['B'] + self.order[-1:]

		self.print_deck()


	def joker_cut(self):
		a = self.order.index('A')
		b = self.order.index('B')

		if a < b:
			self.order = self.order[b+1:] + self.order[a:b+1] + self.order[:a]
		else:
			self.order = self.order[a+1:] + self.order[b:a+1] + self.order[:b]

		self.print_deck()

	def count_cut(self):
		bottom_value = self.order[-1] if type(self.order[-1]) is int else self.joker_value
		
		
		# bottom card remains unchanged.
		# count cards from the top of the deck equal to the value of the bottom card. 
		# cut the deck to the card counted, leaving the bottom card in the same place

		self.order = self.order[bottom_value:-1] + self.order[:bottom_value] + self.order[-1:]

		self.print_deck()
		
	def gen_output(self):
		top_value = self.order[0] if type(self.order[0]) is int else self.joker_value

		if type(self.order[top_value]) is int:
			return self.order[top_value]

	def gen_cipherstream(self,length):
		stream = []
		for i in range(length):
			self.move_jokers()
			self.joker_cut()
			self.count_cut()
			if type(self.gen_output()) is int:
				stream.append(self.gen_output())

		return stream

	def print_deck(self):
		print self.order

test_order = [7, 30, 34, 37, 6, 5, 32, 24, 21, 26, 2, 16, 41, 25, 12, 'B', 1, 40, 11, 35, 3, 52, 22, 10, 4, 43, 'A', 33, 31, 44, 29, 14, 50, 45, 18, 47, 15, 9, 36, 17, 42, 13, 38, 27, 8, 51, 23, 49, 48, 19, 20, 39, 46, 28]
test_deck = Deck(test_order, 'full')