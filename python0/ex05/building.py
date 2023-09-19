import sys

def ispunct(x) -> bool:
	punct = ".,:;?!'\"/[]()-@$%&"
	for i in punct:
		if x == i: return True
	return False

def building(x: str):
	low = up = punct = space = digit = 0
	for i in x:
		if i.isupper(): up += 1
		elif i.islower():
			low += 1
		elif ispunct(i):
			punct += 1
		elif i.isspace():
			space += 1
		elif i.isdigit():
			digit += 1

	print(f"This text contains {len(x)} characters:")
	print(f"{up} upper letters")
	print(f"{low} lower letters")
	print(f"{punct} punctuation marks")
	print(f"{space} spaces")
	print(f"{digit} digits")

def main():
	size = len(sys.argv)
	try:
		assert size <= 2, "Assertion Error: more than one argument provided."

		if size == 1:
			building(input("What is the text to count?\n"))
		else:
			building(sys.argv[1])
	except AssertionError as e:
		print(e)

if __name__ == "__main__":
	main()