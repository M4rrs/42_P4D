# import ft_filter
import sys

# def ispunct(x) -> bool:
# 	punct = ".,:;?!/[]()-@$%&"
# 	for i in punct:
# 		if x == i: return True
# 	return False

def main():
	try:
		assert len(sys.argv) == 3, "Assertion Error: bad arguments."
		assert  sys.argv[1].isascii() or not sys.argv[1].isnumeric(), "Assertion Error: found punctuation"
	except AssertionError as e:
		print(e)


if __name__ == "__main__":
	main()