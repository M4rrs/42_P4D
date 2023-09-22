from ft_filter import ft_filter
import sys


def validLength(S, N):
    if (len(S) >= N):
        return True
    return False


def isInvalid(x):
    return any(char in ".,:;?!/\\[]()-@$%&" for char in x)


def main():

    try:
        assert len(sys.argv) == 3, "Assertion Error: bad arguments."
        assert not isInvalid((str(sys.argv[1]))), (
            "Assertion Error: First argument contains invalid characters."
        )
        assert (str(sys.argv[2])).isnumeric(), (
            "Assertion Error: Second argument does not consist of digits only."
        )

        S = sys.argv[1].split()
        N = int(sys.argv[2])

        filteredList = ft_filter(lambda x: validLength(x, N), S)

        print(filteredList)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
