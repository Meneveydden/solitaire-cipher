#helper functions
def stream_to_string(stream):
	output_string = ''
	for i in stream:
		letter_index = i % 26 if i % 26 != 0 else 26
		output_string += chr(letter_index + 96)
	return output_string

def string_to_stream(message):
	output_stream = []
	for char in message:
		output_stream += [ord(char) - 96]
	return output_stream

def encode(cipherstream, message):
	m = string_to_stream(message)
	for i in range(len(m)):
		m[i] = (cipherstream[i] + m[i]) % 26
	return stream_to_string(m)

def decode(cipherstream, ciphertext):
	c = string_to_stream(ciphertext)
	for i in range(len(c)):
		c[i] = (c[i] - cipherstream[i]) % 26
	return stream_to_string(c)