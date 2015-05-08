from deck import *
from helpers import *
from card_strings import *
from prompt_strings import *

import sys

def main():

	# random deck generator
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
	#if sys.argv > 1:
	#	print "yes"

	# mode: 0 for decode, 1 for encode
	mode = 1

	print key_input_prompt

if __name__ == "__main__":
	main()