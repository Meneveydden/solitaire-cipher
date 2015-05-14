from deck import *
from helpers import *
from card_strings import *
from prompt_strings import *

import sys

def main():

	# random deck generator
	def generate():
		if sys.argv[1] == "generate":
			if len(sys.argv) == 2:
				d = Deck("full")
				d.randomize()
			else:
				if sys.argv[2] == "half":
					d = Deck("half")
					d.randomize()
				elif sys.argv[2] == "full":
					d = Deck("full")
					d.randomize()

			d.print_deck()

		filename = raw_input"Name of file to save to: ")

		text_file = open(filename, "w")
		text_file.write(d.generate_text())
		text_file.close()

	# mode: 0 for decode, 1 for encode
	mode = 1

	def interactive():
		pass

	def encode():
		pass

	def decode():
		pass

	print key_input_prompt

	print test2

if __name__ == "__main__":
	main()
