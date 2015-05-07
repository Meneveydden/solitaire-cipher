diamond = u"\u2666"
club = u"\u2663"
heart = u"\u2665"
spade = u"\u2660"

# use standard convention for suit ordering. From lowest to highets: diamond, club, heart, spade

deck_size = 'full'

strings_half = {}

strings_full = {}

for i in range(1,27):
	if i == 1:
		strings_half[i] = club + " " + "A"
	elif (i > 1) and (i < 11):
		strings_half[i] = club + " " + str(i)
	elif i == 11:
		strings_half[i] = club + " " + "J"
	elif i == 12:
		strings_half[i] = club + " " + "Q"
	elif i == 13:
		strings_half[i] = club + " " + "K"
	elif i == 14:
		strings_half[i] = spade + " " + "A"
	elif i > 14 and i < 24:
		strings_half[i] = spade + " " + str(i - 13)
	elif i == 24:
		strings_half[i] = spade + " " + "J"
	elif i == 25:
		strings_half[i] = spade + " " + "Q"
	elif i == 26:
		strings_half[i] = spade + " " + "K"

for i in range(1,53):
	if i == 1:
		strings_full[i] = diamond + " " + "A"
	elif (i > 1) and (i < 11):
		strings_full[i] = diamond + " " + str(i)
	elif i == 11:
		strings_full[i] = diamond + " " + "J"
	elif i == 12:
		strings_full[i] = diamond + " " + "Q"
	elif i == 13:
		strings_full[i] = diamond + " " + "K"
	elif i == 14:
		strings_full[i] = club + " " + "A"
	elif i > 14 and i < 24:
		strings_full[i] = club + " " + str(i - 13)
	elif i == 24:
		strings_full[i] = club + " " + "J"
	elif i == 25:
		strings_full[i] = club + " " + "Q"
	elif i == 26:
		strings_full[i] = club + " " + "K"
	elif i == 27:
		strings_full[i] = heart + " " + "A"
	elif (i > 27) and (i < 37):
		strings_full[i] = heart + " " + str(i - 26)
	elif i == 37:
		strings_full[i] = heart + " " + "J"
	elif i == 38:
		strings_full[i] = heart + " " + "Q"
	elif i == 39:
		strings_full[i] = heart + " " + "K"
	elif i == 40:
		strings_full[i] = spade + " " + "A"
	elif i > 40 and i < 50:
		strings_full[i] = spade + " " + str(i - 39)
	elif i == 50:
		strings_full[i] = spade + " " + "J"
	elif i == 51:
		strings_full[i] = spade + " " + "Q"
	elif i == 52:
		strings_full[i] = spade + " " + "K"


strings_half['A'], strings_half['B'], strings_full['A'], strings_full['B'] = "Joker A", "Joker B", "Joker A", "Joker B"
